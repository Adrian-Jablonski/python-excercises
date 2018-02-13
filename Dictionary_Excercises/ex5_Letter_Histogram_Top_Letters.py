word = input("Enter a word: ").lower()
letter_histogram = {}
top_letters = []
top_3_letters= ["", "", ""]

for char in word:
    inDict = letter_histogram.get(char, "None")
    if inDict == "None":    # if character does not exist in dictionary
        letter_histogram[char] = 1
    else:   # if character already exists, add 1
        letter_histogram[char] += 1

print(letter_histogram)

for key, value in letter_histogram.items():
    if key == " ":  #excludes spaces in count
        pass
    else:
        combine = str(value) + key
        top_letters.append(combine)

top_letters.sort()
top_letters.reverse()

i = 0
while i < 3:
    top_3_letters[i] = top_letters[i][1] + ":" + top_letters[i][0]
    i += 1

print("Top 3 letters: ", top_3_letters)

