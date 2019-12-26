from chapter1.helper import little_endiant_to_int, read_variant
from chapter6.tx_in import TxIn
from typing import List


class Tx:
    def __init__(self, version: int, tx_ins: List[TxIn], tx_outs: List, locktime: int, testnet=False):
        """representing transaction"""
        self.version: int = version
        self.tx_ins: List[TxIn] = tx_ins
        self.tx_outs: List = tx_outs
        self.locktime: int = locktime
        self.testnet = testnet

    # https://blog.pyq.jp/entry/Python_kaiketsu_190205
    @classmethod
    def parse(cls, s: bytes, testnet=False):
        """make transaction class from bytes input"""
        version: int = little_endiant_to_int(s.read(4))
        #read the number of input from bytes
        num_inputs = read_variant(s)
        inputs:List = []
        for _ in range(num_inputs):
            inputs.append(TxIn.parse(s))
        return cls(version, inputs, None, None, testnet=testnet)
