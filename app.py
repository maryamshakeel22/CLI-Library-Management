# Dictionary to store books and available copies
library = {}
def add_book():
    """Function to add a book to the library"""
    title = input("Enter book title: ").strip()
    copies = int(input("Enter number of copies: "))

    if title in library:
        library[title] += copies  # Increase copies if book exists
    else:
        library[title] = copies  # Add new book

    print(f'✅ "{title}" added successfully!')

def display_books():
    """Function to display all available books"""
    if not library:
        print("📖 No books available.")
        return

    print("\n📚 Available Books:")
    for title, copies in library.items():
        print(f"📖 {title} - {copies} copies")

def borrow_book():
    """Function to borrow a book from the library"""
    title = input("Enter the book title you want to borrow: ").strip()

    if title in library and library[title] > 0:
        library[title] -= 1  # Reduce book copy count
        print(f'✅ You borrowed "{title}". Enjoy reading!')
    else:
        print("❌ Book not available!")

def return_book():
    """Function to return a borrowed book"""
    title = input("Enter the book title you are returning: ").strip()

    if title in library:
        library[title] += 1  # Increase book count
    else:
        library[title] = 1  # Add book if it was not in system

    print(f'✅ Thank you for returning "{title}".')

# Main Menu Loop
while True:
    print("\n📘 Library Management System 📘")
    print("1️⃣ Add Book")
    print("2️⃣ Display Books")
    print("3️⃣ Borrow Book")
    print("4️⃣ Return Book")
    print("5️⃣ Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("📚 Thank you for using the Library System!")
        break
    else:
        print("❌ Invalid choice! Please select a valid option.")