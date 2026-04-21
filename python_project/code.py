import json
import csv

FILE = "expense.json"


def csv_to_json():
    data = []
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "note": row["note"]
                })

        with open(FILE, "w") as f:
            json.dump(data, f)

        print("CSV converted to JSON successfully!")

    except FileNotFoundError:
        print("CSV file not found. Skipping conversion.")



def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []



def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)



def add_expense(data):
    amount = float(input("Enter amount: "))
    category = input("Enter category (food/travel/etc): ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    data.append(expense)
    print("Expense added!")



def view_expenses(data):
    if not data:
        print("No expenses found.")
        return

    for i, exp in enumerate(data, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']}")


def total_expense(data):
    total = sum(exp["amount"] for exp in data)
    print("Total Expense: ₹", total)



def category_expense(data):
    result = {}

    for exp in data:
        cat = exp["category"]
        result[cat] = result.get(cat, 0) + exp["amount"]

    print("Category-wise Expenses:")
    for cat, amt in result.items():
        print(cat, ":", amt)



def main():
    csv_to_json()   

    data = load_data()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Expense")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            total_expense(data)
        elif choice == "4":
            category_expense(data)
        elif choice == "5":
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice!")


main()