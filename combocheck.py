import wx

class CheckComboPopup(wx.ComboPopup):
    def __init__(self):
        wx.ComboPopup.__init__(self)
        self.sampleList = ['zero', 'one']
        self.curitem = -1
    
    def Create(self, parent):
        self.clb = wx.CheckListBox(parent, -1, choices = self.sampleList)
        self.clb.Bind(wx.EVT_MOTION, self.OnMotion)
        self.clb.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        return True
    
    def GetControl(self):
        return self.clb
    
    def OnMotion(self, evt):
        item = self.clb.HitTest(evt.GetPosition())
        if item >= 0:
            self.clb.SetSelection(item)
            self.curitem = item

    def OnLeftDown(self, evt):
        checked = self.clb.IsChecked(self.curitem)
        self.clb.Check(self.curitem, not checked)
        self.Dismiss()
    
    # Called just prior to displaying the popup, you can use it to
    # 'select' the current item.
    def SetStringValue(self, val):
        # this part is unnecessary since the selection has
        # been set in OnMotion
        if self.curitem >= 0:
            self.clb.SetSelection(self.curitem)

    # Return a string representation of the selected item(s)
    def GetStringValue(self):
        return ','.join(self.clb.GetCheckedStrings())

    # Called immediately after the popup is shown
    def OnPopup(self):
        wx.ComboPopup.OnPopup(self)

    # Called when popup is dismissed
    def OnDismiss(self):
        wx.ComboPopup.OnDismiss(self)

class CheckCombo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        cc = wx.ComboCtrl(self, size = (250, -1))
        tcp = CheckComboPopup()
        cc.SetPopupControl(tcp)

        box = wx.BoxSizer()
        box.Add(cc, 1, wx.EXPAND|wx.ALL, 20)
        self.SetSizer(box)