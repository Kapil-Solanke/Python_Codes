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


hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

# print(hindustani_supporter.email)
# hindustani_supporter.fname = "US"
# print(hindustani_supporter.email) # we cannot change email like this because at runtime when object was created the
# constructor ran at that time and email attribute was initialized .

# print(hindustani_supporter.email())
# hindustani_supporter.fname = "US"
# print(hindustani_supporter.email())

# One way to solve the problem is to create a funcn email and then do the above task ,but by doing these we will violate
# the principle of encapsulation , because we want that programmer should not worry about waht is going in the class
# so we want to give email as an attribute ,To solve this we can use "PROPERTY DECORATOR"


# print(hindustani_supporter.email)
# hindustani_supporter.fname = "US"
# print(hindustani_supporter.email)

# Now we want to set email and set all the attributes from which email is made . If we want I want to change email
# by this I want to change first name and last name and   for this  we can use "SETTER"

hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.email)

#  now if we want to delete our setted email we can use "DELETER"

del hindustani_supporter.email  # this line is finding "DELETER" in the class for this line to run we should have
# "DELETER" in our class

print(hindustani_supporter.email)

hindustani_supporter.email = "Ram.Nam@codewithharry.com"

print(hindustani_supporter.email)