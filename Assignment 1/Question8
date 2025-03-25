import os

CATALOGUE_FILE = "library_catalogue.txt"

def load_catalogue():
    """Load the catalogue from file or create new if doesn't exist"""
    if not os.path.exists(CATALOGUE_FILE):
        with open(CATALOGUE_FILE, "w"):
            pass  # Create empty file
        return []
    with open(CATALOGUE_FILE, "r") as file:
        return [line.strip().split("|") for line in file.readlines()]

def save_catalogue(catalogue):
    """Save the catalogue to file"""
    with open(CATALOGUE_FILE, "w") as file:
        for book in catalogue:
            file.write("|".join(book) + "\n")

def add_book(catalogue):
    """Add a new book to the catalogue"""
    print("\nAdd a New Book")
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    catalogue.append([title.strip(), author.strip(), year.strip()])
    save_catalogue(catalogue)
    print("\nBook added successfully!")

def list_books(catalogue):
    """Display all books in the catalogue"""
    print("\nLibrary Catalogue:")
    if not catalogue:
        print("No books in the catalogue.")
        return
    
    for i, book in enumerate(catalogue, 1):
        print(f"{i}. {book[0]} by {book[1]}, Published in {book[2]}")

def search_books(catalogue):
    """Search for books by title or author"""
    term = input("\nEnter title or author to search: ").lower()
    results = [book for book in catalogue 
               if term in book[0].lower() or term in book[1].lower()]
    
    if not results:
        print("No matching books found.")
        return
    
    print("\nSearch Results:")
    for i, book in enumerate(results, 1):
        print(f"{i}. {book[0]} by {book[1]}, Published in {book[2]}")

def remove_book(catalogue):
    """Remove a book from the catalogue"""
    list_books(catalogue)
    if not catalogue:
        return
    
    try:
        choice = int(input("\nEnter the number of the book to remove: "))
        if 1 <= choice <= len(catalogue):
            removed = catalogue.pop(choice - 1)
            save_catalogue(catalogue)
            print(f"\nRemoved: {removed[0]} by {removed[1]}")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")

def display_menu():
    """Display the main menu"""
    print("\nPlease choose an option:")
    print("1 - Add a New Book")
    print("2 - List All Books")
    print("3 - Search for a Book")
    print("4 - Remove a Book")
    print("0 - Exit")

def main():
    """Main program function"""
    catalogue = load_catalogue()
    print("\nWelcome to your Personal Library Catalogue!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            add_book(catalogue)
        elif choice == "2":
            list_books(catalogue)
        elif choice == "3":
            search_books(catalogue)
        elif choice == "4":
            remove_book(catalogue)
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter 0-4.")

if __name__ == "__main__":
    main()