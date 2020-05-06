from helper import little_endian_to_int


class Script:
    def parse(self):
        pass


class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        if script_sig is None:
            script_sig = Script()
        else:
            script_sig = script_sig
        self.sequence = sequence

    @classmethod
    def parse(cls, s: bytes):
        #with -1,order is inversed ,which means abc → cba
        prev_tx = s.read(32)[::-1]
        prev_index = little_endian_to_int(s.read(4))
        script_sig = Script.parse(s)
        sequence = little_endian_to_int(s.read(4))
        return cls(prev_tx, prev_index, script_sig, sequence)

    def __repr__(self):
        pass
