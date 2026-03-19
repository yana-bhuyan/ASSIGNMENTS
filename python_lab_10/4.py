n = int(input("Enter number of test cases: "))

for _ in range(n):
    try:
        a, b = input("Enter two numbers: ").split()
        result = int(a) // int(b)
        print(result)

    except ZeroDivisionError as e:
        print("Error Code:", e)

    except ValueError as e:
        print("Error Code:", e)