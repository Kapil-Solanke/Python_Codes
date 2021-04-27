lis = ["34", "45", "23"]

# Instead of using the below two lines we can use map function
# for i in range(len(lis)):
#     lis[i] = int(lis[i])

# ***************************************** MAP ************************************

lis = list(map(int, lis))
# map ( a, b) here a = which funcn to apply , b = on which object
# map returns object so we have to store in list , eg. print(map(int, lis))
lis[2] = lis[2] * 2
print(lis[2])
print(len(lis))

# Another example of map with lambda
# num = [2, 3, 4, 5, ]
# square = list(map((lambda a: a * a), num))
# print(square)

# Another example of map with lambda
# sq = lambda x: x * x
# cube = lambda y: y * y * y
#
# lis1 = [sq, cube]
#
# for i in range(5):
#     val = list(map(lambda x: x(i), lis1))
#     print(val)

#  ************************************** FILTER ***********************************

# def is_greaterthan_5(x):
#     return x > 5
#
#
# num = [2, 3, 4, 5, 6, 7, 8, 9]
#
# list2 = list(filter(is_greaterthan_5, num))
# print(list2)

# ********************************* REDUCE ******************************************

from functools import reduce

num = [2, 3, 4, 5, ]

sum = reduce(lambda x, y: x + y, num)
# sum = list((map(lambda x, y: x + y, num))) we cant do the above with map
print(sum)
