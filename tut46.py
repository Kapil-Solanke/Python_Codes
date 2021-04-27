def printhar(string):
    return f"Ye string harry ko de de thakur {string}"


def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__)
# ese file mai name == main show karega kahi dusre jagah import kare to name  == es file ka naam show karega

if __name__ == '__main__':
    # if __name__ == '__main__' this is used to tell the program that agra ese file mai run karoge tabhi if __name__
    # == '__main__  ke andar jo bhi hai vo execute karo agar ye file kahi dusre jagah import kare ho to vaha
    # if __name__ == '__main__' ke andar jo bhi hai vo execute mat karna

    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)

