from point import Point
from field_element import FieldElement
N = 10**3
A = None
B = None


class S256Field(FieldElement):
    def __init__(self, num, prime):
        super().__init__(num=num, prime=prime)

    def __repr__(self):
        return "{:x}".format()


class S256Point(Point):
    def __init__(self, x, y):
        a, b = S256Point(A), S256Point(B)
        super().__init__(x=S256Point(x), y=S256Point(y), a=a, b=b)

    def sec(self):
        return b"\x04"+self.x.num_to_bytes(32,"big")+self.y.num_to_bytes(32,"big")
