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

    def GetEditClassName(self):
        return self.editClass.GetValue()
    
    def SetEditClassName(self, text):
        self.editClass.SetValue(text)

    def AddItemChoiceClass(self, item):
        self.choiceClass.Append(item)
    
    def UpdateChoiceClass(self, classes):
        self.choiceClass.Clear()
        self.choiceClass.Append(classes)
        self.choiceClass.SetSelection(0)

    def GetCChoiceClassValue(self):
        return self.choiceClass.GetValue()

    def GetCChoiceClassSelection(self):
        return self.choiceClass.GetSelection()

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



