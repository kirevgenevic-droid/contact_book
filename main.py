from time import sleep
import os 
import json
def save():
    with open("contact_book.json", "w") as file:
        json.dump(contact_book, file)
def rules():
    print("This is your contact book. Write numbers 1-6 to use functions : ")
    print("1. Add contact")
    print("2. View contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Delete All contact")
    print("6. Exit")
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
    save()
    print("Contact was succesfully added to your contact book!")
def view_contact(contact_book):
    if contact_book == {}:
        print("Contact book is empty!")
        return
    for name in contact_book:
        print("Name:", name)
    name = input("Write contact name:")
    if name not in contact_book:
        print("This name does not exists in your contact book!")
        return
    print("Name:", name)
    print("Number:", contact_book[name]["Number"])
    print("Email:", contact_book[name]["Email"])
    print("Address:", contact_book[name]["Address"])
def edit_contact(contact_book):
    if contact_book == {}:
        print("Contact book is empty!")
        return
    for name in contact_book:
        print("Name:", name)
    name = input("Write name what you want to edit: ")
    if name not in contact_book:
        print("This name does not exists in your contact book!")
        return
    number = input("Write number: ")
    email = input("Write email of contact(you can skip this): ")
    address = input("Write address of contact(you can skip this): ")
    contact_book[name] = {
    "Name": name,
    "Number": number,
    "Email": email,
    "Address":address
    }
    save()
    print("Contact has been edited!")
def delete_contact(contact_book):
    if contact_book == {}:
        print("Contact book is empty!")
        return
    for name in contact_book:
        print("Name:", name)
    name = input("Write name what you want to delete:")
    if name not in contact_book:
        print("This name does not exists in your contact book!")
        return
    del contact_book[name]
    save()
    print("Contact has been deleted!")
def delete_all_contact(contact_book):
    if contact_book == {}:
        print("Contact book already empty!")
        return
    contact_book.clear()
    save()
    print("All contacts has been deleted!")
try:
    with open("contact_book.json", "r") as file:
        contact_book = json.load(file)
except(FileNotFoundError):
    contact_book = {}
session = True
count = 0
while session == True:
    sleep(1)
    rules()
    try:
        choice = int(input("Write number from 1 till 6: "))
    except ValueError:
        os.system('cls')
        print("Invalid input.Please write a number from 1 to 6.")
        continue
    if choice < 1 or choice > 6:
        os.system('cls')
        print("Incorrect, please write number from 1 to 6.")
    elif choice == 1:
        os.system('cls')
        add_contact(contact_book)
        count += 1
    elif choice == 2:
        os.system('cls')
        view_contact(contact_book)
        count += 1
    elif choice == 3:
        os.system('cls')
        edit_contact(contact_book)
        count += 1
    elif choice == 4:
        os.system('cls')
        delete_contact(contact_book)
        count += 1
    elif choice == 5:
        os.system('cls')
        delete_all_contact(contact_book)
        count += 1
    elif choice == 6:
        session = False
        print("Good bye!")
