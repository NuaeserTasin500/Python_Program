## Dunder Methods and Dunder Attributes <AI>
#Source: https://www.pythonmorsels.com/every-dunder-method/#cheat-sheet

# ======================================================================= #


## Dunder Methods <AI>
#Dunder methods, also known as magic methods or special methods, are built-in methods in Python that have double underscores (dunder) at the beginning and end of their names


# .__repr__()
#it returns string
x = 10
y = x.__repr__()
print(y) #prints '10'
print(type(y)) # y is a string 
print()



# .__eq__()
#it returns True if values of two objects are equal, otherwise False or NotImplemented 
# NotImplemented happens when objects can't be compared
x1 = 10
x2 = 10
x3 = 11
x4 = "Hello"
bool1 = x1.__eq__(x2) #x1.__eq__(x2) means x1 == x2
bool2 = x1.__eq__(x3) #x1.__eq__(x3) means x1 == x3
bool3 = x1.__eq__(x4) #x1.__eq__(x4) means x1 == x4
print(bool1) #prints 'True' because values of x1 and x2 are equal
print(bool2) #prints 'False' because values of x1 and x3 are not equal
print(bool3) #prints 'NotImplemented' because x1 is an integer where x4 is a string
print()



# .__ne__()
#it returns True if values of two objects are not equal, otherwise False or NotImplemented 
# NotImplemented happens when objects can't be compared
x1 = 10
x2 = 10
x3 = 11
x4 = "Hello"
bool1 = x1.__ne__(x2) #x1.__ne__(x2) means x1 != x2
bool2 = x1.__ne__(x3) #x1.__ne__(x3) means x1 != x3
bool3 = x1.__ne__(x4) #x1.__ne__(x4) means x1 != x4
print(bool1) #prints 'False' because values of x1 and x2 are equal
print(bool2) #prints 'True' because values of x1 and x3 are not equal
print(bool3) #prints 'NotImplemented' because x1 is an integer where x4 is a string
print()



# .__lt__(), .__gt__(), .__le__(), .__ge__()
#.__lt__() works as < (less than), returns 'True' if first object's value is less than second object's value.
#.__gt__() works as > (greater than), returns 'True' if first object's value is greater than second object's value.
#.__le__() works as >= (less than or equal), returns 'True' if first object's value is less than or equal second object's value.
#.__ge__() works as <= (greater than or equal), returns 'True' if first object's value is greater than or equal second object's value.
#there is 'NotImplemented' issue in these, which means they will raise error if both object types are different.  
x5 = 24
x6 = 33
x7 = 24
bool5 = x5.__lt__(x6) #x5.__lt__(x6) means x5 < x6
bool6 = x5.__le__(x7) #x5.__le__(x7) means x5 <= x6
bool7 = x6.__gt__(x5) #x6.__gt__(x5) means x6 > x5
bool8 = x6.__ge__(x5) #x6.__ge__(x5) means x6 >= x5
bool9 = x5.__gt__(x6) #x5.__gt__(x6) means x5 > x6
print(bool5) #prints 'True' because x5's value is less than x6's value
print(bool6) #prints 'True' because x5's value is less than or equal x7's value
print(bool7) #prints 'True' because x6's value is less than x5's value
print(bool8) #prints 'True' because x6's value is less than or equal x5's value
print(bool9) #prints 'False' because x5's value is not greater than x6's value
print()



# .__str__(), .__bool__(), .__int__(), .__float__()
#these are dunder methods working as str(), bool(), int(), float()
#these are type conversion dunder methods
y1 = 110
y2 = y1.__str__() #it means y2 = str(y1)
print(y2) #prints '110'
print(type(y2)) #y2 is a string
y3 = 120
y4 = 115.545
y5 = y3.__float__() #means y5 = float(y3)
y6 = y4.__int__() #means y6 = int(y4)
print(y5) #prints '120.0'
print(y6) #prints '115'
#you can't do x.__int__() when x = "120" because __int__() can't convert string number to integer
y7 = 1
y8 = 0
bool10 = y7.__bool__() #means bool10 = bool(y7)
bool11 = y8.__bool__() #means bool11 = bool(y8)
print(bool10) #prints 'True'
print(bool11) #prints 'False'
print()



