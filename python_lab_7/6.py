contacts = {}

while True:
    print("1.Add 2.Search 3.Update 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Enter name to search: ")
        print(contacts.get(name, "Not Found"))

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")

    elif choice == "4":
        name = input("Enter name to delete: ")
        contacts.pop(name, None)

    elif choice == "5":
        break