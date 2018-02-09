x = 1
y = 2
z = 0
total = y

while z < 4000000:
    z = x + y
    if z % 2 == 0:
        total += z
    x = y
    y = z

print(total)

