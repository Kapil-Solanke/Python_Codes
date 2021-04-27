try:
    f = open("harry.txt", "r+")
    f.close()
except Exception as e:
    print(e)

else:
    #  Anyone of else and except is executed if except ecexcuted then else is not executed and vice versa
    print("End")
finally:
    print("Finally is executed anyway wether try or except is executed")
