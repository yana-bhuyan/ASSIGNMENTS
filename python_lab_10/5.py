class FileEmptyError(Exception):
    pass

class InvalidDataError(Exception):
    pass

try:
    with open("data.txt", "r") as f:
        data = f.read()

    if not data:
        raise FileEmptyError("File is empty!")

    if not data.replace("\n", "").isalnum():
        raise InvalidDataError("Invalid data!")

    print("Valid data.")

except FileNotFoundError:
    print("File not found!")

except FileEmptyError as e:
    print("Custom Error:", e)

except InvalidDataError as e:
    print("Custom Error:", e)