string = input("Enter string: ").upper()
freq = {}

for ch in string:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

for key in sorted(freq):
    print(freq[key], key)