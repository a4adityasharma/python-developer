contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def search_contact():
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ").strip()
    if name in contacts:
        contacts[name]["phone"] = input("Enter new phone number: ").strip()
        contacts[name]["email"] = input("Enter new email: ").strip()
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting contact book.")
        break
    else:
        print("Invalid choice. Please try again.")