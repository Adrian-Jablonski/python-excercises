import json
import matplotlib.pyplot as plot

jsonFile = input("Type in JSON file to import: ")

x = []; y = []

with open(jsonFile, 'r') as fh:
  contents = json.load(fh)


contentsLen = len(contents['data'])

i = 0
while i < contentsLen:
  x.append(contents['data'][i][0])
  y.append(contents['data'][i][1])
  i += 1

plot.plot(x, y)
plot.show()