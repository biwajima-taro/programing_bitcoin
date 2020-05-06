from helper import little_endian_to_int, read_variant
from transaction_input import TxIn

class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
        self.version = version
        self.tx_ins = tx_ins

    @classmethod
    def parse(cls, s, testnet=False):
        version = little_endian_to_int(s.read(4))
        num_of_input = read_variant(s)
        inputs=[]
        for _ in range(num_inputs):
            innputs.append(TxIn.parse(s))
        return cls(version, None, None, None, testnet)
