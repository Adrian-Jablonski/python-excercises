userFile = input("Enter a file name to open and read: ")

letter_histogram = {}
word_histogram = {}

try:
    file_handle = open(userFile, "r")
    contents = file_handle.read()
    contents = contents.lower()
    words = contents.split()
    file_handle.close()

except FileNotFoundError:
    print("File does not exist")

for char in contents:
    inDict = letter_histogram.get(char, "None")
    if inDict == "None":    # if character does not exist in dictionary
        letter_histogram[char] = 1
    else:   # if character already exists, add 1
        letter_histogram[char] += 1
print("Letter - Summary")
print(letter_histogram)

for word in words:
    inDict = word_histogram.get(word, "None")
    if inDict == "None":
        word_histogram[word] = 1
    else:
        word_histogram[word] += 1

print("Word - Summary")
print(word_histogram)