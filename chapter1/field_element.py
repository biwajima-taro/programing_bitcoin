
class FieldElement:
    'class representing a finite filed element'

    def __init__(self, num, prime):
        if num > prime or num < 0:
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


if __name__ == "__main__":
    print("test")
