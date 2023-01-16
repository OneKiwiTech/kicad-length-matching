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

    def GetChoiceClassValue(self):
        return self.choiceClass.GetValue()

    def GetCChoiceClassSelection(self):
        return self.choiceClass.GetSelection()

    def UpdateFiltterFrom(self, classes):
        self.filtterFrom.Clear()
        self.filtterFrom.Append(classes)
        self.filtterFrom.SetSelection(0)

    def GetFiltterFromValue(self):
        ind = self.filtterFrom.GetSelection()
        return str(self.filtterFrom.GetString(ind))
    
    def UpdateFiltterTo(self, classes):
        self.filtterTo.Clear()
        self.filtterTo.Append(classes)
        self.filtterTo.SetSelection(0)
    
    def GetFiltterToValue(self):
        ind = self.filtterTo.GetSelection()
        return str(self.filtterTo.GetString(ind))

    def UpdateListNet(self, item):
        self.listNet.Clear()
        self.listNet.Append(item)
        self.listNet.SetSelection(0)
        
    

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



