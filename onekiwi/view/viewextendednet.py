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
    
    def GetChoiceReferenceValue(self):
        ind = self.choiceReference.GetSelection()
        return str(self.choiceReference.GetString(ind))
