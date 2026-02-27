n = int(input("Enter number of values: "))
values = []

for i in range(n):
    values.append(float(input("Enter value: ")))

t = tuple(values)
average = sum(t) / len(t)

print("Average:", average)