import pcbnew
import json
from ..kicad.board import *
from typing import List
from .net import NetData

class NetClass:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.nets:List[NetData] = []

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        self.classes:List[NetClass] = []
        self.netclasses = {}

    def export_to_json(self):
        path = get_pcb_path(self.board)
        name = get_pcb_name(self.board) + '_length-matching.json'
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
        path = get_pcb_path(self.board)
        name = get_pcb_name(self.board) + '_length-matching.json'
        json_file = os.path.join(path, name)
        # Check If File Exists
        if os.path.exists(json_file):
            with open(json_file) as json_file:
                data = json.load(json_file)
                status = True
        return status, data
    
    def get_json_data(self):
        status, data = self.read_json()
        if status == True:
            self.classes.clear()
            for jsonclass in data['netclasses']:
                netclass = NetClass(jsonclass['name'], jsonclass['start'], jsonclass['end'])
                for jsonnet in jsonclass['nets']:
                    net = NetData(jsonnet['type'], jsonnet['name1'], jsonnet['code1'], jsonnet['ref1'], jsonnet['pad1'], 
                        jsonnet['name2'], jsonnet['code2'], jsonnet['ref2'], jsonnet['pad2'],
                        jsonnet['xref'], jsonnet['xpad1'], jsonnet['xpad2'])
                    for jsonpad1 in jsonnet['pad1s']:
                        net.pad1s.append(jsonpad1)
                    for jsonpad2 in jsonnet['pad2s']:
                        net.pad2s.append(jsonpad2)
                    netclass.nets.append(net)
                self.classes.append(netclass)
    
    def save_setting(self):
        self.netclasses["netclasses"] = []
        for netclass in self.classes:
            item = {"name": netclass.name, "start": netclass.start, "end": netclass.end, "nets": []}
            for net in netclass.nets:
                if net.selected == True:
                    netdata = {"type": net.type, "name1": net.name1, "code1": net.code1, "ref1": net.ref1, "pad1": net.pad1,
                                "name2": net.name2, "code2": net.code2, "ref2": net.ref2, "pad2": net.pad2,
                                "xref": net.xref, "xpad1": net.xpad1, "xpad2": net.xpad2, "pad1s": [], "pad2s": []}
                    for pad1 in net.pad1s:
                        netdata["pad1s"].append(pad1)
                    for pad2 in net.pad2s:
                        netdata["pad2s"].append(pad2)
                    item["nets"].append(netdata)
            self.netclasses['netclasses'].append(item)

        path = self.export_to_json()
        display = 'Save Setting to file:' + path
        self.logger.info(display)