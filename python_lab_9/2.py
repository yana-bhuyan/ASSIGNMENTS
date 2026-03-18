def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total


print("Sum of cubes:", sum_of_cubes(5))