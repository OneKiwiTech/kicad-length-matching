import pcbnew
import os

DEBUG_GUI = 0

def get_board():
    filename = '/home/vanson/Downloads/radio-4g-imx-rt1052-v1.0/iMXRT1052_Thatico.kicad_pcb'
    board = None
    if DEBUG_GUI == 1:
        board = pcbnew.LoadBoard(filename)
    else:
        board = pcbnew.GetBoard()
    return board

def get_pcb_name():
    file_name = get_board().GetFileName()
    base = os.path.basename(file_name)
    name = os.path.splitext(base)[0]
    return name

def get_pcb_full_name():
    file_name = get_board().GetFileName()
    name = os.path.basename(file_name)
    return name

def get_pcb_path():
    file_name = get_board().GetFileName()
    path = os.path.dirname(file_name)
    return path
    
def get_current_unit():
    return pcbnew.GetUserUnits()

def get_plugin_path():
    # log_file = os.path.join(os.path.dirname(__file__), "..", "lengthmatching.log")
    current_path = os.path.dirname(__file__)
    path1 = os.path.dirname(current_path)
    path = os.path.dirname(path1)
    return path
