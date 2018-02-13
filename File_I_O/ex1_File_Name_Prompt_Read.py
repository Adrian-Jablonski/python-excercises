userFile = input("Enter a file name to open and read: ")

try:
    file_handle = open(userFile, "r")
    contents = file_handle.read()
    file_handle.close()
    print(contents)

except FileNotFoundError:
    print("File does not exist")