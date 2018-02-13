userFile = input("Enter a file name to open and read: ")
userContent = input("Enter the content of the file: ")

file_handle = open(userFile, "w")
file_handle.write(userContent)
file_handle.close()

