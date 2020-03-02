
class FieldElement:
    def __init__(self, num: int, prime: int):
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f"FieldElement_{self.prime}({self.num})"

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

    def __sub__(self, other: FieldElement) -> FieldElement:
        if self.__check(other):
            num = (self.num-other.num) % self.prime
            return self.__class__(num, self.prime)

    def __check(self, other: FieldElement) -> bool:
        if self.prime == other.prime:
            return True
         raise TypeError("two number must be the same prime")
    
    def __mul__(self,other:FieldElement)->FieldElement:
        
        if self.__check(other):
            num=(self.num*other.num)%self.prime
            return self.__class__(slef.num,self.prime)


if __name__ == "__main__":
    # TODO execise2
    # TODO unittest
    print("hoge")
