class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        # Mehtod staring from __ and ending from  __ are called dunder methods
        # __init__ is a dunder method  also ot is special method because it is a constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        print(f"Name is {self.name}, Salary is {self.salary}, Role is {self.role}")

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves

    # We cannot do the given below thing to add we have to use dunder method , for more info serach dunder method
    # or go to link -- https://docs.python.org/3/library/operator.html
    # @classmethod
    # def add(self, other):
    #     return self.salary + other.salary

    def __add__(self, other):
        # add is a special method , it is called dunder add , and this method helps us in operator overloading
        # It is not necessary that all dunder method or special method overload the operator eg. str , repr
        return self.salary + other.salary

    def __repr__(self):
        # return f"Employee ( {self.name} , {self.salary} , {self.name}  )"
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")

# print(harry + rohan)

# print(harry)  # If we want to make output of these line beautiful we use repr and str methods .
# Note - when str is not there in class, compiler shows repr when executing these line .
# Note - when str is  there in class, compiler shows str when executing these line .
# Note - when str is  there in class, compiler shows str even when we try to execute repr because str is more prefered
# than repr  .

print(harry)  # the output of both the lines is same
print(str(harry))

print(harry.salary + rohan.salary)