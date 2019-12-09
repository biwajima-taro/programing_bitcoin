

class FieldElement:
    """class representing a finite filed element."""

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

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError("cannot divide in diffrent fields")
        num = self.num*pow(other.num, self.prime-2, self.prime) % self.prime
        return self.__class__(num=num, prime=self.prime)

    def __pow__(self, exponent):
        n=exponent % (self.prime-1)
        num=pow(self.num,n,self.prime)
        #num = (self.num**exponent) % self.prime
        return self.__class__(num=num, prime=self.prime)

    def __repr__(self):
        return "FieldElement(num={},prime={})".format(self.num, self.prime)

if __name__ == "__main__":
    import time
    tmp = FieldElement(12, 13)
    #ex7
    for p in [7,11,17,31]:
        tmp=[ pow(ele,p-1,p) for ele in range(1,p)]
        print(tmp)
        time.sleep(2)

