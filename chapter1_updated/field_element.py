class FieldElement:
    def __init__(self, num: int, prime: int):
        if num >= prime or num < 0 or type(num) != int or type(prime) != int:
            error_message = "num,prime must be integer ,and num <prime"
            raise ValueError(error_message)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f"{self.__class__.__name__}({self.num!r},{self.prime!r})"

    def __eq__(self, other):
        if other is None:
            return False
            # prime=5.num=0 and prime=5,num=5 isnt equal?
        return self.prime == other.prime and (self.num % self.prime) == (other.num % self.prime)

    def __add__(self, other):
        if self.prime != other.prime:
            raise ValueError("prime must be same")
        num = (self.num+other.num) % self.prime
        # TODO:what will hapen when subclass use self.__class__?
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise ValueError("prime must be same")
        num = (self.num-other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise ValueError("")
        num = (self.num*other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent: int):
        num = (self.num**exponent) % self.prime
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise ValueError("")
        other = other**(self.prime-2)
        print(other)
        return self*other

    def __rmul__(self, num):

        return self*self.__class__(num, self.prime)


if __name__ == "__main__":

    a = FieldElement(2, 19)
    print(a == 9)
    import time
    time.sleep(10)
    b = FieldElement(7, 19)
    print(a/b)
    print(b)
    import time
    time.sleep(10)

    print(repr(FieldElement(3, 100)))
    num_list = [1, 2, 3, 4, 5, 7, 9, 13, 18]
    for num in num_list:
        tmp_set = set()
        for i in range(19):
            tmp_set.add((i*num) % 19)
        print(tmp_set)

    print("\n\n")
    ###############################
    num_list = [7, 13, 31]
    for prime in num_list:
        tmp_set = set()
        for num in range(1, prime):
            tmp_set.add((num**(prime-1)) % prime)
        print(tmp_set)
