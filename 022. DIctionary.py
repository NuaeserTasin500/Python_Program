## Dictionary
# in dictionary, there are two things which are keys and values
# keys are written in left, and their values are written in right
# "Name": "John", here "Name" is a key, "John" is a value

information = {
    "Name": "John",
    "Country": "United Kingdom",
    "Age": 21
}

print(information) #prints whole dictionary
print(information["Name"]) #prints 'John'
print(information["Country"]) #prints 'United Kingdom'
print(information["Age"]) #prints '21'
print()
#better is, using get method
print(information.get('Name')) #prints 'John'
print(information.get('Hobby')) #prints 'None'
print()

#printing all keys
for x in information.keys():
    print(x) 
print()


#print key and value by for loop
for key, value in information.items():
    print(key, ":", "value")
print()

#update dictionary
info2 = {
    "Name": "John",
    "Country": "Ireland",
    "Age": 22
}
information.update(info2)
print(information) #prints info2
print()

#clear dictionary
information.clear()
print(information) #prints {}
print()


#remove key-value pair from dictionary
info2.pop('Age')
print(info2) #prints info2 without "Age": 22
print()