# .__format__() <AI>
#Works as format specification mini-language for space
name = 'John'
s = ""
str_name = name.__format__(s)
print(f"His name is {str_name}") #prints "His name is John"
#We can use "s" for string
name1 = 'Rachel'
s_name = name1.__format__("s")
print(f"Her name is {s_name}") #prints "Her name is Rachel"
#We can use __format__() directly
print(f"{name1.__format__("s")} is going to school")

#"d" — for integers
#"f" — for floating-point values
#"e" — for floating-point exponent
#"E" — for floating-point exponent (uppercase)
#"%" — Percentage (multiplies by 100 and adds %).
#"x" — Hexadecimal (base 16, lowercase).
#"X" — Hexadecimal (base 16, uppercase).
#"b" — Binary (base 2, unsigned).
#"#b" — Binary (base 2, signed).
#"o" — Octal (base 8).
float_num = 0.3
int_num = 200
exponent_num = 1e10
print(f"The percentage of {float_num.__format__(".2f")} is {float_num.__format__("%")}") #prints 'The percentage of 0.30 is 30.000000%'
print(f"The lower hexadecimal value of {int_num.__format__("d")} is {int_num.__format__("x")}") #prints 'The lower hexadecimal value of 200 is c8'
print(f"The upper hexadecimal value of {int_num.__format__("d")} is {int_num.__format__("X")}") #prints 'The upper hexadecimal value of 200 is C8'
print(f"The unsigned binary value of {int_num.__format__("d")} is {int_num.__format__("b")}") #prints 'The unsigned binary value of 100 is 1100100'
print(f"The signed binary value of {int_num.__format__("d")} is {int_num.__format__("#b")}") #prints 'The signed binary value of 100 is 0b1100100'
print(f"The octal value of {int_num.__format__("d")} is {int_num.__format__("o")}") #prints 'The octal value of 200 is 310'
print(f"The exponential of 10000000000 is {exponent_num.__format__("e")}") #prints 'The exponential of 10000000000 is 1.000000e+10'
print(f"The exponential of 10000000000 is {exponent_num.__format__("E")}") #prints 'The exponential of 10000000000 is 1.000000E+10'

#we can directly use value in Format Specification Mini-Language.
print(f"The value of PI is {(3.1416).__format__(".4f")}") #prints 'The value of PI is 3.1416'
print()
#Now this format specification has some methods
#'<' Forces the field to be left-aligned within the available space (this is the default for most objects).
#'>' Forces the field to be right-aligned within the available space (this is the default for numbers).
#'=' Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types, excluding complex. It becomes the default for numbers when ‘0’ immediately precedes the field width.
#'^' Forces the field to be centered within the available space. 
#'+' Indicates that a sign should be used for both positive as well as negative numbers.
#'-' Indicates that a sign should be used only for negative numbers (this is the default behavior).
#<space> Indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.
#',' Inserts a comma every 3 digits for integer presentation type 'd' and floating-point presentation types, excluding 'n'. For other presentation types, this option is not supported.
#'_' Inserts an underscore every 3 digits for integer presentation type 'd' and floating-point presentation types. For integer presentation types 'b', 'o', 'x', and 'X', underscores are inserted every 4 digits. For other presentation types, this option is not supported.
str1 = 'World'
int1 = -120
theta1, theta2 = -3, 7
balance = 1000000
accurate_lightspeed = 299792458
print(f"Hello {str1.__format__("<8")}. How are you?") #prints 'Hello World   . How are you?'
print(f"Hello {str1.__format__(">8")}. How are you?") #prints 'Hello    World. How are you?'
print(f"{int1.__format__("=8")}") #prints '-    120'
print(f"This {str1.__format__("^12")} is good") #prints 'This    World     is good'
print(f"The temperature is between {theta1.__format__("+")} and {theta2.__format__("+")} degrees celsius.") #prints 'The temperature is between -3 and +7 degrees celsius.'
print(f"The temperature is between {theta1.__format__("-")} and {theta2.__format__("-")} degrees celsius.") #prints 'The temperature is between -3 and 7 degrees celsius.'
print(f"The temperature is between {theta1.__format__(" ")} and {theta2.__format__(" ")} degrees celsius.") #prints 'The temperature is between -3 and  7 degrees celsius.'
print(f"My bank balance is {balance.__format__(",")} BDT") #prints 'My bank balance is 1,000,000 BDT'
print(f"Light speed is {accurate_lightspeed.__format__("_")}") #prints 'Light speed is 299_792_458'
print()



# .__len__()
str2 = "Hello Everyone"
len2 = str2.__len__()
print(len2) #prints '14'
print


# .__iter__() and .__next__()
#.__iter__() works as iter()
#.__next__() works as next()
list1 = [1, 2, 3]
iter1 = list1.__iter__()
print(iter1.__next__()) #prints '1'
print(iter1.__next__()) #prints '2'
print(iter1.__next__()) #prints '3'
print()



# .__getitem__(), .__setitem__() and .__delitem__()
#.__getitem__() works as x[index]
#.__setitem__() works as x[index] = assign_value
#.__delitem__() works for delete the element
list2 = [10, 20, 30, 40, 50]
print(list2.__getitem__(0)) #prints '10'; list2[0]
print(list2.__getitem__(1)) #prints '20'; list2[1]
print(list2.__getitem__(2)) #prints '30'; list2[2]
list2.__setitem__(1, 60) #list2[1] = 60
list2.__setitem__(2, 70) #list2[2] = 70
list2.__setitem__(3, 100) #list3[3] = 100
print(list2) #prints '[60, 70, 100, 40, 50]'
print(list2.__getitem__(0)) #prints '60'; list2[0]
print(list2.__getitem__(1)) #prints '70'; list2[1]
print(list2.__getitem__(2)) #prints '100'; list2[2]
list2.__delitem__(0)
print(list2) #prints '[70, 100, 40, 50]'
print()



# .__contains__() and .__reversed__()
list3 = [70, 80, 82, 35, 47]
bool12 = list3.__contains__(70)
bool13 = list3.__contains__(1000)
print(bool12) #prints 'True' because 70 is in list3
print(bool13) #prints 'False' because 1000 is not in list3
list3 = list(list3.__reversed__())
print(list3) #prints '[47, 35, 82, 80, 70]'
list3 = list(list3.__reversed__())
print()



# .__add__(), .__sub__(), .__mul__(), .__truediv__(), .__mod__(), .__pow__(), .__floordiv__() - left side operation
# .__radd__(), .__rsub__(), .__rmul__(), .__rtruediv__(), .__rmod__(), .__rpow__(), .__rfloordiv__ - right side operation
#
#left side operation dunder methods: These methods are invoked when the object appears on the left-hand side of an operator. Python calls them first to attempt the operation.
#obj1.__add__(obj2) → Handles obj1 + obj2
#obj1.__sub__(obj2) → Handles obj1 - obj2
#obj1.__mul__(obj2) → Handles obj1 * obj2
#obj1.__truediv__(obj2) → Handles obj1 / obj2
#obj1.__mod__(obj2) → Handles obj1 % obj2
#obj1.__pow__(obj2) → Handles obj1 ** obj2
#obj1.__floordiv__(obj2) → Handles obj1 // obj2
a1 = 10
b1 = 20
print(a1.__add__(b1)) #prints '30' as a1 + b1 = 10 + 20 = 30
print(a1.__sub__(b1)) #prints '-10' as a1 - b1 = 10 - 20 = -10
print(a1.__mul__(b1)) #prints '200' as a1 * b1 = 10 * 20 = 200
print(a1.__truediv__(b1)) #prints '0.5' as a1 / b1 = 10 / 20 = 0.5
print(a1.__mod__(b1)) #prints '10' as a1 % b1 = 10 % 20 = 10
print(a1.__pow__(b1)) #prints '100000000000000000000' as a1 ** b1 = 10 ** 20 = 100000000000000000000
print(a1.__floordiv__(b1)) #prints '0' as a1 // b1 = 10 // 20 = 0
print()
#right side operation dunder methods: These methods are invoked when the object appears on the right-hand side of an operator, but only if the left-hand side’s method fails or returns NotImplemented. They act as a fallback.
#obj1.__radd__(obj2) → Handles obj2 + obj1 
#obj1.__rsub__(obj2) → Handles obj2 - obj1
#obj1.__rmul__(obj2) → Handles obj2 * obj1
#obj1.__rtruediv__(obj2) → Handles obj2 / obj1
#obj1.__rmod__(obj2) → Handles obj2 % obj1
#obj1.__rpow__(obj2) → Handles obj2 ** obj1
#obj1.__rfloordiv__(obj2) → Handles obj2 // obj1
a1 = 10
b1 = 20
print(a1.__radd__(b1)) #prints '30' as b1 + a1 = 20 + 10 = 30
print(a1.__rsub__(b1)) #prints '10' as b1 - a1 = 20 - 10 = 10
print(a1.__rmul__(b1)) #prints '200' as b1 * a1 = 20 * 10 = 200
print(a1.__rtruediv__(b1)) #prints '2.0' as b1 / a1 = 20 / 10 = 2.0
print(a1.__rmod__(b1)) #prints '0' as b1 % a1 = 20 % 10 = 0
print(a1.__rpow__(b1)) #prints '10240000000000' as b1 ** a1 = 20 ** 10 = 10240000000000
print(a1.__rfloordiv__(b1)) #prints '2' as b1 // a1 = 20 // 10 = 2
print()
#difference between left side operation and right side operation
#for example: x = fraction(1, 2) = 1/2 and y = 2
#x is fraction object and y is integer
#now we exactly want to do y - x = 2 - 1/2 = 3/2 (not x - y = 1/2 - 2 = -3/2) 
#for y.__sub__(x) as working as y - x, it fails because integer doesn't know about fraction in dunder operation
#for x.__sub__(y) as working as x - y, fraction knows about integer in dunder operation but result will be -3/2, not 3/2
#so, using x.__rsub_(y) as y - x; fraction knows about integer in dunder operation and result will be 3/2
import fractions as fr
x = fr.Fraction(1, 2) # x = 1/2
y = 2
print(x) #prints '1/2'
print(y.__sub__(x)) #prints 'NotImplemented' because integer doesn't know about fraction in dunder operation.
print(x.__sub__(y)) #prints '-3/2' but we want 3/2
print(x.__rsub__(y)) #prints '3/2'!
print()
#
#dunder algorithmic operations have limitations, that's why we use right side operation
#there are no limitations in operator signs (+, - etc) in python
#
#we can use these operations without variables:-
print((10).__add__(20)) #prints '30'
ua = 20
print(ua.__sub__(10)) #prints '10'
#also we can store them in a variable
xb = (100).__mul__(2)
xg = (ua.__truediv__(2))
print(xb) #prints '200'
print(xg) #print '10.0'
print()




# .__and__(), .__or__(), .__xor__()  - left side operation 
# .__rand__(), .__ror__(), .__rxor__()  - right side operation
#these are bitwise dunder method operators
#
#obj1.__and__(obj2) → Handles obj1 & obj2
#obj1.__or__(obj2) → Handles obj1 | obj2
#obj1.__xor__(obj2) → Handles obj1 ^ obj2
#obj1.__rand__(obj2) → Handles obj2 & obj1
#obj1.__ror__(obj2) → Handles obj2 | obj1
#obj1.__rxor__(obj2) → Handles obj2 ^ obj1
a = 11 #binary value is 1011
b = 12 #binary value is 1100
print(a.__and__(b)) #prints '8' because 1011 & 1100 = 1001 = 8
print(a.__or__(b)) #prints '15' because 1011 | 1100 = 1111 = 15
print(a.__xor__(b)) #prints '7' because 1011 ^ 1100 = 0111 = 7
print(a.__rand__(b)) #prints '8' because 1100 & 1011 = 8 (a & b = b & a)
print(a.__ror__(b)) #prints '15' because 1100 | 1011 = 15 (a | b = b | a)
print(a.__rxor__(b)) #prints '7' because 1100 ^ 1100 = 7 (a ^ b = b ^ a)
print()



# .__rshift__(), .__lshift__() - left side operation
# .__rrshift__, .__rlshift__() - right side operation
#these are bit-shifting bitwise dunder method operators 
#
#obj1.__rshift__(obj2) → Handles obj1 >> obj2
#obj1.__lshift__(obj2) → Handles obj1 << obj2
#obj1.__rrshift__(obj2) → Handles obj2 >> obj1
#obj1.__rlshift__(obj2) → Handles obj2 << obj1
#
a = 11 # binary of 11 is 1011 [0b1011]
print(a.__rshift__(1)) #prints '5' as a >> 1 = 11 >> 1 = 0b1011 >> 1 = 0b101 = 5
print(a.__lshift__(1)) #prints '22' as a << 1 = 11 << 1 = 0b1011 << 1 = 0b10110 = 22
print((1).__rrshift__(a)) #prints '5' as a >> 1 = 11 >> 1 = 0b1011 >> 1 = 0b101 = 5
print((1).__rlshift__(a)) #prints '22' as a << 1 = 11 << 1 = 0b1011 << 1 = 0b10110 = 22
print()



# .__neg__(), .__pos__(), .__invert__()
#x.__neg__() works as -x
#x.__pos__() works as +x (which is bitwise)
#x.__invert__() works as ~x (which is bitwise)
# 
x = 10
y = -20
print(x.__neg__()) #prints '-10'
print(y.__neg__()) #prints '20'
print(x.__pos__()) #prints '10' which is same because using positive sign before any number (whatever positive or negative) will change nothing
print(x.__invert__()) #prints '-11'  
print()



# in-place arithmetic operations
# __iadd__(), __isub__(), __imul__(), __itruediv__(), __imod__(), __ifloordiv__(), __ipow__()
#These dunder methods are worked as +=, -=, *= etc 
#but unfortunately these dunder method can't work barely...
#so you must avoid using these dunder methods
#
#similarly for in-place bitwise operations
#__iand__(), __ior__(), __ixor__(), __irshift__(), __ilshift__()
#you must avoid using these...



# .__divmod__() and .__rdivmod__()
#works as divmod(obj1, obj2) and divmod(obj2, obj1)
#obj1.__divmod__(obj2) --> divmod(obj1, obj2)
#obj1.__rdivmod__(obj2) --> divmod(obj2, obj1)
#
x = 10
y = 3
print(x.__divmod__(y)) #prints '(3, 1)'
print(x.__rdivmod__(y)) #prints '(0, 3)'
print()



# .__abs__(), .__round__()
#x.__abs__() --> abs(x)
#x.__round__() --> round(x)
a = -10
print(a.__abs__()) #prints '10'
b = 10.6
print(b.__round__()) #prints '11'
print()



# ================================================================== #

# Dunder attributes 


# __name__ or .__name__
#it shows function name
print(__name__) #prints '__main__'
def func20(x, y):
    return x + y
print(func20.__name__) #prints 'func20'
print()



# .__module__ 
#Shows which module a function was defined in.
import math
print(math.sqrt.__module__) # prints 'math'
print()



# .__doc__
#Accesses the "docstring" at the top of a file or function.
def greet():
    """This function says hello."""
    pass

print(greet.__doc__) # prints 'This function says hello.'
print()



# .__class__
#works as type()
x = 42
print(x.__class__) #prints '<class 'int'>'
print()



# .__dict__
#most objects store their attributes here
class Student: 
    def __init__(self, name, roll, cgpa): 
        self.name = name 
        self.roll = roll
        self.cgpa = cgpa

std1 = Student("Alice", 32, 3.95) 
print(std1.__dict__) # Output: {'name': 'Alice', 'roll': 32, 'cgpa': 3.95}
print()



# .__mro__ and .__bases__
#.__mro__: a class's method resolution order used for attribute lookups and super() calls
#.__bases__: the direct parent classes of a class
class Student_info: 
    def __init__(self, name, roll, cgpa): 
        self.name = name 
        self.roll = roll
        self.cgpa = cgpa

class Scholarship_info(Student_info):
    def scholarship(self, scholarship_name):
        self.scholarship_name = scholarship_name

print(Scholarship_info.__mro__) #prints '(<class '__main__.Scholarship_info'>, <class '__main__.Student_info'>, <class 'object'>)'
print(Scholarship_info.__bases__) #prints '(<class '__main__.Student_info'>,)'
print()



# __file__ 
#It shows the path to the current script.
print(__file__) #prints the path of the .py file
print()



# .__wrapped__() <AI>
#functions decorated with functools.wraps use this to point to the original function
import functools

def original(x):
    return x * 2

@functools.wraps(original)
def decorated(x):
    return original(x)

print(decorated.__wrapped__) # prints '<function original at ...>'



# .__package__
#It returns the package name the module belongs to.
import json
print(json.__package__) #prints 'json'
print()



# .__version__
#Often used in libraries to track releases.
import json
print(json.__version__) #prints the version of json
print()



# __debug__
#running Python with -O sets this to False and disables Python's assert statements
print(__debug__) #prints 'True'
print()



# .__defaults__, .__kwdefaults__, .__code__, .__globals__['greet'], .__closure__
def greeting(name, message="Hello", *, punc="!"):
    return f"{message}, {name}{punc}"

print(greeting.__defaults__) #prints '('Hello',)'
print(greeting.__kwdefaults__) #prints '{'punc': '!'}'
print(greeting.__code__) #prints '<code object greeting at ...>
print(greeting.__globals__['greet']) #prints '<function greet at ....>
print(greeting.__closure__) #prints 'None' (it would show cells if using closures)
print()



# .__qualname__ and .__annotations__
def add(x: int, y: int) -> int:
    return x + y

class Example:
    def method(self, x: int) -> str:
        return str(x)

print(add.__qualname__) #prints 'add'
print(Example.__qualname__) #prints 'Example'
print(add.__annotations__) #prints '{'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}'
print()



# .__static_attributes__, .__firstlineno__, .__func__, .__self__
class Demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def say_hi(self):
        return "Hi"

print(Demo.__static_attributes__) #prints '('x', 'y')'
print(Demo.__firstlineno__) #prints '533' (Line number where class is defined)
p = Demo(1, 2)
method = p.say_hi
print(method.__func__) #prints '<function Demo.say_hi at ...>'
print(method.__self__) #prints '<__main__.Demo object at ...>'
print()



# .__loader__, .__package__, .__spec__, .__cached__
import math
import collections
print(math.__loader__) #prints '<class '_frozen_importlib.BuiltinImporter'>'
print(math.__package__)  #prints '' (empty string for built-in modules)
print(math.__spec__) #prints 'ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')'
#print(math.__cached__) # Path to cached .pyc file (if exists)
print(collections.__path__) #Shows package search path list
print()



# .__traceback__, .__context__, .__cause__, .__suppress_context__, .__notes__
try:
    1 / 0
except ZeroDivisionError as e:
    print(e.__traceback__)       # Traceback object
    print(e.__context__)         # Previous exception (if any)
    print(e.__cause__)           # Explicit cause (if set)
    print(e.__suppress_context__)# False by default
    e.__notes__ = ["Division failed"]
    print(e.__notes__)           # ['Division failed']
print()



# .__origin__, .__args__, .__parameters__, .__unpacked__
from typing import List
T = List[int]
print(T.__origin__) #prints '<class 'list'>'
print(T.__args__) #prints '(<class 'int'>,)'
print(T.__parameters__) #print '()' (empty, no type vars)
#print(T.__unpacked__) # None (used for unpacked types)
print()



# .__stdout__, .__stderr__ 
import sys
print(sys.__stdout__) #prints '<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>'
print(sys.__stderr__) #prints '<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>'
print()



# .__covariant__, .__contravariant__, .__bound__, .__constraints__, .__infer_variance__
from typing import TypeVar

#Covariant type variable
T_co = TypeVar("T_co", covariant=True)
print(T_co.__covariant__) #prints 'True'

#Contravariant type variable
T_contra = TypeVar("T_contra", contravariant=True)
print(T_contra.__contravariant__) #prints 'True'

#Bound type variable
T_bound = TypeVar("T_bound", bound=int)
print(T_bound.__bound__) #prints '<class 'int'>'

#Constrained type variable
T_constrained = TypeVar("T_constrained", int, str)
print(T_constrained.__constraints__) #prints '(<class 'int'>, <class 'str'>)'

#Infer variance (Python 3.12+)
T_infer = TypeVar("T_infer", infer_variance=True)
print(T_infer.__infer_variance__) #prints 'True'
