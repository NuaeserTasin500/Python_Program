## Modification vs Assignment in Mutable object <AI>
#In Python programming, we have known that changing value of a mutable object never cause the changing of memory address
#But if the change of value is happened by modification, then memory address won't be changed
#And if the change of value is happened by assignment, then memory address will change


# Modification
a = [1, 2, 3, 4] 
print(id(a)) #prints memory address of 'a'
a.append(10) #modified to make a = [1, 2, 3, 4, 10]
print(id(a)) #prints same memory address
print()
#It means modification of a mutable object never change memory address



# Assignment
b = [10, 11, 13, 17]
print(id(b)) #prints memory address of 'b'
b = [20, 22, 23, 29] #assignment to make b = [20, 22, 23, 29]
print(id(b)) #prints different memory address of 'b'
print()
#It means assignment of a mutable object can change memory address
