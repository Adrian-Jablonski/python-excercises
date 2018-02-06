str1 = input("Enter a word to extend long vowels: ")
doubleVowList = ["a", "e", "i", "o", "u"]

c = 0

while c < len(doubleVowList):
    doubleVowLocation = str1.find(doubleVowList[c] * 2)
    if doubleVowLocation >= 0:
        str1 = str1.replace(doubleVowList[c] * 2, doubleVowList[c] * 5)
    c += 1

print(str1)
