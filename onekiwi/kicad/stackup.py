import json
from .board import *

class Stackup:
    def __init__(self, name, thickness):
        self.name = name
        self.thickness = thickness

def get_layer_stackup():
    board = get_board()
    path = get_pcb_path()
    job_file = os.path.join(path, "jobfile.json")
    pcbnew.GERBER_JOBFILE_WRITER(board).CreateJobFile(job_file)
    pcbnew.GERBER_JOBFILE_WRITER(board).WriteJSONJobFile(job_file)

    # Opening JSON file
    f = open(job_file)
  
    # returns JSON object as 
    # a dictionaryget layge
    data = json.load(f)
  
    # Iterating through the json
    stackups = []
    for obj in data['MaterialStackup']:
        if obj['Type'] == 'Copper' or obj['Type'] == 'Dielectric':
            stackups.append(Stackup(obj['Name'], obj['Thickness']))
    
    # Closing file
    f.close()

    return stackups

def get_thickness_stackup():
    board = get_board()
    path = get_pcb_path()
    job_file = os.path.join(path, "jobfile.json")
    pcbnew.GERBER_JOBFILE_WRITER(board).CreateJobFile(job_file)
    pcbnew.GERBER_JOBFILE_WRITER(board).WriteJSONJobFile(job_file)

    # Opening JSON file
    f = open(job_file)
  
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
  
    # Iterating through the json
    stackups = []
    for obj in data['MaterialStackup']:
        if obj['Type'] == 'Copper' or obj['Type'] == 'Dielectric':
            stackups.append(obj['Thickness'])
    
    # Closing file
    f.close()
    os.remove(job_file)

    return stackups