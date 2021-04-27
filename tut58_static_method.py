""""Some method take self as argument eg.init , some method take class as argument eg.classmethod , but static method
take no class and self as arguments"""


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
        # list1 = string1.split("-")
        # return cls(list1[0],list1[1],list1[2])
        # The above two lines can be written in below single line
        return cls(*string1.split("-"))

    @staticmethod
    def printfunc(str):
        print("I am a static method and argument given to me is: " + str)


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")
karan = Employee.from_dash("Karan-346-Invigilator")

karan.printdetails()

harry.printfunc("Harry")  # accessed by instance
Employee.printfunc("Employee")  # accessed by class
