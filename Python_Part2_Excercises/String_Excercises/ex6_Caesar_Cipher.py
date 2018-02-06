cipher1 = "ABCDEFGHIJKLM "
cipher2 = "NOPQRSTUVWXYZ "

secretMessage = input("Enter secret message to decipher: ")

decryptMessage = ""

for char in secretMessage:
    charLocation1 = cipher1.find(char.upper())
    charLocation2 = cipher2.find(char.upper())

    if charLocation1 >= 0:
        decryptMessage += cipher2[charLocation1]
    elif charLocation2 >= 0:
        decryptMessage += cipher1[charLocation2]

print(decryptMessage)