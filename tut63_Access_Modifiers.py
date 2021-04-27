class Employee:
    no_of_leaves = 10
    var = 23

    # To create protected variable syntax is _nameofvariable
    _protectvar = 8

    # To create private variable syntax is _nameofvariable
    __privatevar = 34

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


karan = Employee("karan", 345, "Student")
print(karan._protectvar)  # we can access protected variable in same class and class derived from that class

# print(karan.__privatevar) you cannot privat variable by this syntax

print(karan._Employee__privatevar)  # Syntax for accesssing private variable is as shown. This is called NAME MANGLING
