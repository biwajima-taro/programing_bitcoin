from point import Point
from field_element import FieldElement
from helper import hash160, encode_base58_checksum
A = 0
B = 7
P = 2**256 - 2**32 - 977
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


class S256Field(FieldElement):
    def __init__(self, num):
        super().__init__(num=num, prime=P)

    def __repr__(self):
        return "{:x}".format()


class S256Point(Point):
    def __init__(self, x, y):
        a, b = S256Field(A), S256Field(B)
        super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)

    def __rmul__(self, coefficient: int):
        coef = coefficient % N
        return super().__rmul__(coef)

    def sec(self, compressed=True):
        if compressed:
            if self.y.num % 2 == 0:
                return b"\x02"+self.x.num.to_bytes(32, "big")
            else:
                return b"\x03"+self.x.num.to_bytes(32, "big")
        else:
            # b"\x04".hex()
            # with hex() you can display hexadecimal version
            return b"\x04"+self.x.to_bytes(32, "big")+self.y.to_bytes(32, "big")

    def hash160(self, compressed=True, testnet=False):
        return hash160(self.sec(compressed))

    def address(self, compressed=True, testnet=False):
        h160 = self.hash160(compressed)
        if testnet:
            prefix = b"\x6f"
        else:
            prefix = b"\x"
        return encode_base58_checksum(prefix+h160)
