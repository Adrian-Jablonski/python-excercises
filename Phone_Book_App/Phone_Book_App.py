import pickle

phonebook = {}

def menu():

    print("""Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Save entries
    6. Load saved entries
    7. Quit
    """)

def saveEntries():
    # open the file in write mode (wb)
    myfile = open('phonebook.pickle', 'wb')
    # dump the contents of the phonebook into myfile - the open file
    pickle.dump(phonebook, myfile)
    # close myfile
    myfile.close()

def loadEntries():
    global phonebook # declared global to update dictionary
    # open the file in read mode (rb)
    myfile = open('phonebook.pickle', 'rb')
    # load the contents from the file and store it in the phonebook variable
    phonebook = pickle.load(myfile)
    myfile.close()    

menu()
entry = int(input("What do you want to do (1-7)? "))

while entry != 7:
    if entry == 1:
        personName = input("Name: ")
        print("Found entry for", personName, ":", phonebook[personName])

    elif entry == 2:
        personName = input("Name: ")
        phoneNumber = input("Phone Number: ")

        phonebook[personName] = phoneNumber
        print("Entry stored for", personName)

    elif entry == 3:
        personName = input("Name: ")
        del phonebook[personName]

    elif entry == 4:
        for key, value in phonebook.items():
            print("Found entry for {}: {}".format(key, value))

    elif entry == 5:
        saveEntries()
        print("Entries saved to phonebook.pickle")

    elif entry == 6:
        loadEntries()
        print("Restored saved entries")

    else:
        print("Invalid Entry")

    menu()
    entry = int(input("What do you want to do (1-7)? "))