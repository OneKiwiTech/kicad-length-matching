import os
import sys
import tempfile
import logging
import wx
import wx.aui
import pcbnew
from wx import FileConfig


from .controller.controller import Controller
from .version import version

class OneKiwiPlugin(pcbnew.ActionPlugin, object):
    config_file = os.path.join(os.path.dirname(__file__), '..', 'config.ini')

    def __init__(self):
        super(OneKiwiPlugin, self).__init__()

        self.InitLogger()
        self.logger = logging.getLogger(__name__)

        self.name = "Length Matching"
        self.category = "Read PCB"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        icon_dir = os.path.dirname(os.path.dirname(__file__))
        self.icon_file_name = os.path.join(icon_dir, 'icon.png')
        self.description = "Track Length Calculator"
        self.config = FileConfig(localFilename=self.config_file)
        
        self._pcbnew_frame = None

        self.kicad_build_version = pcbnew.GetBuildVersion()
        if '5.1' in self.kicad_build_version or '5.0' in self.kicad_build_version:
            # Library location for KiCad 5.1
            self.filepath = os.path.join(tempfile.mkdtemp(), 'onekiwi_labels.pretty', 'label.kicad_mod') 
            try: # Use try/except here because python 2.7 doesn't support exist_ok
                os.makedirs(os.path.dirname(self.filepath))
            except:
                pass

    def Run(self):
        if self._pcbnew_frame is None:
            try:
                self._pcbnew_frame = [x for x in wx.GetTopLevelWindows() if ('pcbnew' in x.GetTitle().lower() and not 'python' in x.GetTitle().lower()) or ('pcb editor' in x.GetTitle().lower())]
                if len(self._pcbnew_frame) == 1:
                    self._pcbnew_frame = self._pcbnew_frame[0]
                else:
                    self._pcbnew_frame = None
            except:
                pass
        
        board = pcbnew.GetBoard()
        pcb_file_name = board.GetFileName()

        if not pcb_file_name:
            wx.MessageBox(
                'Please save the board file before', 
                'Message Box', wx.OK | wx.ICON_WARNING
            )
            return

        controller = Controller(self._pcbnew_frame, version)

        if controller.Show() == wx.ID_OK:
            
            if '5.99' in self.kicad_build_version or '6.0' in self.kicad_build_version:
                if self._pcbnew_frame is not None:
                    # Set focus to main window and attempt to execute a Paste operation
                    self._pcbnew_frame.Raise()
                    wx.Yield()
         
    def InitLogger(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)

        log_file = os.path.join(os.path.dirname(__file__), "..", "onekiwi.log")

        # and to our error file
        handler2 = logging.FileHandler(log_file)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s %(name)s %(lineno)d:%(message)s", datefmt="%m-%d %H:%M:%S"
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)
