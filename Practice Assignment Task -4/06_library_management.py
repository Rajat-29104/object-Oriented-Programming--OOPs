# Program: Library Management System

class Book:

    def __init__(self, title):

        self.title = title

        self.issued = False


class Member:

    def __init__(self, name):

        self.name = name


class Library:

    def __init__(self):

        self.books = []

    def add_book(self, title):

        self.books.append(Book(title))

        print(title, "added successfully")

    def issue_book(self, title):

        for book in self.books:

            if book.title == title and not book.issued:

                book.issued = True

                print(title, "issued successfully")

                return

        print("Book not available")

    def return_book(self, title):

        for book in self.books:

            if book.title == title and book.issued:

                book.issued = False

                print(title, "returned successfully")

                return

        print("Book not found")

    def display_books(self):

        print("\nAvailable Books")

        for book in self.books:

            if not book.issued:

                print(book.title)


library = Library()

member = Member("Rajat")

library.add_book("Python Programming")

library.add_book("Data Structures")

library.display_books()

library.issue_book("Python Programming")

library.display_books()

library.return_book("Python Programming")

library.display_books()