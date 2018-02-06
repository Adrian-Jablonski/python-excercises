listOne = [[1, 3, 3, 4], [2, 4, 3, 4]]
listTwo = [[5, 2, 2, 4], [1, 0, 2, 4]]
listResult =[]
finalResult = []

x = 0
y = 0

listLength = len(listOne[0])

while x < 2:
    y = 0
    while y < listLength:
        listResult.append(listOne[x][y] + listTwo[x][y])
        y += 1
    x += 1

finalResult.append(listResult[:listLength])
finalResult.append(listResult[listLength:])

print(finalResult)