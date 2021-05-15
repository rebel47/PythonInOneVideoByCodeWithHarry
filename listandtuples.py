# # Print the list using []
# a = [18,26,33,64,598,69,76,82,93,3410,45,1234,76]

# #  Print the list using print() function
# print(a)

# # Access using index using a[0], a[1], a[2]
# print(a[0])
# print(a[1])
# print(a[2])
# # If try to find any index value which does not exist then it will show error

# # Update any index value
# a[0] = 54 #You can update any index value like this
# print(a)

# # We can create the list with items of differnt datatypes
# c = [54, "Ayaz", True, 43.3]
# print(c)

# # List Slicing
# friends = ["Harry", "Divya", "Rohan", "Ayaz", "Shraddha", "Akash", 45]
# print(friends[0:4])
# print(friends[-4:])

# List Methods
# lmethod = [2, 16, 7, 9, 12, 14]
# print(lmethod)
# lmethod.sort() # this will sort the list
# print(lmethod)
# lmethod.reverse() # this will reverse the list
# print(lmethod)
# lmethod.append(10) # this will add the data at the end of the list
# print(lmethod)
# lmethod.insert(2,43) # the first value is the index number and the second one is the value that you want to add
# print(lmethod)
# lmethod.remove(16) # this will remove 16 from the list
# print(lmethod)
# lmethod.pop(2)# this will remove the value at index 2
# print(lmethod)


'''******************TUPLES******************'''
# # Creating the tuples
# t = (1, 2, 3, 4, 5)
# # Printing the tuples
# print(t[0])
# print(t[2])
# print(t[3])

# # Cannot update the value of tuples its immutable datatype in python
# t[0] = 68 # throws an error

# t1 = () # empty tuples
# t2 = (1,)# tuples with single element need comma
# t3 = (1, 2, 3, 4, 5) #tuples with more than one element

# Methods in Tuples
t = (1, 2, 3, 4, 5, 1, 1, 1)
print(t.count(1)) #count the number of 1 in the tuples
print(t.index(4))# find the index value of the given number