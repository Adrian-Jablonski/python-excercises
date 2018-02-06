paragraph = input("Type in a paragraph to translate to leetspeak ")

leetspeak = ""

c = 0

for char in paragraph:
    if char.upper() == "A":
        leetspeak += "4"
    elif char.upper() == "E":
        leetspeak += "3"
    elif char.upper() == "G":
        leetspeak += "6"
    elif char.upper() == "I":
        leetspeak += "1"
    elif char.upper() == "O":
        leetspeak += "0"
    elif char.upper() == "S":
        leetspeak += "5"
    elif char.upper() == "T":
        leetspeak += "7"
    else:
        leetspeak += char
    
    c += 1

print(leetspeak)
