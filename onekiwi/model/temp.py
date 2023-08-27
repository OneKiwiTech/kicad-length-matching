
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

class TempxNet:
    def __init__(self, name, code, ref1, pad1, ref2, pad2):
        self.name = name
        self.code = code
        self.ref1 = ref1
        self.ref2 = ref2
        self.pad1s = [pad1]
        self.pad2s = [pad2]
        self.dis1s = [ref1+'.'+pad1]
        self.dis2s = [ref2+'.'+pad2]
    
    def add_dis1(self, ref1, pad1):
        self.pad1s.append(pad1)
        self.dis1s.append(ref1+'.'+pad1)
    
    def add_dis2(self, ref2, pad2):
        self.pad2s.append(pad2)
        self.dis2s.append(ref2+'.'+pad2)