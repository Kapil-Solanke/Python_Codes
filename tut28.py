# f = open("harry.txt", "w") // erase old content and add new
# f.write("hary is good")
# f.close()


# f = open("harry.txt", "a") //write at end and keep old content
# a = f.write("hary is good") #f.write() returns chareacter wriiten
# print(a)
# f.close()

f = open("harry.txt", "r+") # read and write both
print(f.read()) # f.read() reads only what was in the file before opening not what is added now
f.write("harry is good") #writes inthe original file
print(f.read())
f.close()