l = [[1, "one"], [2, "two"], [3, "three"], [4, "four"]]
# for item, lolipop in l:
#     print(item, lolipop)

# Typecasting into dict and then printing
d = dict(l)
# When you want to print both keys and its values .items()
# for i , j in d.items() :
#     print(i, j)

# for only keys use below lines
# for i in d:
#     print(i)

li = [1, 45, "one", "h", 34, 7]
for i in li:
    if type(i) == int and i > 6:
        print(i)

# both the for loop are same
for i in li:
    if str(i).isnumeric() and i > 6:
        print(i)
