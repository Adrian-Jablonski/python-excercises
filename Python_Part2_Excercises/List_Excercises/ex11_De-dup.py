listStr = ["one", "two", "one", "three", "four", "one", "four", "five"]
listNumb = [1, 2, 3, 10, 1, 3, 5, 4, 1, 1, 6, 8, 9, 3, 10, 7]

x = 0
y = 0

listStr.sort()
listNumb.sort()

newListStr = [listStr[0]]
newListNumb = [listNumb[0]]

for word in listStr:
    if word != newListStr[x]:
        newListStr.append(word)
        x += 1

for numb in listNumb:
    if numb != newListNumb[y]:
        newListNumb.append(numb)
        y += 1

print(newListStr)
print(newListNumb)
