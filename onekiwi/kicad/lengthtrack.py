import logging
import pcbnew

from .findtrack import FindNet
from .netclass import *

ANY_LAYER = 'Any'

class TrackLength:
    def __init__(self, ref_start, pad_start, ref_end, pad_end, thickness):
        self.name = ''
        self.code = 0
        self.ref_start = ref_start
        self.pad_start = pad_start
        self.ref_end = ref_end
        self.pad_end = pad_end
        self.point_start = None
        self.point_end = None
        self.layer_start = ANY_LAYER
        self.layer_end = ANY_LAYER
        self.tracks = []
        self.thickness = thickness
        self.hole_pads = []

    def get_info(self):
        board = get_board()
        pin_start = board.FindFootprintByReference(self.ref_start).FindPadByNumber(self.pad_start)
        pin_end = board.FindFootprintByReference(self.ref_end).FindPadByNumber(self.pad_end)
        self.name = pin_start.GetNetname()
        self.code = board.GetNetcodeFromNetname(self.name)
        self.tracks = list(board.TracksInNet(self.code)) #Convert Tuple to List
        start_pad_layer = board.FindFootprintByReference(self.ref_start).IsFlipped()
        end_pad_layer = board.FindFootprintByReference(self.ref_end).IsFlipped()
        if self.ref_start == self.ref_end and self.pad_start == self.pad_end:
            self.tracks.clear()

        self.point_start = pin_start.GetPosition()
        if pin_start.GetAttribute() == pcbnew.PAD_ATTRIB_SMD:
            if start_pad_layer == True:
                # F_Cu = 31
                self.layer_start = pcbnew.B_Cu
            else:
                # F_Cu = 0
                self.layer_start = pcbnew.F_Cu

        self.point_end = pin_end.GetPosition()
        if pin_end.GetAttribute() == pcbnew.PAD_ATTRIB_SMD:
            if end_pad_layer == True:
                self.layer_end = pcbnew.B_Cu
            else:
                self.layer_end = pcbnew.F_Cu

    def find_hole_pad(self):
        pads = get_pads_from_net_name(self.name)
        for item in pads:
            pin = get_pin(item.reference, item.pad)
            if pin.GetPosition() != self.point_start and pin.GetPosition() != self.point_end:
                # Pad type: Through Hole
                if pin.GetAttribute() == pcbnew.PAD_ATTRIB_PTH:
                    self.hole_pads.append(pin)


    def find_min_track(self):
        self.get_info()
        #logging.debug('netname: %s' %self.name)
        self.find_hole_pad()
        findtrack = FindNet(self.tracks, self.point_start, self.point_end, self.layer_start, self.layer_end, self.thickness, self.hole_pads)
        return findtrack.get_min_track()

