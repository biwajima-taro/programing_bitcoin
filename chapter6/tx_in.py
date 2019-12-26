from chapter1.helper import little_endiant_to_int


class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        """represent input ,which is a elment of transaction"""
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        # opnening a locked box sth that can only be done by the owner of
        if script_sig is None:
            self.script_sig = script_sig
        else:
            self.script_sig = script_sig

    @classmethod
    def parse(cls, s: bytes)
    prev_tx: bytes = s.read(32)[::-1]
    prev_index: int = little_endiant_to_int(s.read(4))
    script_sig = Script.parse(s)
    sequence = little_endiant_to_int(s.read(4))

    return cls(prev_tx, prev_index, script_sig, sequence)

    def __repr__(self) -> str:
        return "{}:{}".format(self.prev_tx.hex(), self.prev_index)
