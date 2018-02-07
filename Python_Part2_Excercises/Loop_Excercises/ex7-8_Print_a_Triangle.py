rows = int(input("Enter number of rows: "))
blanks = rows - 1
asterisk = 1

i = 0

while i < rows:
    print("  " * blanks, "* " * asterisk)
    asterisk += 2
    blanks -= 1
    i += 1
