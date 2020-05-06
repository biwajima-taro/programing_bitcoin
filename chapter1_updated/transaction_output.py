from script import Script
from helper import little_endian_to_int

class TxOut:
    def __init__(self, amount, script_pubkey):
        self.amount = amount
        self.script_pubkey = script_pubkey

    def __repr__(self):
        return f"{self.__class__.__name__}({self.amount},{self.script_pubkey})"

    @classmethod
    def parse(cls, s):
        amount = little_endian_to_int(4)
        script_pub = Script.parse(s)
        return cls(amount, script_pub)
