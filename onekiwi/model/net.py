
class NetData:
    def __init__(self, name, code, ref1, pad1, ref2, pad2):
        self.name = name
        self.code = code
        self.ref1 = ref1
        self.pad1 = pad1
        self.ref2 = ref2
        self.pad2 = pad2
        self.pad1s = []
        self.pad2s = []
        self.selected = False
        self.filter = False
        self.ipad1 = 0 #index
        self.ipad2 = 0 #index

class NetExtendedData:
    def __init__(self, name1, code1, ref1, pad1, name2, code2, ref2, pad2, xref, xpad1, xpad2):
        self.name1 = name1
        self.name2 = name2
        self.code1 = code1
        self.code2 = code2
        self.ref1 = ref1
        self.pad1 = pad1
        self.ref2 = ref2
        self.pad2 = pad2
        self.xref = xref
        self.xpad1 = xpad1
        self.xpad2 = xpad2
        self.pad1s = []
        self.pad2s = []
        self.xpad1s = []
        self.xpad2s = []
        self.selected = False
        self.filter = False
        self.ipad1 = 0
        self.ipad2 = 0
        self.ixpad1 = 0
        self.ixpad2 = 0