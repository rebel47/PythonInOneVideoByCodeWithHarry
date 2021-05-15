# a = "ayaz's" # ---> use this if you have single quotes in your strings

# print(a)

# SLICING

# a = "AyazAlam"
# print(a[0])
# print(a[1])
# print(a[1:3])
# print(a[0:10])
# print(a[::-1])
# print(a[-4:-1])
# print(a[0::1])
# print(a[0::2])
# print(a[0::3])    
# print(a[0::-1])
# print(a[0::-2])
# # Concatenating two strings
# greeting = "Good Morning, "
# name = "Ayaz"
# c = greeting + name
# print(c)

# STRING FUNCTION
story = "Once upon a time there is a boy named Mohd Ayaz Alam who lives in Okhla, Delhi who was learning Python from Code With Harry Youtube channel whose name is Harrish Ali Khan"

print(len(story))
print(story.endswith("notes"))
print(story.endswith("Khan"))
print(story.count("is"))
print(story.capitalize()) #It will only capitalize the first letter in the whole string.
print(story.upper()) #This will capitalize all letters in the given strings.
print(story.lower()) #This will make all the letters lowers in the given strings.
print(story.find("Ayaz"))
print(story.replace("Ayaz", "Josh"))
# Escape Sequence Character
kahani = "Hey guys I am Ayaz and today \nI am going to talk about \t Python\' and only Python\\Python."
print(kahani)