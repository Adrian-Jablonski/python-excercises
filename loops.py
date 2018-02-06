count = 0

while count < 10:
    count += 1
    print("The count is", count)

print("Done")

answer = ''
while answer not in ["y", "n"]:
  answer = input('Say [y/n]')
  answer = answer.lower()
print("Cheese")

while True:
  answer = input('Say when: ')
  if answer.lower() == 'when':
    break
print("Cheese")