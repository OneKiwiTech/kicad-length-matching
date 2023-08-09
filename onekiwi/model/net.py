
class NetData:
    def __init__(self, nettype, name1, code1, ref1, pad1, name2, code2, ref2, pad2, xref, xpad1, xpad2):
        self.type = nettype
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