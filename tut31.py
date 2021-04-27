f = open("harry.txt")
# print(f.tell())  # f.tell() tells us where our file pointer ,i.e f, is at that particular time
# f.readline()
# print(f.tell())
# f.readline()
# print(f.tell())
# f.readline()
# print(f.tell())

# if we want that our file pointer i.e f , should be  at a particular place at a time we can use f.seek()

print(f.readline())
f.seek(0)  # If we had not used f.seek() then after f.readline() would have printed next line not previous one
print(f.readline())
f.close()