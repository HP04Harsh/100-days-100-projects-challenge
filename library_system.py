# Library Management System using Constructor and Methods

class Book:
    def __init__(self, title, author):
        # Constructor initializes book details
        self.title = title
        self.author = author
        self.is_issued = False  # Track if book is issued

    def issue_book(self):
        # Method to issue a book
        if not self.is_issued:
            self.is_issued = True
            print(f"'{self.title}' has been issued.")
        else:
            print(f"'{self.title}' is already issued.")

    def return_book(self):
        # Method to return a book
        if self.is_issued:
            self.is_issued = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not issued.")

    def display_info(self):
        # Method to display book details
        status = "Issued" if self.is_issued else "Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


# Creating objects using constructor
book1 = Book("Python Basics", "John Doe")
book2 = Book("AI Fundamentals", "Jane Smith")

# Using methods
book1.display_info()
book1.issue_book()
book1.display_info()
book1.return_book()
book1.display_info()