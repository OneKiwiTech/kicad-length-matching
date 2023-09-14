from .board import *

class PadNet:
    def __init__(self, reference, pad):
        self.reference = reference
        self.pad = pad
        self.pin = reference + "." + pad

def get_net_classes(board):
    #board = get_board()
    #netclasses = board.GetAllNetClasses()
    netclasses = board.GetNetClasses()
    classes = [str(k) for k, v in netclasses.items()]
    return classes

def get_net_names(board, netclass):
    netnames = board.GetNetsByName().values()
    nets = []
    for net in netnames:
        if net.GetNetClassName() == netclass:
            netname = net.GetNetname()
            if len(netname): #ignore empty netname (e.g. found in Default netclass)
                nets.append(netname)
    return nets

def get_net_code(board, netname):
    netcode = board.GetNetcodeFromNetname(netname)
    return netcode

def get_pin(board, reference, pad):
    return board.FindFootprintByReference(reference).FindPadByNumber(pad)
    
def get_pads_from_net_name(board, netname):
    pads = []
    netcode = board.GetNetcodeFromNetname(netname)
    footprints = board.GetFootprints()
    for footprint in footprints:
        for pad in footprint.Pads():
            netpad = str(pad.GetNetname())
            netpadcode = board.GetNetcodeFromNetname(netpad)
            if netcode == netpadcode:
                ref = str(footprint.GetReference())
                pin = str(pad.GetPadName())

                pads.append(PadNet(ref, pin))
    return pads
