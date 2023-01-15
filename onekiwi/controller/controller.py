from ..model.model import Model
from ..view.view import *
from .logtext import LogText
import pcbnew
import sys
import logging
import logging.config
import wx

class Controller:
    def __init__(self, board):
        self.view = LengthMatchingView()
        self.classPanel = ClassPanelView(self.view.notebook)
        self.xNetPanel = ExtendedNetPanelView(self.view.notebook)
        self.settingPanel = SettingPanelView(self.view.notebook)
        self.displayPanel = DisplayPanelView(self.view.notebook)
        self.infoPanel = InfoPanelView(self.view.notebook)
        
        self.view.notebook.AddPage(self.classPanel, "Class")
        self.view.notebook.AddPage(self.xNetPanel, "Extended Net")
        self.view.notebook.AddPage(self.settingPanel, "Setting")
        self.view.notebook.AddPage(self.displayPanel, "Display")
        self.view.notebook.AddPage(self.infoPanel, "Net Info")

        self.board = board
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
        references = []
        footprints = self.board.GetFootprints()
        for footprint in footprints:
            ref = str(footprint.GetReference())
            references.append(ref)
        references.sort()
        self.classPanel.UpdateFiltterFrom(references)
        self.classPanel.UpdateFiltterTo(references)

    def OnLoadSetting(self, event):
        self.logger.info('OnLoadSetting')

    def OnSaveSetting(self, event):
        self.logger.info('OnSaveSetting')

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

    def OnAddClass(self, event):
        name = self.classPanel.GetEditClassName()
        if name != '':
            if name not in self.model.clases:
                self.model.clases.append(name)
                self.classPanel.SetEditClassName('')
                self.classPanel.UpdateChoiceClass(self.model.clases)
            else:
                self.logger.info('Name already exists!')
        else:
            self.logger.info('Please enter name!')
    
    def OnUpdateNet(self, event):
        start = self.classPanel.GetFiltterFromValue()
        end = self.classPanel.GetFiltterToValue()
        self.logger.info('Start %s, End %s', start, end)

        ref_start = self.board.FindFootprintByReference(start)
        ref_end = self.board.FindFootprintByReference(end)
        netcodes = []
        for pad in ref_start.Pads():
            netpad = str(pad.GetNetname())
            padcode = self.board.GetNetcodeFromNetname(netpad)
            netcodes.append(padcode)
        for pad in ref_end.Pads():
            netpad = str(pad.GetNetname())
            padcode = self.board.GetNetcodeFromNetname(netpad)
            if padcode in netcodes and netpad != 'GND':
                self.logger.info('Net %s', netpad)
