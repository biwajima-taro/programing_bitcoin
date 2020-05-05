from config import G, N
from random import randint
from signature import Signature
from helper import encode_base58_checksum

class PrivateKey:
    def __init__(self, secret):
        self.secret = secret
        self.point = secret*G

    def hex(self):
        return "{:x}".format(self.secret).zfill(64)

    def sign(self, z):
        k = randint(0, N)
        r = (k*G).x.num
        k_inv = pow(k, N-2, N)
        s = (z+r*self.secret)*k_inv % N
        # ToDO:check why this if statement is needed
        if s > N/2:
            s = N-2
        return Signature(r, s)

    def wif(self, compressed=True, testnet=False):
        secret_bytes=self.secret.to_bytes(32,"big")
        if  test_net:
            prefix=b"\xef"
        else:
            prefix=b"\x80"
        if compressed:
            suffix=b"\x01"
        else:
            suffix=""
        return encode_base58_checksum(prefix+secret_bytes+suffix)