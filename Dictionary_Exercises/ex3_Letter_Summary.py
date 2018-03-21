word = input("Enter a word: ").lower()
letter_histogram = {}

for char in word:
    inDict = letter_histogram.get(char, "None")
    if inDict == "None":    # if character does not exist in dictionary
        letter_histogram[char] = 1
    else:   # if character already exists, add 1
        letter_histogram[char] += 1

print(letter_histogram)