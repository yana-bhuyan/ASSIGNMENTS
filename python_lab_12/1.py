class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.marks = {"Physics": phy, "Chemistry": chem, "Maths": maths}

    def display(self):
        print(f"\nName: {self.name}")
        print(f"SAP ID: {self.sap_id}")
        print(f"Marks: {self.marks}")

    def marks_percentage(self):
        total = sum(self.marks.values())
        percentage = total / 3
        return percentage

    def result(self):
        for subject, mark in self.marks.items():
            if mark <= 40:
                return "Fail"
        return "Pass"


students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i+1}")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = float(input("Enter Physics marks: "))
    chem = float(input("Enter Chemistry marks: "))
    maths = float(input("Enter Maths marks: "))

    s = Student(name, sap_id, phy, chem, maths)
    students.append(s)

print("\n--- Student Details ---")
for s in students:
    s.display()
    print(f"Percentage: {s.marks_percentage():.2f}%")
    print(f"Result: {s.result()}")


def class_average(students):
    total = 0
    for s in students:
        total += s.marks_percentage()
    avg = total / len(students)
    return avg


print(f"\nClass Average Percentage: {class_average(students):.2f}%")