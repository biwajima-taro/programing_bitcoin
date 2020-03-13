from __future__ import annotations
from typing import Any
from field_element import S256Field
# eliptica curve parameter for bicoin!
A = 0
B = 7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


class Point:
    def __init__(self, x: Any, y: Any, a: Any, b: Any):
        """
        all arguments x,y,a,b must be the same class
        Parameters
        ----------
        x : Any
        y : Any
        a : Any
        b : Any
        Raises
        ------
        ValueError
        if not on the elliptic curve raise error
        """
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.y**2 != self.x**3+self.a*x+self.b:
            raise ValueError("is not on the curve")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and \
            self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not(self == other)

    def __add__(self, other: Point) -> Point:
        if self.a != other.a or self.b != other.b:
            raise TypeError()
        if self.x is None:
            return other
        if other.x is None:
            return self
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)
        if self.x != other.x:
            slope = (other.y-self.x)/(other.x-self.x)
            x = slope**2-self.x-other.x
            y = slope*(self.x-x)-self.y
            return self.__class__(x, y, self.a, self.b)
        if self == other:
            slope = (3*self.x**2+self.a)/(2*self.y)
            x = slope**2-2*self.x
            y = slope*(self.x-x)-self.y
            return self.__class__(x, y, self.a, self.b)

    def __repr__(self) -> str:
        return f"Point(x={self.x},y={self.y},a={self.a},b={self.b})"

    def __rmul__(self, coefficient: int) -> Point:
        coef = coefficient
        current = self  # <1>
        result = self.__class__(None, None, self.a, self.b)  # <2>
        while coef:
            if coef & 1:  # <3>
                result += current
            current += current  # <4>
            coef >>= 1  # <5>
        return result


class S256Point(Point):

    def __init__(self, x, y, a=None, b=None):
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)
        else:
            # x is S56Field case
            super().__init__(x=x, y=y, a=a, b=b)

    def __repr__(self):
        if self.x is None:
            return "S256Point(infinity)"
        else:
            return f"S256point({self.x},{self.y})"

    def __rmul__(self, coefficient: int):
        coef = coefficient % N
        return super().__rmul__(coef)

    def sec(self, compressed=True):
        '''returns the binary version of the SEC format'''
        if compressed:
            if self.y.num % 2 == 0:
                return b'\x02' + self.x.num.to_bytes(32, 'big')
            else:
                return b'\x03' + self.x.num.to_bytes(32, 'big')
        else:
            
            return b'\x04' + self.x.num.to_bytes(32, 'big') + \
                self.y.num.to_bytes(32, 'big')
    # end::source1[]


if __name__ == "__main__":
    a = Point(-1, -1, 5, 7)
    print(a)
    # rais error
    print(2*a)
