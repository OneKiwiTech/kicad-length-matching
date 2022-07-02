from ..observable.observable import Observable
from ..data.netclass import *

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

    def set_pads(self, pads):
        self.pads = pads

class PadPin:
    def __init__(self, reference, pad):
        self.reference = reference
        self.pad = pad
        self.pin = reference + "." + pad

class Model:
    def __init__(self):
        self.status1 = Observable('')
        self.status2 = Observable('')
        self.classes = get_net_classes()
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

    def set_status2(self, value):
        self.status2.set(value)



