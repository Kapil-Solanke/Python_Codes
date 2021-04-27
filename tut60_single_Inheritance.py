class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        print(f"Name is {self.name}, Salary is {self.salary}, Role is {self.role}")

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves

    @classmethod
    def from_dash(cls, string1):
        return cls(*string1.split("-"))

    @staticmethod
    def printfunc(str):
        print("I am a static method and argument given to me is: " + str)


class Programmer(Employee):
    def __init__(self, aname, asalary, arole, language):
        # super().__init__(aname, asalary, arole) This is super call    
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = language

    def printprog(self):
        print(f"Name is {self.name}, Salary is {self.salary}, Role is {self.role} . Language is {self.language}")


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")

karan = Programmer("Karan", 555, "Programmer", ["Python"])

karan.printprog()
