def func1():
    print("Hello")


# del func1 -- if we delete here it will show error
func2 = func1
del func1  # if we delete here it will not show error
func2()


# We can return function in a function

# def returner(a):
#     if a == 1:
#         return sum
#     elif a == 0:
#         return print
#
#
# print(returner(0))

# ***************************************************

# a function can be passed as argument
# def executor(func):
#     func("I am a string")
# executor(print)

# ******************************** DECORATOR ************************

def dec1(func3):
    def nowexec():
        print("Executing now")
        func3()
        print("Execution ended")

    return nowexec
    

@dec1
def func3():
    print("I am func 3")


# func3 = dec1(func3) // this line can also be written as in line 40

func3()
