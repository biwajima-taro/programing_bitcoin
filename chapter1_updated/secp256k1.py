from point import Point
from field_element import FieldElement

class S256Field(FieldElement):
    def __init__(self,num,prime):
        super().__init__(num=num,prime=prime)

    def __repr__(self):
        return "{:x}".format()