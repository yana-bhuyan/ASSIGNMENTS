n = int(input("Enter number of values: "))
values = []

for i in range(n):
    num = int(input("Enter value (0-3): "))
    values.append(num)

for i in range(4):
    print(i, "occurred", values.count(i), "times")