def rules():
    print("This is your contact book. Write numbers 1-6 to fo : ")
    print("1. Add contact")
    print("2. View contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Delete All contact")
    print("6. Exit",)
def add_contact(contact_book):
    name = input("Write contact name: ")
    if name in contact_book:
        print("This contact already exists in your contact book!")
        return
    number = input("Write phone: ")
    email = input("Write email of contact(you can skip this): ")
    address = input("Write address of contact(you can skip this): ")
    contact_book[name] = {
    "Name": name,
    "Number": number,
    "Email": email,
    "Address":address
    }
    print("Contact was succesfully added to your contact book!")
def view_contact(contact_book):
    name = input("Write contact name:")
    if contact_book == {}:
        print("Contact book is empty!")
        return
    if name not in contact_book:
        print("This name does not exists in your contact book!")
        return
    print("Name:", name)
    print("Number:", contact_book[name]["Number"])
    print("Email:", contact_book[name]["Email"])
    print("Address:", contact_book[name]["Address"])
def edit_contact(contact_book):
    name = input("Write name what you want to edit: ")
    if name not in contact_book:
        print("This name does not exists in your contact book!")
        return
    number = input("Write number: ")
    email = input("Write email of contact(you can skip this): ")
    address = input("Write adress of contact(you can skip this): ")
    contact_book[name] = {
    "Name": name,
    "Number": number,
    "Email": email,
    "Address":address
    }
    print("Contact has been edited!")
def delete_contact(contact_book):
    name = input("Write name what you want to delete:")
    if name not in contact_book:
        print("This name does not exists in your contact book!")
        return
    del contact_book[name]
    print("Contact has been deleted!")
def delete_all_contact(contact_book):
    if contact_book == {}:
        print("Contact book already empty!")
        return
    contact_book.clear()
    print("All contacts has been deleted!")
session = True
contact_book = {}
while session == True:
    rules()
    choice = int(input("Write number from 1 till 6: "))
    if choice < 1 or choice > 6:
        print("Incorrect, please write number from 1 to 6.")
    if choice == 1:
        add_contact(contact_book)
    if choice == 2:
        view_contact(contact_book)
    if choice == 3:
        edit_contact(contact_book)
    if choice == 4:
        delete_contact(contact_book)
    if choice == 5:
        delete_all_contact(contact_book)
    if choice == 6:
        session = False