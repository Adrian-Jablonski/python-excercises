sentance = input("Enter a word: ").lower()
words = sentance.split()    # splits words into a list
word_histogram = {}

for word in words:
    inDict = word_histogram.get(word, "None")
    if inDict == "None":
        word_histogram[word] = 1
    else:
        word_histogram[word] += 1

print(word_histogram)