def create_book(book_id, title, author):
    return {
        "id": book_id,
        "title": title,
        "author": author,
        "is_borrowed": False
    }

def create_member(member_id, name):
    return {
        "id": member_id,
        "name": name,
        "borrowed_books": []
    }

def process_transaction(books, members, m_id, b_id, action="issue"):
    if m_id not in members or b_id not in books:
        return False, "Error: ID not found."

    book = books[b_id]
    member = members[m_id]

    if action == "issue":
        if book["is_borrowed"]:
            return False, f"Error: '{book['title']}' is already out."
        book["is_borrowed"] = True
        member["borrowed_books"].append(b_id)
        return True, f"Success: Issued '{book['title']}' to {member['name']}."

    elif action == "return":
        if b_id not in member["borrowed_books"]:
            return False, f"Error: {member['name']} does not have this book."
        book["is_borrowed"] = False
        member["borrowed_books"].remove(b_id)
        return True, f"Success: '{book['title']}' returned."

def display_inventory(books):
    print(f"\n{'ID':<5} {'Title':<20} {'Author':<15} {'Status'}")
    print("-" * 50)
    for b_id, info in books.items():
        status = "Borrowed" if info["is_borrowed"] else "Available"
        print(f"{b_id:<5} {info['title']:<20} {info['author']:<15} {status}")

# def main():
books = {
    101: create_book(101, "Python Basics", "John Doe"),
    102: create_book(102, "Clean Code", "R. Martin"),
    103: create_book(103, "Data Science", "Jane Smith")
}
members = {
    1: create_member(1, "Alice"),
    2: create_member(2, "Bob")
}

while True:
    print("\n--- Library System ---")
    print("1. View Books\n2. Issue Book\n3. Return Book\n4. Exit")
    choice = input("Select option: ")

    if choice == "1":
        display_inventory(books)
    
    elif choice == "2":
        m_id = int(input("Enter Member ID: "))
        b_id = int(input("Enter Book ID: "))
        success, message = process_transaction(books, members, m_id, b_id, "issue")
        print(message)

    elif choice == "3":
        m_id = int(input("Enter Member ID: "))
        b_id = int(input("Enter Book ID: "))
        success, message = process_transaction(books, members, m_id, b_id, "return")
        print(message)

    elif choice == "4":
        print("Exiting system.")
        break
    else:
        print("Invalid choice.")

# if __name__ == "__main__":
#     main()