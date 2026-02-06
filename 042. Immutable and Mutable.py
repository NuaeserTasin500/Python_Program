## Immutable and Mutable

# Immutable Objects
#In Python programming, immutable objects are those which can't be changed after creation.
#Int, Str (String), Float, Tuple, Bool (Boolean), Frozenset, Byte, None - these are immutable objects

a = 5 #this is an immutable object

#Now you might think that if we make a = 1, then a's value would be changed which would look like it would clash the definition of immutable.
#Well, that's not how we can define immutable. We can define that by id() function

print(a) #prints '5'
print(id(a)) #prints the memory address of 'a'
a = 1 #changing value of a as 1
print(a) #prints '1'
print(id(a)) #prints different memory address of 'a'
print()
#It means that changing value of an immutable object causes the changing of memory address 
#That's why, immutable objects are considered as unchangable objects 




# Mutable Objects
#In Python programming, mutable objects are those which can be changed after creation.
#List, Dict (Dictionary), Set - these are mutable objects

b = [1, 2, 3, 4] #this is a mutable object
print(b) #prints '[1, 2, 3, 4]'
print(id(b)) #prints the memory address of 'b'
b.append(5) #changing value of b as [1, 2, 3, 4, 5]
print(b) #prints '[1, 2, 3, 4, 5]'
print(id(b)) #prints same memory address of 'b'
#It means that changing value of an mutable object never cause the changing of memory address 
#That's why, mutable objects are considered as changable objects 
