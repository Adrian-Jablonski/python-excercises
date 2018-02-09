count = 0
numb = 2

while count <= 10001:
    
    i = 2
    prime = True    #flag
    while i < numb:
        if numb % i == 0:
            prime = False
        i += 1
    if prime == True:
        count += 1  # counts number of primes
    if count == 5000:
        print(numb) 
        break
    numb += 1
    
