import random

secret_number = random.randint(1, 10)

guessed_number = False

print("I am thinking of a number between 1 and 10")

while guessed_number == False:
    guess = int(input("What's the number? "))
    if guess == secret_number:
        print("Yes! You win!")
        guessed_number = True
    elif guess < secret_number and guess >= 1:
        print(guess, " is too low")
    elif guess > secret_number and guess <= 10:
        print(guess, " is too high")
    else:
        print("Invalid number. Type a number between 1 and 10")
