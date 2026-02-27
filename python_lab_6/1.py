string = input("Enter a string: ")
count = 0

for ch in string:
    if ch.isupper():
        count += 1

print("Number of capital letters:", count)