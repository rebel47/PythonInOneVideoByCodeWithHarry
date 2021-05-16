# myDict = {
#     "Fast": "In a quick manner",
#     "Ayaz": "A Developer/Hacker",
#     "Mark": [1, 2, 4],
#     "anotherdict": {'ayaz': 'Player'}
# }
# print(myDict)
# print(myDict['Fast'])
# print(myDict['Ayaz'])
# print(myDict['Mark'])
# print(myDict['anotherdict']['ayaz'])

# We change the value of any key
# myDict['Mark'] = [89,79]
# print(myDict['Mark'])


# METHODS IN DICTIONARY
myDict = {
    "Fast": "In a quick manner",
    "Ayaz": "A Developer/Hacker",
    "Mark": [1, 2, 4],
    "anotherdict": {'ayaz': 'Player'},
    1:2
}

# print(myDict.keys()) # Print the all keys in myDict

# print(type(myDict.keys())) #Print the type of myDict keys
# print(list(myDict.keys())) #Prints the keys of the dictionary

# print(myDict.values()) #Prints the values of the dictionary
# print(list(myDict.values())) #Prints the values of the dictionary

# print(myDict.items()) # Prints the (keys, values) for all contents of the dictionary

updateDict ={
    "Divya": "Friend",
    "Shrey": "A dancer",
    "Owaimir": "Friend",
    "Athar": "Friend",
}
myDict.update(updateDict) #Updates the dictionary by adding key-values pairs form updateDict
print(myDict)

print(myDict.get("Shrey")) # Prints value associated with key "Shrey"
print(myDict["Shrey"]) # Prints value associated with key "Shrey"

# The difference between .get() and [] syntax in Dictionaries 
print(myDict.get("Shrey2")) # Returns NONE as Shrey2 is not present in the dictionary
print(myDict["Shrey2"]) # throws an error as Shrey2 is not present in the dictionary

