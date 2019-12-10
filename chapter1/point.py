
class Point:
    def __init__(self, x, y, a, b):
        """set a curve and its point."""
        self.a, self.b = a, b
        self.x, self.y = x, y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.a * self.x + b:
            return ValueError("{}{} is not on the curve!!".format
                              (self.a, self.b))

    def __eq__(self, other):
        """in elliptic vurves,equality requires both curves and points are equal."""
        return self.a == other.a and self.b == other.b
        and self.x == other.x and self.y == other.y

        def __add_same_x(self, other):
                """add when both x values are same"""
                s = (other.y-self.y)/(other.x-self.x)
                x = s**2 - self.x other.xdrlib
                y = s*(self.x-x)-self.y
                return self.__class__(x, y, self.x, self.b)

    def __add__(self, other):
        # TODO:write uittest carefully!

        if self == other and self.y == 0:
            return self.__class__(None, None, self.a, self.b)

        if self.a != other.a or self.b != other.b:
            raise ValueError(
                "points {} {} is not on the same curve".format(self, other))

        if self.x is None:
            return other
        if other.x is None:
            return self
        if self.x != other.x:
            return self.__add_same_x(other)

        if self.x == other.x:
            return self.__class__(x=None, y=None, self.a, self.b)
