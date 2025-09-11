# inheritance example
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print("Name of the employee :",self.name)
        print("Salary of employee:",self.sal)
class Manager(Employee):
    def __init__(self, name, sal,dept):
        super().__init__(name,sal)
        self.dept=dept
    def display(self):
        print("Name of the employee :",self.name)
        print("Salary of employee:",self.sal)
        print("dept of employee:",self.dept)
obj1=Manager("jay",50000,"software")
obj1.display()
obj2=Employee("jayanth",30000)
obj2.display()

