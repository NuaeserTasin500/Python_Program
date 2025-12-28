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

# converting tuple into list
countries = ('Australia', 'Afghanistan', 'New Zealand', 'Bangladesh')
list_countries = list(countries)
print(countries, "is a tuple")
print(list_countries, "is a list")
print()

# converting list into tuple
oceania = ['Australia', 'New Zealand', 'Papua', 'Niue', 'Cook Island', 'Tuvalu', 'Fiji']
tup_oceania = tuple(oceania)
print(oceania, "is a list")
print(tup_oceania, "is a tuple")
print()


# this is how we can change values, add, remove in tuple 
southEastAsia = ('Myanmar', 'China', 'Laos', 'Vietnam', 'Indonesia', 'Malaysia', 'Cambodia', 'Brunei', 'America')
print("Wrong South East Asia Tuple =", southEastAsia)
temp = list(southEastAsia)
temp[1] = 'Thailand'
temp.append('East Timor')
temp.remove('America')
southEastAsia = tuple(temp)
print("Correct South East Asia Tuple =", southEastAsia)
print()

#count elements
num = (4, 5, 6, 4, 7, 5, 4, 0, 6, 5, 4)
print(num)
print("In this tuple, 4 occurs", num.count(4), "times")
print("In this tuple, 5 occurs", num.count(5), "times")
print("In this tuple, 6 occurs", num.count(6), "times")
print("In this tuple, 7 occurs", num.count(7), "times")
print()

#get index by elements
tuple4 = (1, 2, 3, 4, 5, 6)
print(tuple4.index(4))
tuple5 = (4, 5, 6, 4, 7, 5, 4, 0, 6, 5, 4)
print(tuple5.index(6, 4, len(tuple5))) #index(element, start, end)

