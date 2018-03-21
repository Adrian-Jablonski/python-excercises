import matplotlib.pyplot as plot

def f(x):
    return x * 1.8 + 32

xs = list(range(-20, 40))
ys = []
for x in xs:
    ys.append(f(x))

plot.xlabel("Celcius")
plot.ylabel("Fahrenheit")
plot.grid(True)
plot.plot(xs, ys)
plot.show()