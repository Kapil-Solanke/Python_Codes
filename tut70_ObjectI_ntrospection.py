class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    # def email(self):
    #     return f"{self.fname}.{self.lname}@codewithharry.com"

    @property  # Here we are taking email as an attributes but actually it is a funcn
    def email(self):
        if self.fname == None and self.lname == None:
            return "Eail is not set"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, str1):
        names = str1.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skilllf = Employee("Skill", "F")
# print(skilllf.email)
# In Python everything is an object int , str

# OBJECT INTROSPECTION -> It means to know about he object , eg. of what class it is , of what type

# print(type(skilllf))

# Every OBJECT has an UNIQUE ID
# print(id(skilllf))

#  NOTE - dir() -> It tells us  wht all methods can we apply to given object

# print(dir(skilllf))
# print(dir(str))

import inspect
print(inspect.getmembers(skilllf))