from __future__ import annotations
from typing import Any


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
        # point at intfinity or representing zero in finitefield
        product = self.__class__(None, None, self.a, self.b)
        for _ in range(coefficient):
            product += self
        return product


if __name__ == "__main__":
    a = Point(-1, -1, 5, 7)
    print(a)
    # rais error
    print(2*a)
