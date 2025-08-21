import json
import os

BOOK_FILE = "address_book.json"

def load_book():
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_book(book):
    with open(BOOK_FILE, 'w') as f:
        json.dump(book, f, indent=2)

def add_contact(book):
    name = input("Name: ")
    address = input("Aptos Wallet Address: ")
    notes = input("Notes: ")
    book[name] = {'address': address, 'notes': notes}
    save_book(book)
    print(f"Contact '{name}' added.")

def view_contacts(book):
    if not book:
        print("No contacts in address book.")
        return
    for name, info in book.items():
        print(f"Name: {name}\nAddress: {info['address']}\nNotes: {info['notes']}\n---")

def search_contact(book):
    term = input("Search name: ")
    result = {n: i for n, i in book.items() if term.lower() in n.lower()}
    if result:
        for name, info in result.items():
            print(f"Name: {name}\nAddress: {info['address']}\nNotes: {info['notes']}\n---")
    else:
        print("Nothing found.")

def menu():
    print("\nAptos Address Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

def main():
    book = load_book()
    while True:
        menu()
        choice = input("Choose option: ")
        if choice == '1':
            add_contact(book)
        elif choice == '2':
            view_contacts(book)
        elif choice == '3':
            search_contact(book)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
