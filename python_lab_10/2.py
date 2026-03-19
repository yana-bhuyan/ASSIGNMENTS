try:
    # Writing numbers to file
    with open("numbers.txt", "w") as f:
        nums = [10, 150, 200, 45, 99, 120, 300]
        for n in nums:
            f.write(str(n) + "\n")

    # Reading numbers from file
    with open("numbers.txt", "r") as f:
        nums = [int(line.strip()) for line in f]

    print("Maximum:", max(nums))
    print("Average:", sum(nums) / len(nums))

    count = sum(1 for n in nums if n > 100)
    print("Numbers > 100:", count)

except Exception as e:
    print("Error:", e)