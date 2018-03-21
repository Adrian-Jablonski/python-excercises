listOne = [2, 4, 5]
listTwo = [2, 3, 6]
listResult = []

n = 0

while n < len(listOne):
     listResult.append(listOne[n] * listTwo[n])
     n += 1

print(listResult)