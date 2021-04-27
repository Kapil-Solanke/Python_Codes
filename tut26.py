f = open("harry.txt")  # f is a pointer here
# content = f.read()  # when file is read then th pointer becomes empty , means after this line f becomes empty
# print(content)

# this is another way to read file using f.readline() , same as loop
# Note - After using f.read() fxn we cant use for f.readline() to print text ,
# that is why we can use any one of f.read() or loop  or f.readline() to read content at one particular time
#
# print(f.readline())
# print(f.readline())
# print(f.readline())
    
# Note - After using f.read() fxn we cant use for loop to print text ,
# that is why we can use any one of f.ead() or loop or f.readline() to read content at one particular time

for l in f:
    print(l, end="")

