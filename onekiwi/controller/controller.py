from ..model.model import Model
from ..view.view import LengthMatchingView
from .logtext import LogText
import pcbnew
import wx
import sys
import logging
import logging.config

# https://github.com/weirdgyn/viastitching/blob/master/viastitching_dialog.py
class Controller:
    def __init__(self, board):
        self.view = LengthMatchingView()
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
    
    def FillupArea(self):
        '''Fills selected area with vias.'''        

        drillsize = self.model.vias[0].m_Drill
        viasize = self.model.vias[0].m_Diameter
        step_x = 2000000
        step_y = 2000000
        #clearance = self.FromUserUnit(float(self.m_txtClearance.GetValue()))

        index = self.view.choiceArea.GetSelection()
        area = self.model.areas[index]

        bbox = area.GetBoundingBox()
        top = bbox.GetTop()
        bottom = bbox.GetBottom()
        right = bbox.GetRight()
        left = bbox.GetLeft()
        
        #index = self.view.choiceArea.GetSelection()
        #area = self.model.areas[index]
        netname = str(area.GetNetname())
        netcode = self.board.GetNetcodeFromNetname(netname)
        #commit = pcbnew.COMMIT()
        viacount = 0
        x = left

        #Cycle trough area bounding box checking and implanting vias
        layer = area.GetLayer()
        while x <= right:
            y = top
            while y <= bottom:
                p = pcbnew.wxPoint(x,y)
                if area.HitTestFilledArea(layer, p, 0):
                    via = pcbnew.PCB_VIA(self.board)
                    via.SetPosition(p)
                    via.SetLayer(layer)
                    via.SetNetCode(netcode)
                    via.SetDrill(drillsize)
                    via.SetWidth(viasize)
                    #via.SetTimeStamp(__timecode__)
                    self.board.Add(via)
                    viacount +=1
                    """
                    if not self.CheckOverlap(via):
                        #Check clearance only if clearance value differs from 0 (disabled)
                        if (clearance == 0) or self.CheckClearance(p, self.area, clearance):
                            self.board.Add(via)
                            #commit.Add(via)
                            viacount +=1
                            """
                y += step_y
            x += step_x

        pcbnew.Refresh()