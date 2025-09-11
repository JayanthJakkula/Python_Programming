# create the class student
class Student:
    def __init__(self,name,r_n,m):
        self.name=name
        self.r_n=r_n
        self.m=m

    def display(self):
        print("Name of student is :",self.name)
        print("Roll_No is :",self.r_n)
        print("Marks :",self.m)
obj1=Student("jay","5cs",20)
obj1.display()
obj2=Student("jayanth","555",67)
obj2.display()


        