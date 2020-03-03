from s256 import S256Point
G = 123

G: S256Point = S256Point(12, 12)


class PrivateKey:

    def __init__(self, secret: int):
        """test"""
        self.secret: int = secret
        self.point: S256Point = secret*G

    def hex(self) -> str:
        # {:x}で16進数にする
        return "{:x}".format(self.secret).zfill(64)


if __name__=="__main__":
   tnp= PrivateKey()