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

    # Event handlers
    def OnLoadClick(self, event):
        self.model.init_data()
        self.model.get_track_length()
        self.panel1.UpdateCombobox(self.model.classes)
        nets = self.model.nameclasses["classes"][0]['nets']
        self.panel1.UpadateTable(nets)
    
    def OnSaveClick(self, event):
        self.model.to_json()

    def OnUpdateClick(self, event):
        self.model.get_track_length()
        index = self.panel1.GetComboboxSelection()
        nets = self.model.nameclasses["classes"][index]['nets']
        self.panel1.UpadateTable(nets)

    def OnClassChange(self, event):
        index = event.GetEventObject().GetSelection()
        nets = self.model.nameclasses["classes"][index]['nets']
        self.panel1.UpadateTable(nets)
    
    def OnGirdCellChange(self, event):
        row = event.GetRow()
        col = event.GetCol()
        value = str(self.panel1.gridNet.GetCellValue(row, col))
        self.view.SetText(value)

        # change pad start or pad end
        if col == 1 or col == 2:
            index = self.panel1.GetComboboxSelection()
            net = self.model.nameclasses["classes"][index]['nets'][row]
            for pad in net['pads']:
                if value == pad['pin']:
                    if col == 1:
                        net['pad1'] = pad['pad']
                        net['reference1'] = pad['reference']
                    else:
                        net['pad2'] = pad['pad']
                        net['reference2'] = pad['reference']
        

            
