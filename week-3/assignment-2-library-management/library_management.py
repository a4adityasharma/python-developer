class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Book added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.issued:
                    print("Cannot remove an issued book.")
                    return

                self.books.remove(book)
                print("Book removed successfully.")
                return

        print("Book not found.")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.issued:
                    print("Book is already issued.")
                else:
                    book.issued = True
                    print("Book issued successfully.")
                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.issued:
                    print("Book is already available.")
                else:
                    book.issued = False
                    print("Book returned successfully.")
                return

        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
            return

        print("\nLibrary Books")
        print("-" * 60)

        for number, book in enumerate(self.books, start=1):
            print(f"{number}. {book}")


def main():
    library = Library()

    library.add_book("Python Crash Course", "Eric Matthes")
    library.add_book("Clean Code", "Robert C. Martin")
    library.add_book("Automate the Boring Stuff with Python", "Al Sweigart")

    library.display_books()

    print("\nIssuing 'Python Crash Course'...")
    library.issue_book("Python Crash Course")

    library.display_books()

    print("\nReturning 'Python Crash Course'...")
    library.return_book("Python Crash Course")

    print("\nRemoving 'Clean Code'...")
    library.remove_book("Clean Code")

    library.display_books()


if __name__ == "__main__":
    main()
