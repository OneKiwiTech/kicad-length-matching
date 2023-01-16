
class PadInfo:
    def __init__(self, name, code, refs, pins, refe, pine):
        self.name = name
        self.code = code
        self.refs = refs
        self.pins = pins
        self.refe = refe
        self.pine = pine
        self.show = refs + '.' + pins + ' - ' + refe + '.' + pine + ': ' + name