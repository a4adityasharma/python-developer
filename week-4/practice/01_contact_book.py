contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contacts[name] = phone
    print("Contact saved successfully.")


def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")


def display_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nContacts")
    print("-" * 30)
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
