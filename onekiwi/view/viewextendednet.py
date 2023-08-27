from .panelextendednet import ExtendedNetPanel

class ExtendedNetPanelView(ExtendedNetPanel):
    def __init__( self, parent):
        ExtendedNetPanel.__init__(self, parent)

    def UpdateClassName(self, classes):
        self.choiceClass.Clear()
        self.choiceClass.Append(classes)
        self.choiceClass.SetSelection(0)

    def UpdateReference(self, classes):
        self.choiceReference.Clear()
        self.choiceReference.Append(classes)
        self.choiceReference.SetSelection(0)

    def UpdateNetNameStart(self, classes):
        self.choiceNetName1.Clear()
        self.choiceNetName1.Append(classes)
        self.choiceNetName1.SetSelection(0)
    
    def UpdateNetPad1Start(self, classes):
        self.choiceNetStart1.Clear()
        self.choiceNetStart1.Append(classes)
        self.choiceNetStart1.SetSelection(0)
    
    def UpdateNetPad1End(self, classes):
        self.choiceNetEnd1.Clear()
        self.choiceNetEnd1.Append(classes)
        self.choiceNetEnd1.SetSelection(0)

    def UpdateNetNameEnd(self, classes):
        self.choiceNetName2.Clear()
        self.choiceNetName2.Append(classes)
        self.choiceNetName2.SetSelection(0)

    def UpdateNetPad2Start(self, classes):
        self.choiceNetStart2.Clear()
        self.choiceNetStart2.Append(classes)
        self.choiceNetStart2.SetSelection(0)
    
    def UpdateNetPad2End(self, classes):
        self.choiceNetEnd2.Clear()
        self.choiceNetEnd2.Append(classes)
        self.choiceNetEnd2.SetSelection(0)

    def GetChoiceReferenceValue(self):
        ind = self.choiceReference.GetSelection()
        return str(self.choiceReference.GetString(ind))
