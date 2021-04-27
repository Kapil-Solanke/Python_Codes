import os

print(os.getcwd())
#  cwd = current working directory
# os.chdir("C://")   # For changing current working directory
print(os.getcwd())

#  When we import or open a file the program first searches the file in current working directory

# print(os.listdir())  # It gives all the files in current working directory

# print(os.listdir("C://"))  # It gives all the files in given working directory

# os.mkdir("this")  # this creates a folder in current working directory

# os.makedirs("this/that")  # To make folders in a folders we use makedirs()

# os.rename("ps.py", "RoughPractice.py")

# print(os.environ.get("PATH"))
# print(os.path.join("C:/", "harry.txt"))
print(os.path.exists("C:/"))
print(os.path.isdir("C:/"))
