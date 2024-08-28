# contact_book.py

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone_number = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone_number]
        if found_contacts:
            print("Search results:")
            for contact in found_contacts:
                print(f"{contact.name} - {contact.phone_number} - {contact.email} - {contact.address}")
        else:
            print("No contacts found.")

    def update_contact(self):
        name = input("Enter contact name to update: ")
        for contact in self.contacts:
            if contact.name == name:
                print("Enter new details (press Enter to keep current value):")
                contact.phone_number = input(f"Enter new phone number ({contact.phone_number}): ") or contact.phone_number
                contact.email = input(f"Enter new email ({contact.email}): ") or contact.email
                contact.address = input(f"Enter new address ({contact.address}): ") or contact.address
                print(f"Contact '{name}' updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter contact name to delete: ")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()