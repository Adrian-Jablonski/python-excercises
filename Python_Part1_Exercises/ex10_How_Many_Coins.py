coins = 0
run = True

while run == True:
    print("You have ", coins, "coins.")
    answer = input("Do you want another? yes or no? ").lower()
    if answer == "yes":
        coins += 1
    elif answer == "no":
        run = False

