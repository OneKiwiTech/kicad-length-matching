import sys
import wx
import pcbnew
from onekiwi.controller.controller import Controller

filename = ''
print('filename: ' + str(sys.argv[1]))
filename = str(sys.argv[1])

class SimplePluginApp(wx.App):
    def OnInit(self):
        try:
            board = pcbnew.LoadBoard(filename)
            controller = Controller(board)
            controller.Show()
            return True
        except OSError:
            print("OSError: Unable to open file for reading.")
            return 0

def main():
    app = SimplePluginApp()
    app.MainLoop()

    print("Done")

if __name__ == "__main__":
    main()

# python3 dialog.py /home/onekiwi/kicad/bms-three-cell/bms-three-cell.kicad_pcb