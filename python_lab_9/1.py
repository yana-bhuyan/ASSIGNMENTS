def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


nums = [10, 6, 8, 90, 12, 56]
print("Maximum and Minimum:", find_max_min(nums))