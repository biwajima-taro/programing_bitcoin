from __future__ import annotations


class FieldElement:
    def __init__(self, num: int, prime: int):
        """
        class for finite field calculation

        Args:
            num (int): []
            prime (int): [description]
        """
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f"FieldElement_{self.prime}({self.num})"

    def __truediv__(self, other:FieldElement)->FieldElement:
        """definition for division between FieldElement
        Parameters
        ----------
        other : FieldElement
        Returns
        -------
        FieldElement
        """        
        num = self.num*pow(other.num, self.prime-2, self.prime) % self.prime
        return self.__class__(num, self.prime)

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: FieldElement) -> bool:
        return not (self == other)

    def __add__(self, other: FieldElement) -> FieldElement:
        if self.__check(other):
            num = (self.num+other.num) % self.prime
            return self.__class__(num, self.prime)
        raise TypeError("two number must be the same prime")

    def __sub__(self, other: FieldElement) -> FieldElement:
        if self.__check(other):
            num = (self.num-other.num) % self.prime
            return self.__class__(num, self.prime)
        raise TypeError("two number must be the same prime")

  #  def __pow__(self, exponent) -> FieldElement:
   #     num = (self.num**exponent) % self.prime
    #    return self.__class__(num, self.prime)

    def __check(self, other: FieldElement) -> bool:
        if self.prime == other.prime:
            return True

    def __mul__(self, other: FieldElement) -> FieldElement:

        if self.__check(other):
            num = (self.num*other.num) % self.prime
            return self.__class__(num, self.prime)
        raise TypeError("two number must be the same prime")

    def __pow__(self, exponent: int) -> FieldElement:
        n = exponent % (self.prime-1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)


if __name__ == "__main__":
    # TODO execise2
    # TODO unittest
    print("hoge")
    # exercise5

    tmp = [FieldElement(num=3, prime=19)*FieldElement(i, prime=19)
           for i in range(18)]
    print(tmp)
