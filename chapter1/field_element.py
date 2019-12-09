

class FieldElement:
    """class representing a finite filed element"""

    def __init__(self, num: int, prime: int):
        """constructor."""
        if num > prime or num < 0 or type(num) != int or type(prime) != int:
            raise ValueError("illegal input")
        self.num = num
        self.prime = prime

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __add__(self, other):
        if self.prime != other.prime:
            raise ValueError("cannot two add numbers in diffrent fields")
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise ValueError("cannot subtract numbers in diffrent fields")
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "FieldElement(num={},prime={})".format(self.num, self.prime)


if __name__ == "__main__":
    tmp = FieldElement(12, 13)
    print(tmp)
