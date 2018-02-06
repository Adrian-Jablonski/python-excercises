billAmount = int(input("Enter total bill amount: "))

stop = False

while stop == False: 
    levelOfService = input("How was the service? Enter good, fair, or bad: ").lower()
    if levelOfService == "good" or levelOfService == "fair" or levelOfService == "bad":
        stop = True

if levelOfService == "good":
    tipAmount = .2
elif levelOfService == "fair":
    tipAmount = .15
elif levelOfService == "bad":
    tipAmount = .1

split = int(input("Split how many ways: "))

totalBill = billAmount * (1 + tipAmount)
totalBillPerPerson = totalBill / split

print("Tip Amount: ", "${:.2f}".format(billAmount * tipAmount))
print("Total Amount: ", "${:.2f}".format(totalBill))
print("Amount per person: ", "${:.2f}".format(totalBillPerPerson))