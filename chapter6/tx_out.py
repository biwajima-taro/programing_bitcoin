from chapter1.helper import little_endiant_to_int


class TxOut:
    def __init__(self, amount: int, script_pubkey):
        "representing output ,which is a elemnt of transaction"
        self.amount: int = amount
        self.script_pubkey = script_pubkey

    def __repr__(self):
        return "{}{}".format(self.amount, self.script_pubkey)

    @classmethod
    def parse(cls, s: bytes) -> TxOut:
        amount = little_endiant_to_int(s.read(8))
        script_pubkey = Script.parse(s)
        return TxOut(amount, script_pubkey)
