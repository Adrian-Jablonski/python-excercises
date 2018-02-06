numberList = [5, 10, 1, -2, 20, -4, 16, 3, 4, 2, -30 ]
numberSum = 0
largestNumb =  numberList[0]
smallestNumb = numberList[0]
evenNumbList = []
positiveNumbList = []
factorList = []
factor = 5

n = 0

while n < len(numberList):
    numberSum += numberList[n] # sums the list
    if numberList[n] > largestNumb:
        largestNumb = numberList[n] # finds largest number
    elif numberList[n] < smallestNumb:
        smallestNumb = numberList[n] # finds smallest numb
    
    if numberList[n] % 2 == 0:
        evenNumbList.append(numberList[n])  # creates an even number list
    
    if numberList[n] > 0:
        positiveNumbList.append(numberList[n]) # creates a list of positive numbers

    factorList.append(factor * numberList[n])  # multiplies each list item by the factor

    n += 1 

print("Sum of list is ", numberSum)
print("The largest number is", largestNumb)
print("The smallest number is", smallestNumb)
print("Even number list: ", evenNumbList)
print("Positive number list: ", positiveNumbList)
print("Factor list by ", factor, ": ", factorList)