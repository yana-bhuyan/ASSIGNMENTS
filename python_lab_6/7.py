n = int(input("Enter number of fruits: "))

s1 = set()
s2 = set()

print("Enter fruits for set 1:")
for i in range(n):
    s1.add(input())

print("Enter fruits for set 2:")
for i in range(n):
    s2.add(input())

print("Common fruits:", s1 & s2)
print("Only in s1:", s1 - s2)
print("Total fruits:", len(s1 | s2))