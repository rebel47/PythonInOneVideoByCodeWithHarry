a = {1, 2, 3, 4, 5, 1 ,2}
print(a) # Sets do not show the repetitive elements
print(type(a))


# Important: This syntac will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set can be created by using the below syntax:
b = set()
print(type(b))
# Adding values to an empty set
b.add(4)
b.add(6)
b.add(7)
b.add(65)
b.add(4) # This will be not print since sets is collection of non repetitive elements
# b.add([4, 5, 6]) # This will show an error since list can be change same apply for dictinary 
b.add((8, 9, 10)) # wherease tuple can be added since it is also immutable

print(b)

print(len(b)) # Prints the length of the set

b.remove(4) # Removes 4 from the set b
# b.remove(15)# throws an error while tyring to remove 15(which is not present in the set)
print(b)

print(b.pop())# Remove any arbitary element from the set b
print(b)

b.clear() #This will clear all the elements from the set
print(b)

c = {12, 6, 7, 76, 89}
c.intersection()
print(c)
c.union()
print(c)
