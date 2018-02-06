import random

secret_number = random.randint(1, 10)
guesses_left = 5

game_over = False

print("I am thinking of a number between 1 and 10")
print("You have ", guesses_left, "  guesses left.")

while game_over == False:
    guess = int(input("What's the number? "))
    if guess == secret_number:
        print("Yes! You win!")
    elif guess < secret_number and guess >= 1:
        print(guess, " is too low")
        guesses_left -= 1
    elif guess > secret_number and guess <= 10:
        print(guess, " is too high")
        guesses_left -= 1
    else:
        print("Invalid number. Type a number between 1 and 10")

    if guesses_left == 0:
        print("You ran out of guesses")
    elif guess != secret_number :
        print("You have ", guesses_left, "  guesses left.")
    
    if guesses_left == 0 or guess == secret_number:
        play_again = input("Would you like to play again? (Y or N) ").lower()
        if play_again == "n":
            print("Bye!")
            game_over = True
        elif play_again == "y":
            print("I am thinking of a number between 1 and 10")
            secret_number = random.randint(1, 10)
            guesses_left = 5
            print("You have ", guesses_left, "  guesses left.")
