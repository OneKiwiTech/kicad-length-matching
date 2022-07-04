#!/usr/bin/env python3
import logging
import wx
import wx.grid

from .dialog import *

class DialogMain(LengthMatchingDialog):
    def __init__(self, parent):
        LengthMatchingDialog.__init__(self, parent)
        self.SetTitle('Length Matching')
    
    def SetText(self, status):
        self.textStatus.LabelText = status

class NetPanel(NetPanelBase):
    def __init__(self, parent):
        NetPanelBase.__init__(self, parent)
    
    def UpdateClass(self, classes):
        self.comboClass.Append(classes)

    def GetClassSelection(self):
        return self.comboClass.GetValue()

    def UpadateNets(self, nets):
        rows = self.gridNet.GetNumberRows()
        self.gridNet.DeleteRows(0, rows)
        self.gridNet.AppendRows(len(nets))
        for row, net in enumerate(nets, start=0):
            self.gridNet.SetCellValue(row, 0, net.name)
            pins = [item.pin for item in net.pads]
            choice_editor = wx.grid.GridCellChoiceEditor(pins, True)
            self.gridNet.SetCellEditor(row, 1, choice_editor)
            self.gridNet.SetCellEditor(row, 2, choice_editor)
            self.gridNet.SetCellValue(row, 1, pins[0])
            self.gridNet.SetCellValue(row, 2, pins[1])
    
    def UpadateLength(self, netclasses):
        logging.debug('Upadate Length')
        nets = netclasses[1].nets
        for index, net in enumerate(nets, start=0):
            #viacount = round(net.viacount, 4)
            vialength = round(net.vialength, 4)
            tracklength = round(net.tracklength, 4)
            totallength = round(net.totallength, 4)
            self.gridNet.SetCellValue(index, 3, str(net.viacount))
            self.gridNet.SetCellValue(index, 4, str(vialength))
            self.gridNet.SetCellValue(index, 5, str(tracklength))
            self.gridNet.SetCellValue(index, 6, str(totallength))

class xNetPanel(xNetPanelBase):
    def __init__(self, parent):
        xNetPanelBase.__init__(self, parent)

