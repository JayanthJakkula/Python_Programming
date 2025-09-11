from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        print("Area of rectangle :",self.l*self.b)
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area of circle:",(3.14)*self.r*self.r)
ob1=Rectangle(2,5)
ob2=Circle(5)
ob1.area()
ob2.area()

