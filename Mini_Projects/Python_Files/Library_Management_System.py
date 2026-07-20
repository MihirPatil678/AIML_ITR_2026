# Project 2 - Library Management System

book = {}  # Stores All Book Data

def add_book():
    isbn = input("Enter ISBN:")

    if isbn in book:
        print("ISBN Already Exists!")
        return

    title = input("Enter Title:")
    author = input("Enter Author:")

    book[isbn] = {
        "isbn": isbn,
        "title": title,
        "author": author,
        "status": "Available"
    }

    print("Book Added!")
    print(f"ISBN: {isbn} | Title: {title} | Author: {author} | Status: Available")

def view_all():
    if len(book) == 0:
        print("No Books Found.")
        return

    for isbn in book:
        b = book[isbn]
        print(f"ISBN: {b['isbn']} | Title: {b['title']} | Author: {b['author']} | Status: {b['status']}")

def search_book():
    isbn = input("Enter ISBN To Search:")

    if isbn not in book:
        print("Book Not Found.")
        return

    b = book[isbn]

    print("ISBN:", b['isbn'])
    print("Title:", b['title'])
    print("Author:", b['author'])
    print("Status:", b['status'])

def issue_book():
    isbn = input("Enter ISBN To Issue:")

    if isbn not in book:
        print("Book Not Found.")
        return

    if book[isbn]["status"] == "Issued":
        print("Book Already Issued.")
        return

    book[isbn]["status"] = "Issued"

    print("Book Issued Successfully!")
    print("Title:", book[isbn]['title'])

def return_book():
    isbn = input("Enter ISBN To Return:")

    if isbn not in book:
        print("Book Not Found.")
        return

    if book[isbn]["status"] == "Available":
        print("Book Is Already Available.")
        return

    book[isbn]["status"] = "Available"

    print("Book Returned Successfully!")

def delete_book():
    isbn = input("Enter ISBN To Delete:")

    if isbn not in book:
        print("Book Not Found.")
        return

    confirm = input(f"Delete {book[isbn]['title']}? (y/n):")

    if confirm == "y":
        del book[isbn]
        print("Book Deleted.")
    else:
        print("Cancelled.")

# Main Menu Loop
while True:
    print("\n*** LIBRARY MANAGEMENT SYSTEM ***")
    print("1. Add Book")
    print("2. View All")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice.")