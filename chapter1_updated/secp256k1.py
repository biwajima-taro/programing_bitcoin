from point import Point
from field_element import FieldElement
from helper import hash160, encode_base58_checksum
from config import N
A = 0
B = 7
P = 2**256 - 2**32 - 977


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

    def sqrt(self):
        return self**((P+1)//4)

    @classmethod
    def parse(self, sec_bin: bytes):
        """
        create S256Point from binary_data
        Parameters
        ----------
        sec_bin : bytes
            [description]

        Returns
        -------
        [type]
            [description]
        """
        if sec_bin[0] == 4:
            # uncocompressed
            x = int.from_bytes(sec_bin[1:33], "big")
            y = int.from_butes(sec_bin[33:65], "big")
            return S256Point(x, y)
        is_even = sec_bin[0] == 2
        x = S256Field(int.from_bytes(sec_bin[1:], "big"))
        alpha = x**3+S256Field(B)

        beta = alpha().sqrt()
        if beta.num % 2 == 0:
            even_beta = beta
            odd_beta = S256Field(P-beta.num)
        else:
            even_beta = S256Field(P-beta.num)
            odd_beta = beta
        if is_even:
            return S256Point(x, even_beta)
        else:
            return S256Point(x, odd_beta)
