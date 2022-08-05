from ..model.model import Model
from ..view.view import *
import json
import logging

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = LengthMatchingView()
        self.panel1 = NetPanelView(self.view.notebook)
        self.panel2 = xNetPanelView(self.view.notebook)
        #self.panel3 = InfoPanelView(self.view.notebook)
        
        self.view.notebook.AddPage(self.panel1, "Display")
        self.view.notebook.AddPage(self.panel2, "xNet")
        #self.view.notebook.AddPage(self.panel3, "Net Info")

        # Connect Events
        self.view.Bind(wx.EVT_CLOSE, self.OnDialogClose)
        self.panel1.buttonUpdate.Bind(wx.EVT_BUTTON, self.OnUpdateClick)
        self.panel1.buttonSave.Bind(wx.EVT_BUTTON, self.OnSaveClick)
        self.panel1.buttonLoad.Bind(wx.EVT_BUTTON, self.OnLoadClick)
        self.panel1.comboClass.Bind(wx.EVT_COMBOBOX, self.OnClassChange)
        self.panel1.gridNet.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.OnGirdCellChange)
        self.panel1.gridNet.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.OnGridLabelLeftDClick)
        self.panel1.buttonClearHighlight.Bind(wx.EVT_BUTTON, self.OnClearHighlightClick)

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    # Event handlers
    def OnLoadClick(self, event):
        msg = self.model.compare_data()
        if msg != None:
            self.view.SetText('Error: Net %s have 0 or 1 pad connected' %msg)
        else:
            self.model.get_track_length()
            self.panel1.UpdateCombobox(self.model.classes)
            nets = self.model.nameclasses["classes"][0]['nets']
            unit = self.model.get_unit()
            self.panel1.UpadateTable(nets, unit)
            self.view.SetText('Load Setting: Done')
    
    def OnSaveClick(self, event):
        if self.model.statusinit == True:
            path = self.model.export_to_json()
            display = 'Save Setting to file:' + path
            self.view.SetText(display)
        else:
            self.view.SetText('Save Setting: Please press button Load Setting')

    def OnUpdateClick(self, event):
        if self.model.statusinit == True:
            self.model.get_track_length()
            index = self.panel1.GetComboboxSelection()
            nets = self.model.nameclasses["classes"][index]['nets']
            unit = self.model.get_unit()
            self.panel1.UpadateTable(nets, unit)
            self.view.SetText('Update Track: Done')
        else:
            self.view.SetText('Update Track: Please press button Load Setting')

    def OnClassChange(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetValue()
        value = 'Selected: ' + value
        self.view.SetText(value)
        nets = self.model.nameclasses["classes"][index]['nets']
        unit = self.model.get_unit()
        self.panel1.UpadateTable(nets, unit)
    
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
                        net['pin1'] = pad['pin']
                        status = 'Pad Start: change to ' + value
                        self.view.SetText(status)
                    else:
                        net['pad2'] = pad['pad']
                        net['reference2'] = pad['reference']
                        net['pin2'] = pad['pin']
                        status = 'Pad End: change to ' + value
                        self.view.SetText(status)

    def OnGridLabelLeftDClick(self, event):
        class_id = self.panel1.GetComboboxSelection()
        row = event.GetRow()
        col = event.GetCol() # col = -1
        value = str(row) + ' ' + str(col)
        self.model.highlight_net(class_id, row)
        self.view.SetText(value)

    def OnClearHighlightClick(self, event):
        self.model.clear_highlight_net()

    def OnDialogClose(self, event):
        self.model.clear_highlight_net()
        self.Close()
    