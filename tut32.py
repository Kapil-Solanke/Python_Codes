def getdate():
    import datetime
    return datetime.datetime.now()


def harry():
    if person == 0 and choice == 0:
        print("Enter the food\n")
        hf = input()
        f = open("Hwork.txt", "a")
        f.write(str([str(getdate())]) + ": " + hf + "\n")
        f.close()
    elif person == 0 and choice == 1:
        print("Enter the exercise\n", getdate())
        he = input()
        f = open("Hexercise.txt", "a")
        f.write(str([str(getdate())]) + ": " + he + "\n")
        f.close()


def rohan():
    if person == 1 and choice == 0:
        print("Enter the food\n", getdate())
        rf = input()
        f = open("Rwork.txt", "a")
        f.write(str([str(getdate())]) + ": " + rf + "\n")
        f.close()
    elif person == 0 and choice == 1:
        print("Enter the exercise\n", getdate())
        re = input()
        f = open("Rexercise.txt", "a")
        f.write(str([str(getdate())]) + ": " + re + "\n")
        f.close()


def hammad():
    if person == 0 and choice == 0:
        print("Enter the food\n", getdate())
        haf = input()
        f = open("Hawork.txt", "a")
        f.write(str([str(getdate())]) + ": " + haf + "\n")
        f.close()
    elif person == 0 and choice == 1:
        print("Enter the exercise\n", getdate())
        hae = input()
        f = open("Haexercise.txt", "a")
        f.write(str([str(getdate())]) + ": " + hae + "\n")
        f.close()


def retrieve():
    openfile = int(input("Enter  0.to open Harry file\n 1.to open Rohan file\n 2.to open Hammad file\n"))
    if openfile == 0:
        # f = open("Hwork.txt", "r")
        # print(f.readlines())
        # f.close()
        with open("Hwork.txt") as op:
            for i in op:
                print(i, end="")
        # f = open("Hexercise.txt", "r")
        # print(f.readlines())
        # f.close()
        with open("Hexercise.txt") as op:
            for i in op:
                print(i, end="")
    elif openfile == 1:
        with open("Rwork.txt") as op:
            for i in op:
                print(i, end="")
        with open("Rexercise.txt") as op:
            for i in op:
                print(i, end="")
    else:
        with open("Hawork.txt") as op:
            for i in op:
                print(i, end="")
        with open("Hexercise.txt") as op:
            for i in op:
                print(i, end="")


while True:
    person = int(input("Enter\n0.Harry\n 1.Rohan\n 2.Hammad\n"))
    choice = int(input("Enter\n0.lock food\n1.Exercise\n"))

    if person == 0:
        harry()
    elif person == 1:
        rohan()
    elif person == 2:
        hammad()

    choice1 = int(input("Do you want to open file\nEnter\n0 for No \n1 for Yes\n"))
    if choice1 == 1:
        retrieve()

    end = int(input("Do you want to exit, Enter 0 for No \n 1 for Yes"))
    if end == 1:
        break

print("End of the program")
