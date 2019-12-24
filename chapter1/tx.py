class Tx:
    def __init__(self,version,tx_ins,tx_outs,locktime,testnet=False):
        self.version=version
        self.tx_ins=tx_ins
        self.tx_outs=tx_outs
        self.testnet=testnet

    def __repr__(self):
        tx_ins=""
        for tx_in in self.tx_ins:
            tx_ins=+=tx_in.__repr__()+"\n"