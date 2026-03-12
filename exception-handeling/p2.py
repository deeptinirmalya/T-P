

contacts = {}

def add_contact():
    try:
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()

        if name == "" or phone == "":
            raise ValueError("Fields cannot be empty!")

        if name in contacts:
            raise Exception("Contact already exists!")

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be 10 digits!")

        contacts[name] = phone
        print("Contact saved successfully!")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


def edit_contact():
    try:
        name = input("Enter contact name to edit: ").strip()

        if name not in contacts:
            raise KeyError("Contact not found!")

        new_phone = input("Enter new phone number: ").strip()

        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("Invalid phone number format!")

        contacts[name] = new_phone
        print("Contact updated successfully!")

    except KeyError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)


def search_contact():
    try:
        name = input("Enter name to search: ").strip()

        if name == "":
            raise ValueError("Search field cannot be empty!")

        if name not in contacts:
            raise KeyError("Contact not found!")

        print("Name:", name)
        print("Phone:", contacts[name])

    except ValueError as e:
        print("Error:", e)
    except KeyError as e:
        print("Error:", e)


def view_contacts():
    try:
        if len(contacts) == 0:
            raise Exception("No contacts saved!")

        print("\nContact List:")
        for name, phone in contacts.items():
            print(name, "-", phone)

    except Exception as e:
        print("Error:", e)


while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Search Contact")
    print("4. View Contacts")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            edit_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            view_contacts()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a number between 1 and 5!")