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
        # 0*self.x is used in case of any data types
        if self == other and self.y == 0*self.x:
            return self.__class__(None, None, self.a, self.b)

        if self == other:
            s = (3*self.x+self.a)/(2*self.y)
            x = s**2-2*self.x
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

    def __rmul__(self, coef: int):
        # point multiplication
        current = self
        print("**********************")
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            print("++++++++++")
            print(current)
            if coef & 1:
                result += current
            print("current***")
            current += current

            coef >>= 1
        return result


if __name__ == "__main__":
    from field_element import FieldElement
    prime = 223
    a = FieldElement(0, prime)
    b = FieldElement(7, prime)
    x = FieldElement(47, prime)
    y = FieldElement(71, prime)
    p = Point(x, y, a, b)
    print(p)
    for num in range(21):
        result = num*p
