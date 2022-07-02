from pyexpat import model
from ..model.model import Model
from ..view.view import *

class Controller:
    def __init__(self, parent):
        self.model = Model()
        self.view = DialogMain(parent)
        self.panel1 = NetPanel(self.view.notebook)
        self.panel2 = xNetPanel(self.view.notebook)
        self.view.notebook.AddPage(self.panel1, "Panel1")
        self.view.notebook.AddPage(self.panel2, "Panel2")

        # Connect Events
        self.panel1.buttonLoad.Bind( wx.EVT_BUTTON, self.OnLoadClick )

    def Show(self):
        self.view.ShowModal()

    # Virtual event handlers, override them in your derived class
    def OnLoadClick( self, event ):
        self.view.textStatus.LabelText = "Loading"
        self.model.init_data()
        self.panel1.comboClass.Append(self.model.classes)
