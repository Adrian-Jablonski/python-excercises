import random
validNumber = False
gameOver = False
guessNumber = 1
minNumber = 0
maxNumber = 100
playAgain = ""

while gameOver == False:
    #Asks user for a number for the computer to guess
    while validNumber == False:
        try:
            secret_number = int(input("Enter a number between 0 - 100: "))
            if secret_number >= 0 and secret_number <= 100:
                validNumber = True
            else:
                print("Invalid Number. Input a number from 0 - 100")
        except ValueError:
            print("Invalid input. Enter a number")

    # generate guess for PC by guessing first three numbers by splitting possibilities 
    #in half. Then alternates between a random guess and a split guess
    if (guessNumber % 2 != 0 and guessNumber >=2) or guessNumber <= 3:
        guess = int((maxNumber + minNumber) / 2)  
    else:
        guess = random.randint(minNumber, maxNumber)
    
    # checks if guess is correct
    if secret_number == guess:
        gameOver = True
        guessDirection = "Correct"
    elif guess > secret_number:
        guessDirection = "Too high"
        maxNumber = guess - 1
    elif guess < secret_number:
        guessDirection = "Too low"
        minNumber = guess + 1

    print(guess ,"is", guessDirection)

    if gameOver == True:
        print("The computer took", guessNumber, "times to guess correctly")
        validInput = False
        while validInput == False:
            playAgain = input("Play again? (Y/N): ").upper()
            # resets game if user types in Y
            if playAgain == "Y":
                validNumber = False
                gameOver = False
                guessNumber = 0
                minNumber = 0
                maxNumber = 100
                validInput = True
            elif playAgain == "N":
                print("Bye!")
                validInput = True
            else:
                print("Invalid input. Type Y or N")

    guessNumber += 1