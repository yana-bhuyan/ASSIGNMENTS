try:
    # Writing names to file
    with open("name.txt", "w") as f:
        names = ["Aman", "Neha", "Ishita", "Om", "Ravi", "Uday"]
        for name in names:
            f.write(name + "\n")

    # Reading names from file
    with open("name.txt", "r") as f:
        names = [line.strip() for line in f]

    print("Total names:", len(names))

    vowels = ('A', 'E', 'I', 'O', 'U')
    count_vowel = sum(1 for n in names if n.upper().startswith(vowels))
    print("Names starting with vowel:", count_vowel)

    longest = max(names, key=len)
    print("Longest name:", longest)

except Exception as e:
    print("Error:", e)