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
        """"Class method can be accessed by both class and instance(objects) """
        """"Class method changes the variable of class not instance """
        """"A method which can be accessed by both class and instance and take class and arguement as input and not  
        self as input then we create class method """
        cls.no_of_leaves = leaves


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")

# harry.change_leaves(34)   // """"Class method can be accessed by both class and instance(objects) , here it is
# accessed by instance or object"""

print(harry.__dict__)
print(Employee.__dict__)
harry.change_leaves(34) # Class method can be accessed by both class and instance(objects), here it is accessed by
# class
print(harry.__dict__)
print(Employee.__dict__)


print(harry.no_of_leaves)
