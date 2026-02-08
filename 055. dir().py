## dir()

#dir() function in Python returns a list of valid attributes and methods for an object.
#We know that, in python, everything is an object.


list1 = [1, 2, 3] #a list
print(dir(list1)) #shows all valid attributes and methods of list
print(list1.__add__) #prints '<method-wrapper '__add__' of list object at 0xsomething>'
print()
tuple1 = (1, 2, 3) #a tuple
print(dir(tuple1)) #shows all valid attributes and methods of tuple
print()
a = 10 #an integer
print(dir(a)) #shows all valid attributes and methods of integer



