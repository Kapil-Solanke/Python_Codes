import time

start = time.time()
print(start)
a = "bad"
c = 2
# b = "You are %s %s" % (c, a)  # This way is not good when we want ot insert  more no of variables eg. 1 0 0r 20 variables
b = "You are {1} {0}"
# d = b.format(c,a) # this is also not good way for big insertions

d = f"You are {a} {c}"  # this is f string , her f stands for fast
print(d)

# time.sleep(1) //It is use to tell program to wait for given seconds , here 1
end = time.time()
print(end)
print("Time of program ")
print(time.time() - start)
