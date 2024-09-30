import sys

MAX_BOOKS = 100

class Book:
    def __init__(self):
        self.bookId = 0
        self.title = ""
        self.author = ""
        self.isAvailable = True

library = [Book() for _ in range(MAX_BOOKS)]
bookCount = 0

def addBook():
    global bookCount
    if bookCount == MAX_BOOKS:
        print("Library is full. Cannot add more books.")
        return

    library[bookCount].title = input("Enter book title: ")
    library[bookCount].author = input("Enter author name: ")
    library[bookCount].bookId = bookCount + 1
    library[bookCount].isAvailable = True

    print(f"Book added successfully. Book ID: {library[bookCount].bookId}")
    bookCount += 1

def displayBooks():
    if library[0].bookId == 0:
        print("Library is empty. No books to display.")
        return

    print("Book ID\tTitle\tAuthor\tStatus")
    for book in library:
        if book.bookId != 0:
            status = "Available" if book.isAvailable else "Checked Out"
            print(f"{book.bookId}\t{book.title}\t{book.author}\t{status}")

def searchBook():
    searchTitle = input("Enter the title of the book to search: ")
    found = False

    for book in library:
        if book.bookId != 0 and book.title == searchTitle:
            found = True
            print("Book is found!")
            status = "Available" if book.isAvailable else "Checked Out"
            print(f"Book ID: {book.bookId}\nTitle: {book.title}\nAuthor: {book.author}\nStatus: {status}")
            break

    if not found:
        print("Book not found in the library.")

def borrowBook():
    bookId = int(input("Enter the Book ID to borrow: "))

    if bookId < 1 or bookId > MAX_BOOKS or library[bookId - 1].bookId == 0:
        print("Invalid Book ID. Please enter a valid Book ID.")
        return

    if library[bookId - 1].isAvailable:
        print("Book successfully borrowed.")
        library[bookId - 1].isAvailable = False
    else:
        print("Sorry, the book is already checked out.")

def returnBook():
    bookId = int(input("Enter the Book ID to return: "))

    if bookId < 1 or bookId > MAX_BOOKS or library[bookId - 1].bookId == 0:
        print("Invalid Book ID. Please enter a valid Book ID.")
        return

    if not library[bookId - 1].isAvailable:
        print("Book successfully returned.")
        library[bookId - 1].isAvailable = True
    else:
        print("This book is already in the library.")

def deleteBook():
    bookId = int(input("Enter the Book ID to delete: "))

    if bookId < 1 or bookId > MAX_BOOKS or library[bookId - 1].bookId == 0:
        print("Invalid Book ID. Please enter a valid Book ID.")
        return

    # Shift the remaining books to fill the gap
    for i in range(bookId - 1, MAX_BOOKS - 1):
        library[i] = library[i + 1]

    print("Book successfully deleted.")

def displayAvailableBooks():
    if library[0].bookId == 0:
        print("Library is empty. No books to display.")
        return

    print("Available Books:")
    print("Book ID\tTitle\tAuthor")
    for book in library:
        if book.bookId != 0 and book.isAvailable:
            print(f"{book.bookId}\t{book.title}\t{book.author}")

def updateBook():
    bookId = int(input("Enter the Book ID to update: "))

    if bookId < 1 or bookId > MAX_BOOKS or library[bookId - 1].bookId == 0:
        print("Invalid Book ID. Please enter a valid Book ID.")
        return

    library[bookId - 1].title = input("Enter updated book title: ")
    library[bookId - 1].author = input("Enter updated author name: ")
    print("Book details updated successfully.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Display Available Books")
        print("8. Update Book")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            addBook()
        elif choice == 2:
            displayBooks()
        elif choice == 3:
            searchBook()
        elif choice == 4:
            borrowBook()
        elif choice == 5:
            returnBook()
        elif choice == 6:
            deleteBook()
        elif choice == 7:
            displayAvailableBooks()
        elif choice == 8:
            updateBook()
        elif choice == 0:
            print("\nExiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

