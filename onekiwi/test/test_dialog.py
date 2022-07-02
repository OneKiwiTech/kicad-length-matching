from ..controller.controller import Controller
import wx

app = wx.App(False)
controller = Controller(app)
app.MainLoop()

print("Done")
