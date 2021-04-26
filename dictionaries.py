#Dictionaries are the  datastructures of key  value pair
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
#print(phonebook)

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

phonebook.pop("John")
print(phonebook)
#removing item using del or pop