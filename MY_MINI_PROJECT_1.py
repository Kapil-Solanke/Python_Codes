class Library:
    def __init__(self, list_of_books, name_of_Libray):
        self.list_of_books = list_of_books
        self.name_of_library = name_of_Libray
        self.name_of_person = None

    def displayBook(self):
        for index, item in enumerate(self.list_of_books):
            print(index, ".", item)

    def lendBooK(self, books_name, name_of_person):
        if books_name in self.list_of_books:
            if self.name_of_person is None:
                print(f"{name_of_person} , you can have the book {books_name}.")
                self.name_of_person = name_of_person
            else:
                print(f"{self.name_of_person} has {books_name}, You may  contact him/her .")
        else:
            print(f"The book is not present in the library.")

    def returnBook(self, name_of_book, name_of_person):
        print(f"{name_of_person} , Thank You for returning {name_of_book}")
        self.list_of_books.append(name_of_book)
        self.name_of_person = None

    def addBook(self, add_book, name_of_person):
        if add_book in self.list_of_books:
            print(f"The {add_book} is already present in the library.")
        else:
            self.list_of_books.append(add_book)
            print(f"The {add_book} is added . Thank you {name_of_person} .")

    def main(self):
        exit = True
        print("Welcome to Harry Library\n\nWhat do you want to do\nEnter 1 for display book \nEnter 2 for add book"
              "Enter 3 for lend book\nEnter 4 for return book")
        choice = int(input())

        while exit is not False:
            if choice == 1:
                self.displayBook()
            elif choice == 2:
                self.addBook()
            elif choice == 3:
                self.lendBooK()
            elif choice == 4:
                self.returnBook()
            else:
                print("Invalid option entered")

            print("\nThank You for using Harry Library")


if __name__ == '__main__':
    Harry = Library(["a", "b", "c"], "Harry")
    Harry.main()
