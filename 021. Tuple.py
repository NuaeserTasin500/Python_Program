## Tuples
# Tuple is an unchangeable list

tuple1 = (1, 2, 3)
print(tuple1)
print(type(tuple1))
print(len(tuple1))

# tuple supports different type of elements
tuple1 = (1, 2, 3, "green", 4.5)
print(tuple1)
print()

# getting every elements of a tuple by indexing
tuple1 = (4, 5, 6, 8)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print()

# element manipulation
if 4 in tuple1:
    print("Yes") #obviously prints "Yes" because 4 is in tuple1
else:
    print("No")
print()

#using for loop for printing all elements of a tuple
department = ('CSE', 'EEE', 'ME', 'BBA')
for x in department:
    print(x) 
print()

#indexing
print(department[:]) #prints whole list with all elements
print(department[:3]) #prints ('CSE', 'EEE', 'ME') 
print(department[::2]) #prints ('CSE', 'ME'), here 2 is jump index like i = i+2
print()

