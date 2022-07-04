import logging
from ..kicad.netclass import *
from ..kicad.stackup import *
from ..kicad.lengthtrack import *
import json

class NetClass:
    def __init__(self, name):
        self.name = name
        self.nets = []
    
    def set_nets(self, nets):
        self.nets = nets

class NetName:
    def __init__(self, name, code, reference1, pad1, reference2, pad2):
        self.name = name
        self.code = code
        self.reference1 = reference1
        self.pad1 = pad1
        self.reference2 = reference2
        self.pad2 = pad2
        self.totallength = 0.0
        self.tracklength = 0.0
        self.vialength = 0.0
        self.viacount = 0.0

    def set_pads(self, pads):
        self.pads = pads

class PadPin:
    def __init__(self, reference, pad):
        self.reference = reference
        self.pad = pad
        self.pin = reference + "." + pad

class Model:
    def __init__(self):
        self.classes = get_net_classes()
        self.thickness = get_thickness_stackup()
        self.netclasses = []
        self.nameclasses = {}
        self.nameclasses["classes"] = []

    def to_json(self):
        #board = get_board()
        path = get_pcb_path()
        logging.debug('path %s' %path)
        name = get_pcb_name() + '_length-matching.json'
        logging.debug('name %s' %name)
        json_file = os.path.join(path, name)
        logging.debug('file %s' %json_file)
        # Serializing json 
        json_object = json.dumps(self.netclasses, indent = 4)
        #print(json_object)
        # Writing to sample.json
        #with open(json_file, "w") as outfile:
            #outfile.write(json_object)

    def init_data(self):
        for name in self.classes:
            self.netclasses.append(NetClass(name))

        for nameclass in self.netclasses:
            temp_nets = []
            nets = []
            pads = []
            temp_nets = get_net_names(nameclass.name)
            for name in temp_nets:
                netcode = get_net_code(name)
                pads = get_pads_from_net_name(name)
                net = NetName(name, netcode, pads[0].reference, pads[0].pad, pads[1].reference, pads[1].pad)
                net.set_pads(pads)
                nets.append(net)
            nameclass.set_nets(nets)

    def init_data2(self):
        for name in self.classes:
            net = {"name": name, "nets":[]}
            self.nameclasses['classes'].append(net)
            
        for nameclass in self.nameclasses['classes']:
            nets = []
            nets = get_net_names(nameclass['name'])
            for ind, name in enumerate(nets):
                pads = []
                code = get_net_code(name)
                pads = get_pads_from_net_name(name)
                net = {'name': name, 'code': code, 'reference1': pads[0].reference, 'pad1':pads[0].pad, 'reference2': pads[1].reference, 'pad2':pads[1].pad, 'pads': []}
                #self.nameclasses['classes'][index]['nets'].append(net)
                nameclass['nets'].append(net)
                for pad in pads:
                    pad_info = {'reference': pad.reference, 'pad': pad.pad, 'pin': pad.pin}
                    nameclass['nets'][ind]['pads'].append(pad_info)
        #jsdata = json.dumps(self.nameclasses, indent = 4)
        #logging.debug(jsdata)

    def get_track_length2(self):
        logging.debug('get_track_length2')
        for netclass in enumerate(self.nameclass['classes']):
            nets = netclass['nets']
            for net in nets:
                logging.debug(net)

    def get_track_length(self):
        logging.debug('get_track_length')
        for thick in self.thickness:
            logging.debug('thickness: %f', thick)
        for netclass in self.netclasses:
            logging.debug('class: %s', netclass.name)
            nets = netclass.nets
            for net in nets:
                logging.debug('net: %s', net.name)
                track_data = get_min_track_lenght(net.reference1, net.pad1, net.reference2, net.pad2)
                net.viacount = len(track_data.vias)
                sum_via_length = 0.0
                for via in track_data.vias:
                    stackup = []
                    start = 2*via.start
                    end = 2*via.end
                    logging.debug('via start: %d - %d' %(via.start, via.end))
                    logging.debug('via stack: %d - %d' %(start, end))
                    if end >= len(self.thickness):
                        end = len(self.thickness)
                        stackup = self.thickness[start:]
                        logging.debug('zz1')
                        logging.debug(stackup)
                    else:
                        logging.debug('zz2')
                        stackup = self.thickness[start:end+1]
                        logging.debug(stackup)
                    offset = 0.0
                    offset = (stackup[0] + stackup[len(stackup) - 1])/2
                    logging.debug('offset', offset)
                    via_length = 0.0
                    logging.debug('zz3')
                    for item in stackup:
                        logging.debug(item)
                        via_length += item
                        logging.debug('vialength %f' %via_length)
                        #print('name %s %f' %(item.name, item.thickness))
                    logging.debug('zz4')
                    via_length = via_length - offset
                    logging.debug('vialength %f' %via_length)
                    sum_via_length += via_length
                    logging.debug('sum_via_length %f' %sum_via_length)
                logging.debug('zz5')
                net.vialength = sum_via_length

                sum_track_length = 0.0
                for track in track_data.tracks:
                    sum_track_length += track.GetLength()
                net.tracklength = sum_track_length/pcbnew.IU_PER_MM
                net.totallength = net.tracklength + net.vialength
                logging.debug('%f %f %f' %(net.tracklength, net.vialength, net.viacount))
                logging.debug('==============')
        #logging.debug('end get_track_length')
    ############################
        """"
        net = self.netclasses[0].nets[0]
        track_data = get_min_track_lenght(net.reference1, net.pad1, net.reference2, net.pad2)
        via_counts = len(track_data.vias)
        sum_via_length = 0.0
        
        for via in track_data.vias:
            stackupsv = []
            stackupsv.clear()
            start = 2*via.start
            end = 2*via.end
            if end >= len(self.stackups):
                end = len(self.stackups)
                stackupsv = self.stackups[start:]
            else:
                stackupsv = self.stackups[start:end+1]
            offset = (stackupsv[0].thickness + stackupsv[len(stackupsv) - 1].thickness)/2
            via_length = 0
            for item in stackupsv:
                via_length += item.thickness
                #print('name %s %f' %(item.name, item.thickness))
            via_length = via_length - offset
            sum_via_length += via_length

        sum = 0.0
        for track in track_data.tracks:
            #startpoint = track.GetStart()
            #endpoint = track.GetEnd()
            #ind = track_data.tracks.index(track) + 1
            #print('%d, %s,%s' %(ind, startpoint, endpoint))
            sum += track.GetLength()
        sum_track_length = sum/pcbnew.IU_PER_MM
        return sum_track_length, sum_via_length, via_counts
        """

"""
"netclasses":{
    "name": "name class"
    "nets":[
        {
            "name": "net name"
            "code": "net code"
            "reference1": "reference start"
            "pad1": "pad start"
            "reference2": "reference end"
            "pad2": "pad end"
            "pads":[
                "reference": "reference"
                "pad": "pad"
                "pin": "reference.pad"
            ]
        }
    ]
}
"""

