import json
from ..kicad.netclass import *
from ..kicad.stackup import *
from ..kicad.lengthtrack import *

class Model:
    def __init__(self):
        self.classes = get_net_classes()
        self.thickness = get_thickness_stackup()
        self.nameclasses = {}
        self.statusinit = False

    def export_to_json(self):
        path = get_pcb_path()
        name = get_pcb_name() + '_length-matching.json'
        json_file = os.path.join(path, name)
        # Serializing json 
        results = json.dumps(self.nameclasses, indent = 4)

        # Writing to sample.json
        with open(json_file, "w") as outfile:
            outfile.write(results)
    
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
        #jsdata = json.dumps(self.nameclasses, indent = 4)
        #logging.debug(jsdata)

    def compare_data(self):
        self.statusinit = True
        self.init_data()
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

                    
    def get_track_length(self):
        for netclass in self.nameclasses['classes']:
            nets = netclass['nets']
            for net in nets:
                reference1 = net['reference1']
                reference2 = net['reference2']
                pad1 = net['pad1']
                pad2 = net['pad2']
                track_data = get_min_track_lenght(reference1, pad1, reference2, pad2)
                net['viacount'] = len(track_data.vias)
                
                sum_via_length = 0.0
                for via in track_data.vias:
                    stackup = []
                    start = 2*via.start
                    end = 2*via.end
                    if end >= len(self.thickness):
                        end = len(self.thickness)
                        stackup = self.thickness[start:]
                    else:
                        stackup = self.thickness[start:end+1]
                    offset = 0.0
                    offset = (stackup[0] + stackup[len(stackup) - 1])/2
                    via_length = 0.0
                    for item in stackup:
                        via_length += item
                    via_length = via_length - offset
                    sum_via_length += via_length
                net['vialength'] = sum_via_length

                sum_track_length = 0.0
                for track in track_data.tracks:
                    sum_track_length += track.GetLength()
                sum_track_length = sum_track_length/pcbnew.IU_PER_MM
                net['tracklength'] = sum_track_length
                net['totallength'] = sum_track_length + sum_via_length

        #jsdata = json.dumps(self.nameclasses, indent = 4)
        #logging.debug(jsdata)

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