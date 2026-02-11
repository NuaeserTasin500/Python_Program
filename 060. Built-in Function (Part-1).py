## Built-in Function (Part-1)
#Found from: https://docs.python.org/3/library/functions.html
#and https://dev.to/onyxwizard/python-built-in-functions-ultimate-cheat-sheet-6n0

# abs()
#it returns absolute value of a number
z = abs(-3)
print(z) #prints '3'
print()



# aiter()
#aiter() is a built-in function that returns an asynchronous iterator object from an asynchronous iterable
#for aiter, we need to import asyncio
import asyncio 
async def async_number():
    for i in range(1, 4):
        yield i

async def main1():
    async for number in aiter(async_number()):
        print(number)

asyncio.run(main1()) #prints '1 <newline> 2 <newline> 3'
print()



# anext()
#anext() is a built-in function that retrieves the next item from an asynchronous iterator, acting as the async version of next().
async def async_number1(x):
    for i in range(x):
        yield i

async def main2(x):
    agen = async_number1(x) #Create an async generator
    print(await anext(agen, 'End'))
    print(await anext(agen, 'End'))
    print(await anext(agen, 'End'))
    print(await anext(agen, 'End'))

num = 2
asyncio.run(main2(num)) #prints '0 <newline> 1 <newline> End <newline> End'
print()

num = 4
asyncio.run(main2(num)) #prints '0 <newline> 1 <newline> 2 <newline> 3'
print()




# all() 
#it returns True if all elements in an iterable are True, otherwise false
list1 = [1, 2, 3]
list2 = [False, False]
bool1 = all(list1)
bool2 = all(list2)
print(bool1) #prints 'True'
print(bool2) #prints 'False'
print()


# any()
#returns True if at least one element is True
list3 = [False, 3]
list4 = [10, 9, 8]
list5 = [False, False]
bool3 = any(list3)
bool4 = any(list4)
bool5 = any(list5)
print(bool3) #prints 'True'
print(bool4) #prints 'True'
print(bool5) #prints 'False'
print()


# ascii()
#returns a string containing a printable representation
print(ascii('café')) #prints 'caf\xe9'
print()




# bin()
#returns binary version of a number
a = 5
bin_a = bin(a) 
print(bin_a) #prints '0b101'
print()


# bool()
#converts a value to boolean
print(bool(0)) #prints 'False'
print(bool(1)) #prints 'True'
print(bool(2)) #still prints 'True'
print(bool(-1)) #still prints 'True'
print()



# breakpoint()
#breakpoint() is a built in function which pause execution and opens interactive debugger (pdb)
#this time, type command 'c' means continue execution; type command 'n' means go to the next line <AI>
#source: https://www.digitalocean.com/community/tutorials/python-breakpoint
var1 = 10
var2 = 20
print(var1)
breakpoint()
print(var2)
print()



# bytearray()
#it creates a mutable array of bytes
ba1 = bytearray('café', 'utf-8')
print(ba1) #prints 'bytearray(b'caf\xc3\xa9')'
ba2 = bytearray('hello', 'utf-8')
print(ba2) #prints 'bytearray(b'hello')'
print()



# bytes()
#it creates an immutable bytes object
ba3 = bytes('hello', 'utf-8')
print(ba3) #prints 'b'hello''



# callable()
#it returns 'True' for object which is callable, otherwise it will return 'False'
def func300(x):
    return x
fnc1 = func300
print(callable(fnc1)) #prints 'True' because func300 is an function and it is callable

eee = 10
print(callable(eee)) #prints 'False' because eee is an integer variable and it isn't callable
print()


# chr()
#it returns the character corresponding to an ASCII code
print(chr(65)) #prints 'A'

#let's make a fun of this chr() function
def ascii(num):
    return chr(num)
a = [73, 32, 108, 111, 118, 101, 32, 121, 111, 117]
for i in a:
    print(ascii(i), end='') #prints 'I love you'
print("\n")



