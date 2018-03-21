width = int(input("Width? "))
height = int(input("Height? "))

i = 0

while i < height:
    if i == 0 or i == height - 1:
        print("* " * width)
    else:
        print("* ", "  " * (width - 3), "* ")
    i += 1