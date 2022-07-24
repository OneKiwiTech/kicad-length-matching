import wx
from frame import ComboFrame

if __name__ == '__main__':
    app = wx.App(False)
    frm = ComboFrame(None)
    frm.Show()
    app.MainLoop()