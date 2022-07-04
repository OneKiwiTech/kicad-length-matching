from pyexpat import model
from ..model.model import Model
from ..view.view import *

class Controller:
    def __init__(self, parent):
        self.model = Model()
        self.view = DialogMain(parent)
        self.panel1 = NetPanel(self.view.notebook)
        self.panel2 = xNetPanel(self.view.notebook)
        self.view.notebook.AddPage(self.panel1, "Display")
        self.view.notebook.AddPage(self.panel2, "xNet")

        # Connect Events
        self.panel1.buttonUpdate.Bind(wx.EVT_BUTTON, self.OnUpdateClick)
        self.panel1.buttonSave.Bind(wx.EVT_BUTTON, self.OnSaveClick)
        self.panel1.buttonLoad.Bind(wx.EVT_BUTTON, self.OnLoadClick)
        self.panel1.comboClass.Bind(wx.EVT_COMBOBOX, self.OnClassChange)
        self.panel1.gridNet.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.OnGirdCellChange)

    def Show(self):
        self.view.ShowModal()

    # Virtual event handlers, override them in your derived class

    def OnLoadClick(self, event):
        self.model.init_data2()
        self.model.get_track_length2()
        #self.model.init_data()
        #self.model.get_track_length()
        #self.panel1.UpdateClass(self.model.classes)
        #self.panel1.UpadateTable(self.model.netclasses[0].nets)
    
    def OnSaveClick(self, event):
        self.model.to_json()

    def OnUpdateClick(self, event):
        self.model.get_track_length()
        self.panel1.UpadateLength(self.model.netclasses)

    def OnClassChange(self, event):
        net_class = event.GetEventObject().GetValue() 
        for netclass in self.model.netclasses:
            if net_class == netclass.name:
                self.view.SetText(netclass.name)
                self.panel1.UpadateTable(netclass.nets)
    
    def OnGirdCellChange(self, event):
        row = event.GetRow()
        col = event.GetCol()
        value = str(self.panel1.gridNet.GetCellValue(row, col))
        status =  str(row) + ' '  + str(col)
        value = value + ' ' + status
        self.view.SetText(value)
