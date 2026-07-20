class Book:
    def __init__(self, title, author, price):
        self.title  = title
        self.author = author
        self.price  = price
 
    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: Rs.", self.price)

book1 = Book("Sherlock Holmes", "Sir Arthur Conan Doyle", 989)
book2 = Book("Harry Potter", "J.K. Rowling", 1299)
book1.show_details()
book2.show_details()