import logging
from ..kicad.netclass import *
from ..kicad.stackup import *
from ..kicad.lengthtrack import *

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

    def init_data(self):
        for name in self.classes:
            self.netclasses.append(NetClass(name))

        for nameclass in self.netclasses:
            temp_nets = []
            nets = []
            temp_nets = get_net_names(nameclass.name)
            pads = []
            for name in temp_nets:
                netcode = get_net_code(name)
                pads = get_pads_from_net_name(name)
                net = NetName(name, netcode, pads[0].reference, pads[0].pad, pads[1].reference, pads[1].pad)
                net.set_pads(pads)
                nets.append(net)
            nameclass.set_nets(nets)

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

