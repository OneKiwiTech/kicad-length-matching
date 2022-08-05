import json
import logging
from typing import List
from ..kicad.netclass import *
from ..kicad.stackup import *
from ..kicad.lengthtrack import *

class DataNet:
    def __init__(self, name, code, tracks):
        self.name = name
        self.code = code
        self.tracks = tracks

class DataClass:
    def __init__(self, name, nets):
        self.name = name
        self.nets:List[DataNet] = nets

class Model:
    def __init__(self):
        self.classes = get_net_classes()
        self.thickness = get_thickness_stackup()
        self.nameclasses = {}
        self.dataclass:List[DataClass] = []
        self.statusinit = False
        self.classid = None
        self.netid =None
    
    def get_unit(self):
        unit = get_current_unit()
        # pcbnew.EDA_UNITS_INCHES = 0
        if unit == pcbnew.EDA_UNITS_INCHES:
            return 'in'
        # pcbnew.EDA_UNITS_MILLIMETRES = 1
        elif unit == pcbnew.EDA_UNITS_MILLIMETRES:
            return 'mm'
        # pcbnew.EDA_UNITS_MILS = 5
        elif unit == pcbnew.EDA_UNITS_MILS:
            return 'mil'

    def export_to_json(self):
        path = get_pcb_path()
        name = get_pcb_name() + '_length-matching.json'
        json_file = os.path.join(path, name)
        # Serializing json 
        results = json.dumps(self.nameclasses, indent = 4)

        # Writing to sample.json
        with open(json_file, "w") as outfile:
            outfile.write(results)
        return json_file
    
    def read_json(self):
        data = {}
        status = False
        path = get_pcb_path()
        name = get_pcb_name() + '_length-matching.json'
        json_file = os.path.join(path, name)
        # Check If File Exists
        if os.path.exists(json_file):
            with open(json_file) as json_file:
                data = json.load(json_file)
                status = True
        return status, data

    def init_data(self):
        self.nameclasses["classes"] = []
        for name in self.classes:
            net = {"name": name, "nets":[]}
            self.nameclasses['classes'].append(net)
            
        for nameclass in self.nameclasses['classes']:
            nets = []
            nets = get_net_names(nameclass['name'])
            
            for index, name in enumerate(nets):
                pads = []
                code = get_net_code(name)
                pads = get_pads_from_net_name(name)
                if len(pads) < 2:
                    return name
                ref1 = pads[0].reference
                pad1 = pads[0].pad
                pin1 = ref1 + '.' + pad1
                ref2 = pads[1].reference
                pad2 = pads[1].pad
                pin2 = ref2 + '.' + pad2
                net = {'name': name, 'code': code, 'reference1': ref1, 'pad1': pad1, 'pin1': pin1, 'reference2': ref2, 'pad2':pad2, 'pin2': pin2, 'pads': []}
                nameclass['nets'].append(net)
                for pad in pads:
                    pad_info = {'reference': pad.reference, 'pad': pad.pad, 'pin': pad.pin}
                    nameclass['nets'][index]['pads'].append(pad_info)
        return None
        #jsdata = json.dumps(self.nameclasses, indent = 4)
        #logging.debug(jsdata)

    def compare_data(self):
        self.statusinit = True
        msg = self.init_data()
        if msg != None:
            return msg
        status, data = self.read_json()
        if status == True:
            for netclass in self.nameclasses['classes']:
                for jsonclass in data['classes']:
                    if jsonclass['name'] == netclass['name']:
                        for net in netclass['nets']:
                            for jsonnet in jsonclass['nets']:
                                if jsonnet['name'] == net['name'] and jsonnet['code'] == net['code']:
                                    pins = [pin['pin'] for pin in net['pads']]
                                    # check if reference and pad exists
                                    if jsonnet['pin1'] in pins:
                                        net['reference1'] = jsonnet['reference1']
                                        net['pad1'] = jsonnet['pad1']
                                        net['pin1'] = jsonnet['pin1']
                                    else:
                                        net['reference1'] = net['pads'][0]['reference']
                                        net['pad1'] = net['pads'][0]['pad']
                                        net['pin1'] = net['pads'][0]['pin']

                                    if jsonnet['pin2'] in pins:
                                        net['reference2'] = jsonnet['reference2']
                                        net['pad2'] = jsonnet['pad2']
                                        net['pin2'] = jsonnet['pin2']
                                    else:
                                        net['reference2'] = net['pads'][1]['reference']
                                        net['pad2'] = net['pads'][1]['pad']
                                        net['pin2'] = net['pads'][1]['pin']
        return None

                    
    def get_track_length(self):
        for netclass in self.nameclasses['classes']:
            nets = netclass['nets']
            datanets: List[DataNet] = []
            for net in nets:
                reference1 = net['reference1']
                reference2 = net['reference2']
                pad1 = net['pad1']
                pad2 = net['pad2']
                track_data = TrackLength(reference1, pad1, reference2, pad2, self.thickness)
                info = track_data.find_min_track()
                net['status'] = info.status
                net['viacount'] = info.via_count
                net['vialength'] = info.via_length
                net['tracklength'] = info.track_length
                net['totallength'] = info.total_length

                data = DataNet(net['name'], net['code'], info.tracks)
                datanets.append(data)
            dataclass = DataClass(netclass['name'], datanets)
            self.dataclass.append(dataclass)

        #jsdata = json.dumps(self.nameclasses, indent = 4)
        #logging.debug(jsdata)

    def highlight_net(self, class_id, net_id):
        self.clear_highlight_net()
        self.set_highlight_net(class_id, net_id)

    def set_highlight_net(self, class_id, net_id):
        self.classid = class_id
        self.netid = net_id
        tracks = self.dataclass[class_id].nets[net_id].tracks
        for track in tracks:
            track.SetBrightened()
        pcbnew.Refresh()

    def clear_highlight_net(self):
        if self.classid != None and self.netid != None:
            tracks = self.dataclass[self.classid].nets[self.netid].tracks
            for track in tracks:
                track.ClearBrightened()
            pcbnew.Refresh()

"""
data class
"classes": [
    {
        "name": "FlexSPI",
        "nets": [
            {
                "name": "FlexSPI_A_CLK",
                "code": 248,
                "reference1": "U7",
                "pad1": "6",
                "reference2": "U3",
                "pad2": "L4",
                "pads": [
                    {
                        "reference": "U7",
                        "pad": "6",
                        "pin": "U7.6"
                    },
                    {
                        "reference": "U3",
                        "pad": "L4",
                        "pin": "U3.L4"
                    }
                ],
                "viacount": 0,
                "vialength": 0.0,
                "tracklength": 39.1458,
                "totallength": 39.1458
            }
        ]
    },
    {
    }
]
"""