from helper import int_to_little_endian, hash256, little_endian_to_int, read_variant, encode_variant
from transaction_input import TxIn
from transaction_output import TxOut
from typing import List
from io import BytesIO
from script import Script
from transaction_fetcher import TxFetcher
SIGHASH_ALL = 1


class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
        self.version = version
        self.tx_ins: List[TxIn] = tx_ins
        self.tx_outs: List[TxOut] = tx_outs
        self.locktime = locktime
        self.testnet = testnet

    def fee(self, testnet=False):
        input_sum = 0
        output_sum = 0
        for txin in self.tx_ins:
            input_sum += txin.value(testnet)
        for txout in self.tx_outs:
            output_sum += txout.amount
        return input_sum-output_sum

    def serialize(self):
        result = int_to_little_endian(self.version, 4)
        result += encode_variant(len(self.tx_ins))
        for tx_in in self.tx_ins:
            result += tx_in.serialize()
        result += encode_variant(len(self.tx_outs))
        for tx_out in self.tx_outs:
            result += tx_out.serialize()
        result += int_to_little_endian(self.locktime, 4)
        return result

    @classmethod
    def parse(cls, s, testnet=False):
        version = little_endian_to_int(s.read(4))
        num_of_input = read_variant(s)
        inputs = []
        for _ in range(num_of_input):
            inputs.append(TxIn.parse(s))

        num_of_output = read_variant(s)
        outputs = []
        for _ in range(num_of_output):
            outputs.append(TxOut.parse(s))

        locktime = little_endian_to_int(s.read())
        return cls(version, None, None, None, testnet)

    def sig_hash(self, input_index: int):
        """
        create hash signiautre hash from input with designated index

        Parameters
        ----------
        input_index : int
            [description]\

        Returns
        -------
        [type]
            [description]
        """
        s: bytes = int_to_little_endian(self.version, 4)
        s += encode_variant(len(self.tx_ins))
        for i, tx_in in enumerate(self.tx_ins):
            if i == input_index:
                s += TxIn(prev_tx=tx_in.prev_tx, prev_index=tx_in.prev_index,
                          script_sig=tx_in.script_pubkey(self.testnet),
                          sequence=tx_in.sequence)
            else:
                s += TxIn(prev_tx=tx_in.prev_tx, prev_index=tx_in.prev_index,
                          sequence=tx_in.sequence)

        s += encode_variant(len(self.tx_outs))
        for tx_out in self.tx_outs:
            s += tx_out.serialize()
        s += int_to_little_endian(self.locktime, 4)
        s += int_to_little_endian(SIGHASH_ALL)
        h256 = hash256(s)
        return int.from_bytes(h256, "big")

    def verify_input(self, input_index: int):
        tx_in: TxIn = self.tx_ins[input_index]
        script_pubkey = tx_in.script_pubkey(testnet=self.testnet)
        z = self.sig_hash(input_index)
        comined = tx_in.script_sig+script_pubkey
        return comined.evaluate()

    def verify(self):
        if self.fee() < 0:
            # ==0 is allowed?
            return False
        for i in range(len(self.tx_outs)):
            if not self.verify_input(i):
                return False
        return True

    def sign_input(self, input_index: int, private_key):
        z = self.sig_hash(input_index)
        der = private_key.sign(z).der()
        sig = der+SIGHASH_ALL.to_bytes(1, "big")
        sec = private_key.point.sec()
        self.tx_ins[input_index].script_sig = Script([sig, sec])
        return self.verify_input(input_index)


class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        if script_sig is None:
            self.script_sig = Script()
        else:

            self.script_sig = script_sig
        self.sequence = sequence

    def fetch_tx(self, testnet=False):
        return TxFetcher.fetch(self.prev_tx.hex(), tesetnet=testnet)

    def value(self, testnet=False):
        """
        return input value

        Parameters
        ----------
        testnet : bool, optional
            [description], by default False

        Returns
        -------
        [type]
            [description]
        """
        tx: Tx = self.fetch_tx(testnet=testnet)
        return tx.tx_outs[self.prev_index].amount

    def script_pubkey(self, testnet=False):
        tx: Tx = self.fetch_tx(testnet=testnet)
        return tx.tx_outs[self.prev_index].script_pubkey

    def serialize(self):
        # with -1 ,it reverse  charactestrs' order
        result = self.prev_tx[::-1]
        result += int_to_little_endian(self.prev_index, 4)
        result += self.script_sig.serialize()
        result += int_to_little_endian(self.sequence, 4)
        return result

    @classmethod
    def parse(cls, s: bytes):
        # with -1,order is inversed ,which means abc → cba
        prev_tx = s.read(32)[::-1]
        prev_index = little_endian_to_int(s.read(4))
        script_sig = Script.parse(s)
        sequence = little_endian_to_int(s.read(4))
        return cls(prev_tx, prev_index, script_sig, sequence)

    def __repr__(self):
        pass


if __name__ == "__main__":
    raw_tx = bytes.fromhex('0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600')
    print(raw_tx[4])
    #stream = BytesIO(raw_tx)
    # stream.
    time.sleep(3)
    tx = Tx.parse(stream)
    #self.assertEqual(tx.version, 1)
f
