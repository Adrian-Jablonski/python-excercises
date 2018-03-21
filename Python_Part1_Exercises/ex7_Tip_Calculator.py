billAmount = int(input("Enter total bill amount: "))

stop = False

while stop == False: 
    levelOfService = input("How was the service? Enter good, fair, or bad ").lower()
    if levelOfService == "good" or levelOfService == "fair" or levelOfService == "bad":
        stop = True

if levelOfService == "good":
    tipAmount = .2
elif levelOfService == "fair":
    tipAmount = .15
elif levelOfService == "bad":
    tipAmount = .1

print("Tip Amount: ", "${:.2f}".format(billAmount * tipAmount))
print("Total Amount: ", "${:.2f}".format(billAmount * (1 + tipAmount)))