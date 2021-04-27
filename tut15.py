print("Enter first num")
a = int(input())
print("Enter first num")
b = int(input())
print("enter the operator")
print("a = add \n d = divide \n s = substract \n m = multiply")
o = input()
# print(o)

if a == 45 & b == 3 & o == "m":
    print("555")
elif a == 56 & b == 9 & o == "a":
    print("77")
elif a == 56 & b == 6 & o == "d" :
    print("4")
elif o == "a":
    print(a+b)
elif o == "d":
    print(a/b)
elif o == "m":
    print(a*b)
elif o == "s" :
    print(a - b)
else:
    print("Sorry")