# compile(), eval(), exec()
#In Python programming, compile() function takes source code (as a string, bytes, or AST object) and returns a code object that can later be executed by the exec() or eval() functions
#eval() is used if the source is a single expression that results in a value
code_string = '5 ** 2'
compilation1 = compile(code_string, '<string>', 'eval')
output1 = eval(compilation1)
print(output1) #prints '25'

#exec() used if the source consists of a sequence of statements (e.g. function)
code_string2 = '''
def func110(x, y):
    return x + y

print(func110(10, 20))
''' 
compilation2 = compile(code_string2, '<string>', 'exec')
exec(compilation2) #prints '30'
#We can use eval() function freely also
eval("2 + 3") #prints '5'
#We can use exec() function freely also
exec("x = 100\nprint(x)") #prints '100'
print()


# complex()
#it creates complex number
b = complex(2, 3)
print(b) #prints '(2+3j)'


# delattr()
#it deletes an attribute from an object
class Car:
    color = 'red'
    light = 'yellow'
    def info (self):
        print(f"{self.color} and {self.light}")
c = Car()
c.info()
delattr(Car, 'color')
#in this time c.info() will work error, because we have deleted color attribute
print()



# dict() 
#it creates dictionary
dict1 = dict(name="John", age="11")
print(dict1) 
print()



# dir()
#returns attributes of an object
int_a = 10
list_a = [10, 20, 30]
print(dir(int_a)) #shows attributs of integer
print(dir(list_a)) #shows attributs of list
print()




# divmod() 
#it shows quotient and remainder
a1 = 10
b1 = 3
result1 = a1 / b1
remainder1 = a1 % b1
print(f"{result1} , {remainder1}") #prints '3.3333333333333335, 1'
#here result comes as float, not integer; which is not quotient
#but we can get quotient and remainder by divmod(), and the quotient will come as 
print(divmod(a1, b1)) #prints '(3, 1)'



# enumerate()
#it returns index and value pairs for list, tuple
country = ["Afghanistan", "Pakistan", "Tajikistan", "Turkmenistan"]
for index, x in enumerate(country):
    print(f"{index}. {x}") 
print()



# filter() 
#filters iterable using a function
h = tuple(filter(lambda x: x % 5 == 0, (10, 3, 15, 4, 5, 20)))
print(h) #prints '(10, 15, 5, 20)'



# float()
#converts a value to float
a3 = 10
b3 = "10.451"
print(float(a3)) #prints '10.0'
print(float(b3)) #prints '10.451'
print()



# format() 
#formats a string
#source: https://www.geeksforgeeks.org/python/python-string-format-method/
a4 = "John"
b4 = 22
message = "My name is {0} and I am {1} years old.".format(a4, b4)
print(message) #prints 'My name is John and I am 22 years old.

#for single placeholder
print("{} is my favorite language".format("English"))

#using variable
c1 = "Bangla"
print("I love {} language".format(c1))




# frozenset()
#it creats and immutable set
a5 = frozenset([1, 2, 3])
print(a5) #prints 'frozenset([1, 2, 3])'
print()


# getattr()
#it returns the value of a named attribute
class Dog:
    name = "Spike"

print(getattr(Dog, "name")) #prints 'Spike' 
print()




# globals()
#returns dictionary of global variables
print(globals()) #prints '{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000238B554C380>, '__spec__': None,......' something
print()




# hasattr() 
#it returns true if a class has that attribute
class Student:
    schoolName = "XYZ High School"

print(hasattr(Student, "schoolName")) #prints 'True' because Student class has schoolName attribute
print(hasattr(Student, "headmasterName")) #prints 'False' because Student class has no headmasterName attribute
print()



# hash()
#it returns hash of an object
a6 = 100
print(hash(a6)) #prints '100'
b6 = "hello"
print(hash(b6)) #prints some number becuase b6 is not an integer
print()



# help()
#it provides interactive documentation about objects, modules, classes, functions, or keywords.
print(help(list)) #it shows documentation of list
print()


# hex()
#returns hexadecimal representation
a = 1234
b = hex(a)
print(b) #prints '0x4d2'






