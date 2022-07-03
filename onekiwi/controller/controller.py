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

        #self.DisplayStatus(self.model.status.get())
        #self.model.status.addCallback(self.DisplayStatus)
        # Connect Events
        self.panel1.buttonUpdate.Bind(wx.EVT_BUTTON, self.OnUpdateClick)
        self.panel1.buttonLoad.Bind(wx.EVT_BUTTON, self.OnLoadClick)
        self.panel1.comboClass.Bind(wx.EVT_COMBOBOX, self.OnClassChange)

    def Show(self):
        self.view.ShowModal()

    # Virtual event handlers, override them in your derived class
    def OnUpdateClick(self, event):
        track, via, count = self.model.get_track_length()
        self.panel1.UpadateLength(track, via, count)

    def OnLoadClick(self, event):
        #self.model.set_status1('Loading')
        self.model.init_data()
        self.panel1.UpdateClass(self.model.classes)

    def OnClassChange(self, event):
        net_class = event.GetEventObject().GetValue() 
        for netclass in self.model.netclasses:
            if net_class == netclass.name:
                self.view.SetText(netclass.name)
                self.panel1.UpadateNets(netclass.nets)
