class Book:
    def __init__(self, bookid, title, author):
        self.bookid = bookid
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, bookid):
        book_to_remove = None
        for book in self.books:
            if book.bookid == bookid:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book with ID {bookid} has been removed.")
        else:
            print(f"Book with ID {bookid} not found.")

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            status = "Checked out" if book.is_checked_out else "Available"
            print(f"ID: {book.bookid}, Title: {book.title}, Author: {book.author}, Status: {status}")

    def checkout_book(self, bookid):
        for book in self.books:
            if book.bookid == bookid:
                if not book.is_checked_out:
                    book.is_checked_out = True
                    print(f"Book '{book.title}' has been checked out.")
                else:
                    print("This book is already checked out.")
                return
        print("Book not found.")

    def return_book(self, bookid):
        for book in self.books:
            if book.bookid == bookid:
                if book.is_checked_out:
                    book.is_checked_out = False
                    print(f"Book '{book.title}' has been returned.")
                else:
                    print("This book is already in the library.")
                return
        print("Book not found.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Check Out Book")
        print("5. Return Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            bookid = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            book = Book(bookid, title, author)
            library.add_book(book)

        elif choice == '2':
            bookid = input("Enter Book ID to remove: ")
            library.remove_book(bookid)

        elif choice == '3':
            library.list_books()

        elif choice == '4':
            bookid = input("Enter Book ID to check out: ")
            library.checkout_book(bookid)

        elif choice == '5':
            bookid = input("Enter Book ID to return: ")
            library.return_book(bookid)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
