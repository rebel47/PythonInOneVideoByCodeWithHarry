# #  Print user name with Good afternoon message
# name = input("Enter your name:\n")
# print("Good afternoon", name)

# #Print the given name by adding user name
# name = input("Enter the Candidate Name:\n")
# date = input("Enter the Date:\n")
# letter = '''Dear <|NAME|>,
# You are selected!!

# Date: <|DATE|>'''
# letter = letter.replace("<|NAME|>", name)
# letter = letter.replace("<|DATE|>", date)
# print(letter)

# # WAP to detect double spaces in a string and replace them with single spaces
# story = "hello my  name is  Ayaz  Alam and today  I am going  to learn  Python"
# doubleSpaces = story.find("  ")
# print(doubleSpaces)
# print(story.count("  "))
# print(story.replace("  ", " "))

# Format the given text by using escape sequence
letter = '''Dear Harry, \n\tThis Python course is nice. \nThanks! '''
print(letter)