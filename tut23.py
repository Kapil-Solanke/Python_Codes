# a = 3
# b = 4
# c = sum((a, b)) -> Built in fxn
# print(c)

# Docstring is a comment which is the first line in a fxn which tells about the sxn , you can print the doc string
# by using fxnname.__doc__


def func1(a, b):
    """ this is function to find exponents"""
    print("Hello")
    return a ** b

print(func1.__doc__)
# for storing retutn value in some variable
# d = func1(3, 3)
# print(d)
# for printing return value

print(func1(3,3))
