#Count the Occurrence of Each Character

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:")

for key in frequency:
    print(key, ":", frequency[key])