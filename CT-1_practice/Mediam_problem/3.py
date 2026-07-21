#Find the Longest Word in a Sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)