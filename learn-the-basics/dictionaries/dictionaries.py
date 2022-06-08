phonebook = {}
phonebook["Claudio"] = 984500932
phonebook["Ricardo"] = 885939389
phonebook["Fernando"] = 985284920
print(phonebook)

phonebook1 = {
    "Claudio": 984500932,
    "Ricardo": 885939389,
    "Fernando": 985284920
}
print(phonebook1)

#iterating
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#removing item
del phonebook["Ricardo"]
print(phonebook)

phonebook1.pop("Claudio")
print(phonebook1)