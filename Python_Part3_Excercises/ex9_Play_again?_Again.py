def playAgain():
    validAnswer = False
    while validAnswer == False:
        answer = input("Do you want to play again (Y or N)? ").upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("Invalid Input")

print(playAgain())