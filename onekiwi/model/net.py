
class NetData:
    def __init__(self, nettype, name, code, ref1, pad1, ref2, pad2):
        self.type = nettype
        self.name1 = name
        self.name2 = ''
        self.code1 = code
        self.code2 = ''
        self.ref1 = ref1
        self.pad1 = pad1
        self.ref2 = ref2
        self.pad2 = pad2
        self.xref = ''
        self.xpad1 = ''
        self.xpad2 = ''
        self.pad1s = []
        self.pad2s = []
        self.xpad1s = []
        self.xpad2s = []