class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != x**3+self.a*self.x+self.b:
            raise ValueError("not on the curve")

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError("not on the same curve")
        if self.x is None:
            return other
        if other.x is None:
            return self
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)
        if self.x != other.x:
            s = (other.y-self.y)/(other.x-self.x)
            x = s**2-self.x-other.x
            y = s*(self.x-x)-self.y
            return self.__class__(x, y, self.a, self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.x == other.x \
            and self.y == other.y

    def __ne__(self, other):
        return self != other

    def __repr__(self):
        return f"{self.__class__.__name__}({self.a!r},{self.a!r},{self.x!r},\
            {self.y!r})"
