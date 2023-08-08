import pcbnew
import json
from ..kicad.board import *
from typing import List
from .net import NetData

class NetClass:
    def __init__(self, name, start, end):
        self.name = name
        self.start = ''
        self.end = ''
        self.nets:List[NetData] = []

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        self.classes:List[NetClass] = []
        self.netclasses = {}

    def export_to_json(self):
        path = get_pcb_path()
        name = get_pcb_name() + '_length-matching.json'
        json_file = os.path.join(path, name)
        # Serializing json 
        results = json.dumps(self.netclasses, indent = 4)

        # Writing to sample.json
        with open(json_file, "w") as outfile:
            outfile.write(results)
        return json_file
    
    def read_json(self):
        data = {}
        status = False
        path = get_pcb_path()
        name = get_pcb_name() + '_length-matching.json'
        json_file = os.path.join(path, name)
        # Check If File Exists
        if os.path.exists(json_file):
            with open(json_file) as json_file:
                data = json.load(json_file)
                status = True
        return status, data
    