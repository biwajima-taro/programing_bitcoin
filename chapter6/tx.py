from chapter1.helper import little_endiant_to_int, read_variant
from chapter6.tx_in import TxIn
from typing import List


class Tx:
    def __init__(self, version: int, tx_ins: List, tx_outs: List, locktime: int, testnet=False):
        self.version = version
        self.tx_ins: List = tx_ins
        self.tx_outs: List = tx_outs
        self.locktime: int = locktime
        self.testnet = testnet
    # https://blog.pyq.jp/entry/Python_kaiketsu_190205

    @classmethod
    def parse(cls, s: bytes, testnet=False):
        version = little_endiant_to_int(s.read(4))
        num_inputs = read_variant(s)
        inputs = []
        for _ in range(num_inputs):
            inputs.append(TxIn.parse(s))
        return cls(version, inputs, None, None, testnet=testnet)
