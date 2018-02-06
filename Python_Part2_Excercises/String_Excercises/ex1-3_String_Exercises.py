string = "hello world"
print(string.upper())   #Makes each letter in the word uppercase
print(string.title())   #Capitalizes first letter of each word


strLen = len(string) - 1
newStr = string[strLen]

while strLen > 0:
    strLen -= 1
    newStr += string[strLen]    #reverses a string

print(newStr)


