def display_menu():
    print("\nEmail Directory Menu:")
    print("1. Look up an email address")
    print("2. Add a new contact")
    print("3. Update an Existing contact")
    print("4. Delete a contact")
    print("5. Display all contacts")
    print("6. List All email addresses")
    print("7. Exit")

def look_up_email(directory):
    name = input("Enter the name to look up: ")
    if name in directory:
        print(f"The email address for {name} is {directory[name]}")
    else:
        print(f"{name} was not found in the directory")

def add_contact(directory):
    name = input("Enter the name: ")
    email = input("Enter the email address: ")
    if name in directory:
        print(f"{name} already exists in the directory.")
    else:
        directory[name] = email
        print(f"{name} has been added to the directory.")

def update_contact(directory):
    name = input("Enter the name to update: ")
    if name in directory:
        email = input("Enter the new email address: ")
        directory[name] = email
        print(f"Email address for {name} has been updated.")
    else:
        print(f"{name} was not found in the directory.")

def remove_contact(directory):
    name = input("Enter the name to remove: ")
    if name in directory:
        del directory[name]
        print(f"{name} has been removed from the directory.")
    else:
        print(f"{name} was not found in the directory.")

def display_all_contacts(directory):
    if directory:
        print("\nAll Contacts:")
        for name, email in directory.items():
            print(f"{name}: {email}")
    else:
        print("The directory is empty.")

def list_all_emails(directory):
    if directory:
        print("\nAll Email Addresses:")
        for email in directory.values():
            print(email)
    else:
        print("The directory is empty.")

def main():
    directory = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            look_up_email(directory)
        elif choice == '2':
            add_contact(directory)
        elif choice == '3':
            update_contact(directory)
        elif choice == '4':
            remove_contact(directory)
        elif choice == '5':
            display_all_contacts(directory)
        elif choice == '6':
            list_all_emails(directory)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()