import pcbnew
import os

def get_board():
    board = pcbnew.GetBoard()
    return board

def get_pcb_name():
    file_name = pcbnew.GetBoard().GetFileName()
    base = os.path.basename(file_name)
    name = os.path.splitext(base)[0]
    return name

def get_pcb_full_name():
    file_name = pcbnew.GetBoard().GetFileName()
    name = os.path.basename(file_name)
    return name

def get_pcb_path():
    file_name = pcbnew.GetBoard().GetFileName()
    path = os.path.dirname(file_name)
    return path

def get_plugin_path():
    # log_file = os.path.join(os.path.dirname(__file__), "..", "lengthmatching.log")
    current_path = os.path.dirname(__file__)
    path1 = os.path.dirname(current_path)
    path = os.path.dirname(path1)
    return path
