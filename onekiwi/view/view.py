import wx
from .dialog import *
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

class ClassPanelView(ClassPanel):
    def __init__( self, parent):
        ClassPanel.__init__(self, parent)

class ExtendedNetPanelView(ExtendedNetPanel):
    def __init__( self, parent):
        ExtendedNetPanel.__init__(self, parent)

class SettingPanelView(SettingPanel):
    def __init__( self, parent):
        SettingPanel.__init__(self, parent)

class DisplayPanelView(DisplayPanel):
    def __init__( self, parent):
        DisplayPanel.__init__(self, parent)

class InfoPanelView(InfoPanel):
    def __init__( self, parent):
        InfoPanel.__init__(self, parent)



