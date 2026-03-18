def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add_numbers(10, 20, 30))


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


display_info(name="Yana", age=18)