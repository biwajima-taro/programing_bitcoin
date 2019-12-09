
class Point:
	def __init__(self,x,y,a,b):
		self.a,self.b=a,b
		self.x,self.y=x,y
		if self.x is None and self.y is None:
			return 
		if self.y**2 !=self.a*self.x+b:
			return ValueError("{}{} is not on the curve!!".format(self.a,self.b))

	def  __add__(self,other):

		if self.x==other.x:
			return self.__class__(x=None,y=None,self.a,self.b)