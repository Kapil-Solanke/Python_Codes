a = 0
while a < 9:
    i = int(input("Enter the number \n"))
    if i > 18:
        print("Greater, Think Small")
    elif i < 18:
        print("Smaller , Think Big")
    else:
        print("You Guessed It Right")
        break
    a = a + 1
    print("No of guesses left :", 9 - a)
    if a == 9:
        print("Game over")
