from cgitb import text
import wx
from .dialog import *
from ..kicad.board import get_current_unit
from ..version import version

class LengthMatchingView(LengthMatchingDialog):
    def __init__(self):
        LengthMatchingDialog.__init__(self, None)
        self.window = wx.GetTopLevelParent(self)

    def HighResWxSize(self, window, size):
        """Workaround if wxWidgets Version does not support FromDIP"""
        if hasattr(window, "FromDIP"):
            return window.FromDIP(size)
        else:
            return size

    def SetUnitText(self, unit):
        text = 'Unit: ' + unit
        self.textUnit.SetLabelText(text)
    
    def SetNetText(self, net):
        text = 'Net: ' + net
        self.textNet.SetLabelText(text)

    def AddViasSize(self, vias):
        self.choiceVia.Append(vias)
        self.choiceVia.SetSelection(0)

    def AddLayersName(self, names):
        self.choiceLayer.Append(names)
        self.choiceLayer.SetSelection(0)

    def AddAreasName(self, names):
        self.choiceArea.Append(names)
        self.choiceArea.SetSelection(0)