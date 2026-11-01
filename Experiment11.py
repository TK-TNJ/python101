# Develop a Python program to maintain a library catalogue using text files. The program 
# should store book details in a text file, allow new books to be added, search for books 
# by title or author, update the catalogue by appending new entries, and generate reports 
# such as the total number of books or books by a specific author. 


# Library Catalogue Management System

FILE_NAME = "library.txt"

# Function to add new books
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")

    with open(FILE_NAME, "a") as file:
        file.write(book_id + "," + title + "," + author + "\n")

    print("Book added successfully!")


# Function to display all books
def display_books():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n----- LIBRARY CATALOGUE -----")

            for line in file:
                book_id, title, author = line.strip().split(",")
                print("Book ID:", book_id)
                print("Title:", title)
                print("Author:", author)
                print("--------------------")

    except FileNotFoundError:
        print("No books found!")


# Function to search books by title
def search_title():
    title = input("Enter book title to search: ").lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                book_id, book_title, author = line.strip().split(",")

                if title in book_title.lower():
                    print("Book Found:", book_id, book_title, author)
                    found = True

        if not found:
            print("Book not found!")

    except FileNotFoundError:
        print("Catalogue is empty!")


# Function to search books by author
def search_author():
    author = input("Enter author name to search: ").lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                book_id, title, book_author = line.strip().split(",")

                if author in book_author.lower():
                    print("Book Found:", book_id, title, book_author)
                    found = True

        if not found:
            print("No books found for this author!")

    except FileNotFoundError:
        print("Catalogue is empty!")


# Function to generate reports
def generate_report():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        print("\nTotal Number of Books:", len(books))

        author = input("Enter author name for report: ").lower()
        count = 0

        for line in books:
            book_id, title, book_author = line.strip().split(",")

            if author in book_author.lower():
                count += 1

        print("Books by this author:", count)

    except FileNotFoundError:
        print("Catalogue is empty!")


# Main menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search by Title")
    print("4. Search by Author")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_title()
    elif choice == "4":
        search_author()
    elif choice == "5":
        generate_report()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
