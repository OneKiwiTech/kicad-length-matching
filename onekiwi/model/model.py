import pcbnew
from typing import List

class ExtendedNet:
    def __init__(self):
        self.ref = ''
        self.net1 = ''
        self.net2 = ''
        self.code1 = ''
        self.code2 = ''
        self.ref1_start = ''
        self.ref1_end = ''
        self.pad1_start = ''
        self.pad1_end = ''
        self.ref2_start = ''
        self.ref2_end = ''
        self.pad2_start = ''
        self.pad2_end = ''
        
class DataNet:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.ref_start = ''
        self.ref_end = ''
        self.pad_start = ''
        self.pad_end = ''

class ClassName:
    def __init__(self, name):
        self.name = name
        self.ref_start = ''
        self.ref_end = ''
        self.clases:List[DataNet] = []

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        self.clases:List[str] = []
    