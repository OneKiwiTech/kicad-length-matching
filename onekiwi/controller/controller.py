from ..model.model import Model
from ..model.pad import PadInfo
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
        self.updatenets = []
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
        self.classPanel.buttonAddAll.Bind(wx.EVT_BUTTON, self.OnAddAll)
        self.classPanel.buttonAddSelected.Bind(wx.EVT_BUTTON, self.OnAddSelected)
        self.classPanel.buttonRemoveSelected.Bind(wx.EVT_BUTTON, self.OnRemoveSelected)
        self.classPanel.buttonRemoveAll.Bind(wx.EVT_BUTTON, self.OnRemoveAll)
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
        self.logger.info('OnLoadSetting')

    def OnSaveSetting(self, event):
        self.logger.info('OnSaveSetting')
        self.model.netclasses["netclasses"] = []
        for item in self.model.classes:
            print(item)
            #net = {"name": item, "nets":[]}
            #self.model.netclasses['netclasses'].append(net)

        path = get_pcb_path(self.board)
        name = get_pcb_name(self.board) + '_length-matching.json'
        json_file = os.path.join(path, name)
        # Serializing json 
        results = json.dumps(self.model.netclasses, indent = 4)

        # Writing to sample.json
        with open(json_file, "w") as outfile:
            outfile.write(results)
        return json_file

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
            if name not in self.model.classes:
                self.model.classes.append(name)
                self.classPanel.SetEditClassName('')
                self.classPanel.UpdateChoiceClass(self.model.classes)
            else:
                self.logger.info('Name already exists!')
        else:
            self.logger.info('Please enter name!')
    
    def OnUpdateNet(self, event):
        if len(self.model.classes) < 1:
            self.logger.info('Please create class name')
            return
        self.updatenets.clear()
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
                        net = NetData('net', name2, code2, ref1, pin1, ref2, pin2)
                        self.netpads.append(net)

        self.classPanel.ClearListNet()
        self.netpads.sort(key=lambda x: x.name1)
        for data in self.netpads:
            self.updatenets.append(data.name1)
        self.classPanel.UpdateListNet(self.updatenets)
    
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
        nets = []
        for item in self.updatenets:
            if item.rfind(value) != -1:
                nets.append(item)
        self.classPanel.ClearListNet()
        self.classPanel.UpdateListNet(nets)
        
    def OnAddAll(self, event):
        self.classPanel.ClearListNet()
        self.classPanel.UpdateListNetClass(self.netpads)

    def OnAddSelected(self, event):
        names = []
        items = self.classPanel.listNet.GetSelections()
        for index in items:
            v = self.classPanel.listNet.GetString(index)
            names.append(v)
        self.classPanel.UpdateListNetClass(names)
        items.sort(reverse=True)
        for i in items:
            self.classPanel.DeleteItemListNet(i)

    def OnRemoveSelected(self, event):
        names = []
        items = self.classPanel.listNetClass.GetSelections()
        for index in items:
            v = self.classPanel.listNetClass.GetString(index)
            names.append(v)
        self.classPanel.UpdateListNet(names)
        items.sort(reverse=True)
        for i in items:
            self.classPanel.DeleteItemListNetClass(i)

    def OnRemoveAll(self, event):
        self.classPanel.ClearListNetClass()
        self.classPanel.UpdateListNet(self.netpads)
    
    def OnRenameClass(self, event):
        self.logger.info('OnRenameClass')

    def OnRemoveClass(self, event):
        self.logger.info('OnRemoveClass')

    def OnUpdateClass(self, event):
        name = self.classPanel.GetChoiceClassValue()
        start = self.classPanel.GetReferenceFromValue()
        end = self.classPanel.GetReferenceToValue()
        netname = NetClass(name, start, end)
        #netname.nets = self.netpads
        self.model.classes.append(netname)