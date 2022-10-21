from ..model.model import Model
from ..view.view import *
from .logtext import LogText
import pcbnew
import sys
import logging
import logging.config

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