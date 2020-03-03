class Point:
    def __init__(self, x, y, a, b):    
        """point class forv elliptic curves.
            there exist only add .
        Args:
            x ([type]): [description]
            y ([type]): [description]
            a ([type]): [description]
            b ([type]): [description]
        
        Raises:
            ValueError: [description]
        """        
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.y**2 == self.x**3+self.a*x+self.b:
            raise ValueError("is not on the curve")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

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
