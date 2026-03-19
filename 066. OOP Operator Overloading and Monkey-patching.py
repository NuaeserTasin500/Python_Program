## OOP Operator Overloading and Monkey-patching <AI>

# =========================================================================== #

# OOP Operator Overloading
#In Python Programming, operator overloading is a special technique that allows to redefine the behavior of mathematical and comparison operators for custom data types

#Suppose, we want to make vector operator, where we can do addition and subtraction of vector objects
#for example, a = 4i + 6j + 10k and b = 2i + 3j + 5k, now python has no vector operator that you can calculate a + b or a - b
#That's why we will use operator overloading
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k 
    
    #for printing value, we need to use __str__() dunder method
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k" #this is naturally returns vector object
        
    #for addition between two vectors, we need to use "other" for second operand
    #and we need to use __add__() dunder method (this is called operator overloading)
    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k) #returning only string in operator overloading won't be a vector object. So we must use Vector() for returning vector object.
    
    #similarly we will do for subtraction by using __sub__() 
    def __sub__(self, other):
        return Vector(self.i - other.i, self.j - other.j, self.k - other.k)

# Now let's test 
a = Vector(4, 6, 10) #a = 4i + 6j + 10k 
b = Vector(2, 3, 5) #b = 2i + 3j + 5k
print(a)
print(b)
print(type(a)) #shows that 'a' is a vector object
print(type(b)) #shows that 'b' is a vector object
c = a + b
d = a - b
print(c)
print(d)
print(type(c)) #shows that 'c' is a vector object
print(type(d)) #shows that 'd' is a vector object
print()

#Here __add__() and __sub__() dunder methods help to do + and - between two objects outside the public class
#__add__() works as object1 + object2
#__sub__() works as object1 - object2
#Other operator overloading dunder methods are
#
#__mul__() works as object1 * object2
#__truediv__() works as object1 / object2
#__mod__() works as object1 % object2
#__floordiv__() works as object1 // object2
#__pow__() works as object1 ** object2


# =============================================================== #

# OOP Monkey-patching <AI>
#we have seen that, when we are printing the type of vector object, it shows <class '__main__.Vector'>
#but we want to show it as <class 'vector'> or <class 'Vector>
#for doing these, we need to do monkey patching

Vector.__module__ = "builtins"  
Vector.__name__ = "vector"

#now it will show as <class 'vector'>
print(type(a)) #prints '<class 'vector'>'

Vector.__module__ = "builtins"  
Vector.__name__ = "Vector"

#now it will show as <class 'Vector'>
print(type(a)) #prints '<class 'Vector'>'

#we can change module name too
Vector.__module__ = "abcd"  
Vector.__name__ = "Vector"
print(type(a)) #prints '<class 'abcd.Vector'>'
