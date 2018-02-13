phonebook_dict = {
  "Alice": "703-493-1834",
  "Bob": "857-384-1234",
  "Elizabeth": "484-584-2923"
}

print(phonebook_dict["Elizabeth"])  # prints Elizabeth's number

phonebook_dict["Kareem"] = "938-489-1234" #Adds an entry for Kareem

del phonebook_dict["Alice"]   # Delete's Alice's phone entry

phonebook_dict["Bob"] = "968-345-2345"  # Changes Bob's number

print(phonebook_dict) # Prints phone entries