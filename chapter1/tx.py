class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
        self.version = version
        self.tx_ins = tx_ins
        self.tx_outs = tx_outs
        self.locktime = locktime
        self.testnet = testnet

    @classmethod
    def parse(cls, stream):
        serized_version = stream.read(4)
        return int.from_bytes(serized_version, "little")
