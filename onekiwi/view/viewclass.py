from .panelclass import ClassPanel

class ClassPanelView(ClassPanel):
    def __init__( self, parent):
        ClassPanel.__init__(self, parent)

    def GetEditClassName(self):
        return self.editClass.GetValue()
    
    def SetEditClassName(self, text):
        self.editClass.SetValue(text)

    def GetEditRename(self):
        return self.editRename.GetValue()
    
    def SetEditRename(self, text):
        self.editRename.SetValue(text)

    def AddItemChoiceClass(self, item):
        self.choiceClass.Append(item)
    
    def UpdateChoiceClass(self, classes):
        self.choiceClass.Clear()
        self.choiceClass.Append(classes)
        self.choiceClass.SetSelection(0)

    def GetChoiceClassValue(self):
        ind = self.choiceClass.GetSelection()
        return str(self.choiceClass.GetString(ind))
    
    def SetChoiceClassValue(self, text):
        ind = self.choiceClass.GetSelection()
        self.choiceClass.SetString(ind, text)

    def GetChoiceClassSelection(self):
        return self.choiceClass.GetSelection()

    def UpdateReferenceFrom(self, classes):
        self.choiceReferenceFrom.Clear()
        self.choiceReferenceFrom.Append(classes)
        self.choiceReferenceFrom.SetSelection(0)

    def GetReferenceFromValue(self):
        ind = self.choiceReferenceFrom.GetSelection()
        return str(self.choiceReferenceFrom.GetString(ind))
    
    def UpdateReferenceTo(self, classes):
        self.choiceReferenceTo.Clear()
        self.choiceReferenceTo.Append(classes)
        self.choiceReferenceTo.SetSelection(0)
    
    def GetReferenceToValue(self):
        ind = self.choiceReferenceTo.GetSelection()
        return str(self.choiceReferenceTo.GetString(ind))