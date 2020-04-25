class FiniteField:
    def __init__(self, num: int, prime: int):
        if num >= prime or num < 0:
            error_message = ""
            raise ValueError(error_message)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f"{self.__class__.__name__}({self.num!r},{self.prime!r})"

    def __eq__(self, other):
        if other is None:
            return False
        # prime=5.num=0 and prime=5,num=5 isnt equal?
        return self.num == other.num and self.prime == other.prime

    def __add__(self, other):
        if self.prime != other.prime:
            raise ValueError("prime must be same")
        num = (self.num+other.num) % self.prime
        return self.__class__(num, self.prime)


if __name__ == "__main__":
    print(repr(FiniteField(3, 100)))
