def playAgain():
    answer = input("Do you want to play again (Y or N)? ").upper()
    if answer == "Y":
        return True
    else:
        return False

print(playAgain())