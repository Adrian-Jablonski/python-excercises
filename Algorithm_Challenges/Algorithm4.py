number = 13195
i = 1
primeList1 = []
primeList2 = []

while i < (number / 2):
    # prime list
    if number % i == 0:
        primeList1.append(i)
    
    i += 1

primeCheck = True
j = 2

for factor in primeList1:
    if factor % j == 0:
        primeCheck = False
    if primeCheck == True:     
        primeList2.append(factor)
    j += 1

print(primeList2[len(primeList2) - 1])