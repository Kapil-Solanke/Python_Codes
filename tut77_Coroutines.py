def searcher():
    import time
    # any task taking 4 seconds
    book = "This is a book which will be read by the compiler first."
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Text in the book")
        else:
            print("Text not in the book")


search = searcher()
print("search started")
next(search)  # This line will take 4 seconds
#  After this line code will be runned from while loop

print("next method has runned now")

search.send("book")
search.close()  # Used to close coroutine

search.send("book")  # This line will show StopIteration error

#  ******************************* Practice Question *********************************
""""
def searchName():
    import time
    ls = ["Kapil", "Rohan", "Rony", "Shan", "Sam", "Son"]
    time.sleep(3)
    while True:
        #  We have to use while loop because yield is a generator so can be iterated once that is whhy we use while loop
        #  so we can call searchName more than once
        givenName = (yield)
        if givenName in ls:
            print("Your name in list")
        else:
            print("Your name is not in list")


search = searchName()
next(search)
name = input("Enter your name")
search.send(name)
# name = input("Enter your name")
# search.send(name)
name = input("Enter your name")
search.send(name)

search.close()  

"""
