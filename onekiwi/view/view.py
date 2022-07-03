#!/usr/bin/env python3
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

    def UpadateNets(self, nets):
        self.textLength.LabelText = '123'
        rows = self.gridNet.GetNumberRows()
        self.gridNet.DeleteRows(0, rows)
        self.gridNet.AppendRows(len(nets))
        for row, net in enumerate(nets, start=0):   # Python indexes start at zero
            self.gridNet.SetCellValue(row, 0, net.name)
            #pads = get_pads_from_net_name(net)
            pins = [item.pin for item in net.pads]
            choice_editor = wx.grid.GridCellChoiceEditor(pins, True)
            self.gridNet.SetCellEditor(row, 1, choice_editor)
            self.gridNet.SetCellEditor(row, 2, choice_editor)
            self.gridNet.SetCellValue(row, 1, pins[0])
            self.gridNet.SetCellValue(row, 2, pins[1])



class xNetPanel(xNetPanelBase):
    def __init__(self, parent):
        xNetPanelBase.__init__(self, parent)

