


class Signature:
    def __init__(self,r,s):
        self.r=r
        self.s=s

    def __repr__(self):
        return "{}({:x},{:x})".format(self.__class__.__name__,self.r,self.s)