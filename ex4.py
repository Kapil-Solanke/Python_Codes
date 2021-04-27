# ONE METHOD

# print("Pattern printing")
# num = int(input("Enter num how many rows you want : "))
# print("Enter 1 or 0")
# bool_val = input("1 for True value or 0 for False : ")
# if bool_val=="1":
#     for i in range(0,num+1):
#         print("*"*i)
#
# if bool_val=="0":
#     for i in range(num,0,-1):
#         print("*"* i)

# SECOND METHOD

# n = int(input("Enter the lines in star pattern\n"))
# b = int(input("Enter 0 for reverse pattern  or 1 for straight pattern\n"))
# c = bool(b)
# if c == True:
#     for i in range(0, n + 1):
#         print("*" * i)
#
# elif c == False:
#     for j in range(n,0, -1):
#         print("*" * j)

# THIRD METHOD

def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print("*" * a)
            c = c + 1
    else:
        while a > 0:
            print("*" * a)
            a = a - 1


star(5, 1)
