# # WAP to create a dictionary of hindi words translation in english with option to user to look it up!
# hindi_Dict = {
#     "Badboo": "Smell",
#     "Dost": "Friend",
#     "Angoor": "Grapes",
#     "Aadmi": "Man",
#     "Kitaab": "Book"
# }

# print("Options are", hindi_Dict.keys())
# a = input("Enter the word: ")
# # print("Meaning of Word in English", hindi_Dict[a])
# # Below this will not show error if word is not present
# print("Meaning of the word: ", hindi_Dict.get(a))

# # WAP to take eight input from users and display the unique number 

# n1 = int(input("Enter the Number 1: "))
# n2 = int(input("Enter the Number 2: "))
# n3 = int(input("Enter the Number 3: "))
# n4 = int(input("Enter the Number 4: "))
# n5 = int(input("Enter the Number 5: "))
# n6 = int(input("Enter the Number 6: "))
# n7 = int(input("Enter the Number 7: "))
# n8 = int(input("Enter the Number 8: "))

# unique = {n1, n2, n3, n4, n5, n6, n7, n8}
# print(unique)


# # Can we have 18 as int and 18 as str in a set

# same = {18, "18"}
# print(same)
# print(type(same))
# # Answer is Yes we can have 18 as int and 18 as str in a same set


# # What will we the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))


# # What is type of s? : Answer is Dictionary
# s = {}
# print(type(s))


# # Creat a empty dictionary, allow four friends to enter their favourite language as values and use keys as their names, Assume that the names are unique.
# friend_Dict = {}
# a = input("Enter your favorite language Divya: ")
# b = input("Enter your favorite language Owaimir: ")
# c = input("Enter your favorite language Athar: ")
# d = input("Enter your favorite language Sharukh: ")

# friend_Dict['Divya'] = a
# friend_Dict['Owaimir'] = b
# friend_Dict['Athar'] = c
# friend_Dict['Sharukh'] = d

# print(friend_Dict)



# #If the names of two friends are same then what will happened:

# friend_Dict = {}
# a = input("Enter your favorite language Divya: ")
# b = input("Enter your favorite language Owaimir: ")
# c = input("Enter your favorite language Athar: ")
# d = input("Enter your favorite language Divya: ")

# friend_Dict['Divya'] = a
# friend_Dict['Owaimir'] = b
# friend_Dict['Athar'] = c
# friend_Dict['Divya'] = d #As you can now we have two Divya, so in that case the latest value of Divya will be stored.

# print(friend_Dict)


# # If the language of the two friend are same then what will happened:
# friend_Dict = {}
# a = input("Enter your favorite language Divya: ")
# b = input("Enter your favorite language Owaimir: ")
# c = input("Enter your favorite language Athar: ")
# d = input("Enter your favorite language Sharukh: ")

# friend_Dict['Divya'] = a
# friend_Dict['Owaimir'] = b
# friend_Dict['Athar'] = c
# friend_Dict['Sharukh'] = d
# # So if value of two or more than two keys are same then there will be no issue it will print the same value without any changes, Value can be same.
# print(friend_Dict)


# Can you change the values inside a list which is contained in set s

# s = {8, 7, 12, "Harry", [1, 2] } #first it is wrong set we can't put list is set