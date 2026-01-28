## 'is' vs '=='
#In Python programming, is and == are used as comparison operators for checking two values are same or not.
#But there are difference between 'is' and '=='
#'is' is used for exact location of object in memory
#'==' is used for same value 
#'is' will return true if the object being compared are the same object in memory
#'==' will return true if the object have the same data

a = 5
b = 5
bool1 = (a is b)
bool2 = (a == b)
print(bool1) #prints 'True'
print(bool2) #prints 'True'
print()

#For immutable objects (i.e. int, float, complex, bool etc.), 'is' and '==' always return same result
#That's why 'a is b' and 'a == b' both returns 'True' because a and b are immutable


# For Mutable objects (i.e. list, set etc), 'is' and '==' return different result
c = [1, 2, 3]
d = [1, 2, 3]
bool3 = (c is d)
bool4 = (c == d)
print(bool3) #prints 'False'
print(bool4) #prints 'True'
print()
