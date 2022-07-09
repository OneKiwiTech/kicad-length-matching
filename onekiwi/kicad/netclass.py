from .board import *

class PadNet:
    def __init__(self, reference, pad):
        self.reference = reference
        self.pad = pad
        self.pin = reference + "." + pad

def get_net_classes():
    board = get_board()
    netclasses = board.GetDesignSettings().GetNetClasses().NetClasses()
    classes = [str(k) for k, v in netclasses.items()]
    return classes

def get_net_names(netclass):
    board = get_board()
    classes = board.GetDesignSettings().GetNetClasses()
    nets = [str(net) for net in classes.Find(netclass).NetNames()]
    return nets

def get_net_code(netname):
    board = get_board()
    netcode = board.GetNetcodeFromNetname(netname)
    return netcode

def get_pin(reference, pad):
    board = get_board()
    return board.FindFootprintByReference(reference).FindPadByNumber(pad)
    
def get_pads_from_net_name(netname):
    pads = []
    board = get_board()
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
