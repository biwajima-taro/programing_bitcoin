import sys
import os
sys.path.append(os.pardir)
sys.path.append("../../")
from chapter1.field_element import FieldElement
from chapter1.point import Point

class S256Field(FieldElement):

    def __init__(self, num, prime=None):
        super().__init__(num=num, prime=prime)

    def __repr__(self):
        return "{:x}".format(self.num).zfill(64)

class S256Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a,b=S256Field(a),S256Field(b)
        if type(x)==int:
            super().__init__(x=S256Field(x),y=S256Field(y),a=a,b=b)
            else:
                super().__init__(x=x,y=y,a=a,b=b)
                


