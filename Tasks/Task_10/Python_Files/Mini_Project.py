class Book:
    def __init__(self):
        self.title = input("Enter Book Title:")
        self.author = input("Enter Author Name:")
        self.status = "Available"

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print(self.title, "Has Been Issued Successfully.")
        else:
            print(self.title, "Is Already Issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print(self.title, "Has Been Returned Successfully.")
        else:
            print(self.title, "Was Not Issued.")

    def show_info(self):
        print("\nTitle :", self.title)
        print("Author :", self.author)
        print("Status :", self.status)

library = []

def add_book():
    book = Book()
    library.append(book)
    print("Book Added Successfully!")

def issue_book():
    title = input("Enter Book Title To Issue:")

    for book in library:
        if book.title == title:
            book.issue_book()
            return

    print("Book Not Found!")

def return_book():
    title = input("Enter Book Title To Return:")

    for book in library:
        if book.title == title:
            book.return_book()
            return

    print("Book Not Found!")

def show_all_books():
    if len(library) == 0:
        print("No Books Available.")
    else:
        for book in library:
            book.show_info()


while True:
    print("\n***** LIBRARY MANAGEMENT SYSTEM *****")
    print("1. Add New Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        show_all_books()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")