from .dialog import *
from ..version import version

class LengthMatchingView(LengthMatchingDialog):
    def __init__(self):
        LengthMatchingDialog.__init__(self, None)
        self.SetTitle('Length Matching %s' % version)

    def SetText(self, status):
        self.textStatus.LabelText = status

class NetPanelView(NetPanel):
    def __init__( self, parent):
        NetPanel.__init__(self, parent)

    def UpdateCombobox(self, classes):
        self.comboClass.Clear()
        self.comboClass.Append(classes)
        self.comboClass.SetSelection(0)

    def GetComboboxValue(self):
        return self.comboClass.GetValue()

    def GetComboboxSelection(self):
        return self.comboClass.GetSelection()

    def UpadateTable(self, nets, unit):
        scale = 1.0
        if unit == 'in':
            scale = 10/254
        elif unit == 'mil':
            scale = 10000/254
        rows = self.gridNet.GetNumberRows()
        self.gridNet.DeleteRows(0, rows)
        self.gridNet.AppendRows(len(nets))
        #self.gridNet.SetCornerLabelValue('Net Code')
        for row, net in enumerate(nets):
            self.gridNet.SetCellValue(row, 0, net['name'])
            pins = [item['pin'] for item in net['pads']]
            pin1 = net['pin1']
            pin2 = net['pin2']
            choice_editor = wx.grid.GridCellChoiceEditor(pins, True)
            self.gridNet.SetCellEditor(row, 1, choice_editor)
            self.gridNet.SetCellEditor(row, 2, choice_editor)
            self.gridNet.SetCellValue(row, 1, pin1)
            self.gridNet.SetCellValue(row, 2, pin2)
            vialength = round(net['vialength']*scale, 4)
            tracklength = round(net['tracklength']*scale, 4)
            totallength = round(net['totallength']*scale, 4)
            self.gridNet.SetCellValue(row, 3, str(net['viacount']))
            self.gridNet.SetCellValue(row, 4, str(vialength))
            self.gridNet.SetCellValue(row, 5, str(tracklength))
            self.gridNet.SetCellValue(row, 6, str(totallength))
            self.gridNet.SetRowLabelValue( row, str(net['code']))
            

class InfoPanelView(InfoPanel):
    def __init__( self, parent):
        InfoPanel.__init__(self, parent)

class xNetPanelView(xNetPanel):
    def __init__( self, parent):
        xNetPanel.__init__(self, parent)