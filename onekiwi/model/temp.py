
class TempNetClass:
    def __init__(self):
        self.row = 0
        self.name = ''
        self.code = ''
        self.pad1 = ''
        self.pad2 = ''
        self.ind1 = 0
        self.ind2 = 0
    
    def set(self, row, name, code, pad1, pad2, ind1, ind2):
        self.row = row
        self.name = name
        self.code = code
        self.pad1 = pad1
        self.pad2 = pad2
        self.ind1 = ind1
        self.ind2 = ind2
    
    def set1(self, pad1, ind1):
        self.pad1 = pad1
        self.ind1 = ind1
    
    def set2(self, pad2, ind2):
        self.pad2 = pad2
        self.ind2 = ind2