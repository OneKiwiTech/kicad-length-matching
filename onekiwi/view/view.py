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

class xNetPanel(xNetPanelBase):
    def __init__(self, parent):
        xNetPanelBase.__init__(self, parent)

