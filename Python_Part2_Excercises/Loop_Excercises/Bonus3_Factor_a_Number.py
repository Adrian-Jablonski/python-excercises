number = int(input("Enter a number to display all factors: "))
i = 1

while i <= (number):
    answer = int(number/i)
    if number % i == 0 and i <= answer:
        print(i, "X", answer)   # prints factors of the user's number
    i += 1