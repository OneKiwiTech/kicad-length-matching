import select
from ..model.model import Model
from ..model.temp import TempNetClass
from ..model.net import NetData
from ..model.model import NetClass
from ..view.view import *
from ..kicad.board import *
from ..view.viewclass import ClassPanelView
from ..view.viewextendednet import ExtendedNetPanelView
from ..view.viewsetting import SettingPanelView
from ..view.viewdisplay import DisplayPanelView
from ..view.viewinfo import InfoPanelView
from ..view.viewdebug import DebugPanelView
from .logtext import LogText
from typing import List
import sys
import os
import logging
import logging.config
import wx
import json

class Controller:
    def __init__(self, board):
        self.view = LengthMatchingView()
        self.classPanel = ClassPanelView(self.view.notebook)
        self.xNetPanel = ExtendedNetPanelView(self.view.notebook)
        self.settingPanel = SettingPanelView(self.view.notebook)
        self.displayPanel = DisplayPanelView(self.view.notebook)
        self.infoPanel = InfoPanelView(self.view.notebook)
        self.debugPanel = DebugPanelView(self.view.notebook)
        
        self.view.notebook.AddPage(self.classPanel, "Class")
        self.view.notebook.AddPage(self.xNetPanel, "Extended Net")
        self.view.notebook.AddPage(self.settingPanel, "Setting")
        self.view.notebook.AddPage(self.displayPanel, "Display")
        self.view.notebook.AddPage(self.infoPanel, "Net Info")
        self.view.notebook.AddPage(self.debugPanel, "Debug")

        self.board = board
        self.references = []
        self.classes = []
        self.temp:TempNetClass = TempNetClass()
        self.netpads:List[NetData] = []

        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)
        self.GetReference()

        # Connect Events
        self.view.buttonLoadSetting.Bind(wx.EVT_BUTTON, self.OnLoadSetting)
        self.view.buttonSaveSetting.Bind(wx.EVT_BUTTON, self.OnSaveSetting)
        self.view.buttonUpdateLength.Bind(wx.EVT_BUTTON, self.OnUpdateLength)
        self.view.buttonClearHighlight.Bind(wx.EVT_BUTTON, self.OnClearHighlight)
        self.view.buttonClearLog.Bind(wx.EVT_BUTTON, self.OnButtonClear)
        self.view.buttonCopyLog.Bind(wx.EVT_BUTTON, self.OnButtonCopy)
        self.view.buttonExit.Bind(wx.EVT_BUTTON, self.OnButtonClose)

        self.classPanel.buttonAddClass.Bind(wx.EVT_BUTTON, self.OnAddClass)
        self.classPanel.buttonUpdateNet.Bind(wx.EVT_BUTTON, self.OnUpdateNet)
        self.classPanel.editFrom.Bind(wx.EVT_TEXT, self.OnFilterFromChange)
        self.classPanel.editTo.Bind(wx.EVT_TEXT, self.OnFilterToChange)
        self.classPanel.choiceReferenceFrom.Bind(wx.EVT_CHOICE, self.OnChoiceReferenceFrom)
        self.classPanel.choiceReferenceTo.Bind(wx.EVT_CHOICE, self.OnChoiceReferenceTo)
        self.classPanel.choicePinStart.Bind(wx.EVT_CHOICE, self.OnChoiceReferenceStart)
        self.classPanel.choicePinEnd.Bind(wx.EVT_CHOICE, self.OnChoiceReferenceEnd)
        self.classPanel.dataViewClass.Bind(wx.EVT_LEFT_DCLICK, self.TableClassOnLeftDClick)
        self.classPanel.buttonRenameClass.Bind(wx.EVT_BUTTON, self.OnRenameClass)
        self.classPanel.buttonRemoveClass.Bind(wx.EVT_BUTTON, self.OnRemoveClass)
        self.classPanel.buttonUpdateClass.Bind(wx.EVT_BUTTON, self.OnUpdateClass)
        self.classPanel.editNet.Bind(wx.EVT_TEXT, self.OnFilterNetChange)
        

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    def init_logger(self, texlog):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)
        # and to our GUI
        handler2 = LogText(texlog)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s",
            datefmt="%Y.%m.%d %H:%M:%S",
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)
        return logging.getLogger(__name__)

    def GetReference(self):
        footprints = self.board.GetFootprints()
        for footprint in footprints:
            ref = str(footprint.GetReference())
            self.references.append(ref)
        self.references.sort()
        self.classPanel.UpdateReferenceFrom(self.references)
        self.classPanel.UpdateReferenceTo(self.references)

    def OnLoadSetting(self, event):
        self.model.get_json_data()
        self.classes.clear()
        for data in self.model.classes:
            self.classes.append(data.name)
        self.classPanel.UpdateChoiceClass(self.classes)
        self.netpads.clear()
        self.netpads = self.model.classes[0].nets
        for ind, ref in enumerate(self.references):
            if self.model.classes[0].start == ref:
                self.classPanel.choiceReferenceFrom.SetSelection(ind)
            if self.model.classes[0].end == ref:
                self.classPanel.choiceReferenceTo.SetSelection(ind)
        self.UpadateClassTable(self.netpads, False)

    def OnSaveSetting(self, event):
        self.model.save_setting()

    def OnUpdateLength(self, event):
        self.logger.info('OnUpdateLength')

    def OnClearHighlight(self, event):
        self.logger.info('OnClearHighlight')

    def OnButtonClear(self, event):
        self.view.textLog.SetValue('')

    def OnButtonCopy(self, event):
        log = self.view.textLog.GetValue()
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(log))
            wx.TheClipboard.Close()

    def OnButtonClose(self, event):
        self.Close()

    # Class
    def OnAddClass(self, event):
        name = self.classPanel.GetEditClassName()
        if name != '':
            if name not in self.classes:
                self.classes.append(name)
                self.classPanel.SetEditClassName('')
                self.classPanel.UpdateChoiceClass(self.classes)
            else:
                self.logger.info('Name already exists!')
        else:
            self.logger.info('Please enter name!')
    
    def OnUpdateNet(self, event):
        if len(self.classes) < 1:
            self.logger.info('Please create class name')
            return
        self.netpads.clear()
        power_names = ['GND', 'GNDA', 'GNDD', 'Earth', 'VSS', 'VSSA', 'VCC', 'VDD', 'VBUS']
        ref1 = self.classPanel.GetReferenceFromValue()
        ref2 = self.classPanel.GetReferenceToValue()
        self.logger.info('Start %s, End %s', ref1, ref2)

        ref_start = self.board.FindFootprintByReference(ref1)
        ref_end = self.board.FindFootprintByReference(ref2)
        for pad1 in ref_start.Pads():
            name1 = str(pad1.GetNetname())
            code1 = self.board.GetNetcodeFromNetname(name1)
            pin1 = str(pad1.GetPadName())
            for pad2 in ref_end.Pads():
                name2 = str(pad2.GetNetname())
                code2 = self.board.GetNetcodeFromNetname(name2)
                pin2 = str(pad2.GetPadName())
                if code1 == code2 and name2 not in power_names:
                    if name2 not in [data.name1 for data in self.netpads]:
                        self.logger.info('Net %s', name2)
                        net = NetData('net', name2, str(code2), ref1, pin1, '', '', ref2, pin2, '', '', '')
                        net.pad1s.append(pin1)
                        net.pad2s.append(pin2)
                        self.netpads.append(net)
                    else:
                        for data in self.netpads:
                            if data.code1 == str(code2):
                                if pin1 not in data.pad1s:
                                    data.pad1s.append(pin1)
                                if pin2 not in data.pad2s:
                                    data.pad2s.append(pin2)

        self.netpads.sort(key=lambda x: x.name1)
        self.UpadateClassTable(self.netpads, False)
        
    
    def OnFilterFromChange(self, event):
        value = event.GetEventObject().GetValue()
        references = []
        for item in self.references:
            if item.rfind(value) != -1:
                references.append(item)
        self.classPanel.UpdateReferenceFrom(references)
    
    def OnFilterToChange(self, event):
        value = event.GetEventObject().GetValue()
        references = []
        for item in self.references:
            if item.rfind(value) != -1:
                references.append(item)
        self.classPanel.UpdateReferenceTo(references)
    
    def OnFilterNetChange(self, event):
        value = event.GetEventObject().GetValue()
        self.logger.info('OnFilterNetChange %s', value)
        for net in self.netpads:
            if net.name1.rfind(value) != -1:
                net.filter = True
            else:
                net.filter = False
        self.UpadateClassTable(self.netpads, True)
    
    def OnRenameClass(self, event):
        self.logger.info('OnRenameClass')

    def OnRemoveClass(self, event):
        self.logger.info('OnRemoveClass')

    def OnUpdateClass(self, event):
        name = self.classPanel.GetChoiceClassValue()
        start = self.classPanel.GetReferenceFromValue()
        end = self.classPanel.GetReferenceToValue()
        netname = NetClass(name, start, end)
        netname.nets = self.netpads
        self.model.classes.append(netname)
    
    def UpadateClassTable(self, nets, filter):
        self.classPanel.dataViewClass.DeleteAllItems()
        if filter == True:
            for index, item in enumerate(nets, start=1):
                if item.filter == True:
                    self.classPanel.dataViewClass.AppendItem([str(index), False, item.name1, item.code1, item.pad1, item.pad2])
        else:
            for index, item in enumerate(nets, start=1):
                self.classPanel.dataViewClass.AppendItem([str(index), False, item.name1, item.code1, item.pad1, item.pad2])

    def TableClassOnLeftDClick(self, event):
        row = event.GetEventObject().GetSelectedRow()
        name = event.GetEventObject().GetTextValue(row, 2)
        code = event.GetEventObject().GetTextValue(row, 3)
        self.classPanel.textNet.SetLabel(name)
        for net in self.netpads:
            if code == net.code1:
                self.temp.set(row, name, code, net.pad1, net.pad2, net.ipad1, net.ipad2)
                self.classPanel.choicePinStart.Clear()
                self.classPanel.choicePinStart.Append(net.pad1s)
                self.classPanel.choicePinStart.SetSelection(net.ipad1)
                self.classPanel.choicePinEnd.Clear()
                self.classPanel.choicePinEnd.Append(net.pad2s)
                self.classPanel.choicePinEnd.SetSelection(net.ipad2)
    
    def OnChoiceReferenceFrom(self, event):
        self.logger.info('OnChoiceReferenceFrom')

    def OnChoiceReferenceTo(self, event):
        self.logger.info('OnChoiceReferenceTo')
    
    def OnChoiceReferenceStart(self, event):
        ind = event.GetEventObject().GetSelection()
        pad = str(event.GetEventObject().GetString(ind))
        self.temp.set1(pad, ind)
        self.classPanel.dataViewClass.SetTextValue(pad, self.temp.row, 4)
        for net in self.netpads:
            if self.temp.code == net.code1:
                net.pad1 = pad
                net.ipad1 = ind

    def OnChoiceReferenceEnd(self, event):
        ind = event.GetEventObject().GetSelection()
        pad = str(event.GetEventObject().GetString(ind))
        self.temp.set2(pad, ind)
        self.classPanel.dataViewClass.SetTextValue(pad, self.temp.row, 5)
        for net in self.netpads:
            if self.temp.code == net.code1:
                net.pad2 = pad
                net.ipad2 = ind