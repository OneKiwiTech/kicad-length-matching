import wx
from frame import MainFrame

if __name__ == '__main__':
    filters = ['R1', 'R11', 'R21', 'R31', 'U11', 'U1']
    app = wx.App(False)
    frame = MainFrame(None)
    frame.comboFilter.AddList(filters)
    frame.Show()
    app.MainLoop()