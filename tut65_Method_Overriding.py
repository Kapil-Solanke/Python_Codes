class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"


class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()  # Position of this line matters a lot
        print(super().classvar1)  # super().classvar1 this is used to print class variables of super class not instance variables


a = A()
b = B()

# print(b.classvar1)
# how the above line works explained in below line
# first it wil find instanc varibales in its own class ,here b , second it will find in instance variable
# in that class from which it is derived , third it will find in class variable in its own class , here B ,
# fourth then it will  go to find in class variable in that class from which it is derived


print(b.special, b.var1, b.classvar1)

