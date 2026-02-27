tasks = []

while True:
    print("1.Add 2.View 3.Remove 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for i, task in enumerate(tasks):
            print(i+1, task)

    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)

    elif choice == "4":
        break