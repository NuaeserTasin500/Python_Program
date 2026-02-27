## Variables, Datatypes and Built-in Functions
#in python, variable declaration doesn't need data type declaration like other programming languages

# Declaring variables
a = 123 #integer
b = "John" #string
c = 12.3 #float
d = 4+8j #complex
e = True #boolean (True, False, None)
f = [8, 2, 0.3, "hello"] #list
g = (8, 2, 3.5, "hello") #tuple
h = {"name":"John", "age":"25"} #dictionary
i = {1, 2, 3, 4} #set
j = frozenset([1, 2, 3, 5]) #frozenset
k = range(4) #range

# Printing variables' values
print(a) #prints '123'
print(b) #prints 'John'
print(c) #prints '12.3'
print(d) #prints '(4+8j)'
print(e) #prints 'True'
print(f) #prints '[8, 2, 0.3, 'hello']'
print(g) #prints '(8, 2, 3.5, 'hello')'
print(h) #prints '{'name': 'John', 'age': '25'}'
print(i) #prints '{1, 2, 3, 4}'
print(j) #prints 'frozenset({1, 2, 3, 5})'
print(k) #prints 'range(0, 4)'

print()

# Getting datatypes of variables
print("Datatypes of all variables are: ")
print(type(a)) #prints '<class 'int'>' which means Integer Datatype
print(type(b)) #prints '<class 'str'>' which means String Datatype
print(type(c)) #prints '<class 'float'>' which means Float Datatype
print(type(d)) #prints '<class 'complex'>' which means Complex Datatype
print(type(e)) #prints '<class 'bool'>' which means Boolean Datatype
print(type(f)) #prints '<class 'list'>' which means List Datatype
print(type(g)) #prints '<class 'tuple'>' which means Tuple Datatype
print(type(h)) #prints '<class 'dict'>' which means Dictionary Datatype
print(type(i)) #prints '<class 'set'>' which means Set Datatype
print(type(j)) #prints '<class 'frozenset'>' which means Frozenset Datatype
print(type(k)) #prints '<class 'range'>' which means Range Datatype
print()


# Only printing datatypes
print("Here are Datatypes: ")
print(int) #prints '<class 'int'>' which means Integer Datatype
print(str) #prints '<class 'str'>' which means String Datatype
print(float) #prints '<class 'float'>' which means Float Datatype
print(complex) #prints '<class 'complex'>' which means Complex Datatype
print(bool) #prints '<class 'bool'>' which means Boolean Datatype
print(list) #prints '<class 'list'>' which means List Datatype
print(tuple) #prints '<class 'tuple'>' which means Tuple Datatype
print(dict) #prints '<class 'dict'>' which means Dictionary Datatype
print(set) #prints '<class 'set'>' which means Set Datatype
print(frozenset) #prints '<class 'frozenset'>' which means Frozenset Datatype
print(range) #prints '<class 'range'>' which means Range Datatype
print()

#Datatypes like int, str, list are classes in Python.
#They behave like functions because you can call them to construct objects (e.g., int("123") → 123).
#But technically, they are classes, not functions.



# Type of type() function <S>
#type() is both class and built-in function
print("Datatypes of type() function is: ")
print(type(type(k))) #prints '<class 'type'>' which means Type Function
print(type) #prints '<class 'type'> which means Type Function
print(type(int)) #still prints '<class 'Type'>
print()



# Printing type of built-in functions (without using type) <S>
print("Here are Built-in functions (without using type): ")
print(print) #prints '<built-in function print>'
print(len) #prints '<built-in function len>'
print(input) #prints '<built-in function input>'
print(abs) #prints '<built-in function abs>'
print()



# Printing type of built-in functions (with using type) <S>
print("Here are Built-in functions (with using type): ")
print(type(print)) #prints <class 'builtin_function_or_method'> 
print(type(len)) #prints <class 'builtin_function_or_method'>
print(type(input)) #prints <class 'builtin_function_or_method'>
print(type(abs)) #prints <class 'builtin_function_or_method'> 
print()



# Binary, Octal and Hexadecimal numbers
#In Python programming, Binary, Octal and Hexadecimal numbers are considered as integer numbers
#for denoting binary, we need to use 0b before binary number
#for denoting octal, we need to use 0o before octal number
#for denoting hexadecimal (lowercase), we need to use 0x before hexadecimal number
#for denoting hexadecimal (uppercase), we need to use 0X before hexadecimal number
#binary number here will be unsigned (not signed, for example: 1101 will be 13, not -3)

bin_a = 0b1011 #decimal of 0b1011 is 11
print(bin_a) #prints '11' 

#for printing as negative, we need to use '-' sign
bin_b = -0b1011 #decimal of -0b1011 is -(11) = -11
print(bin_b) #prints '-11'

#if we want to print binary number as binary number, we need to use bin() function, but that will be printed as string
print(bin(bin_a)) #prints '0b1011'
print(bin(bin_b)) #prints '-0b1011'

#now let's see about octal and hexadecimal number
oct_a = 0o17 #decimal of 0o17 is 15
hex_a = 0x1a #decimal of 0x1a is 26
hex_aa = 0X1A #decimal of 0x1A is 26
print(oct_a) #prints '15'
print(hex_a) #prints '26'
print(hex_aa) #prints '26'
print()
#if we want to print octal number as octal number, we need to use oct() function, but that will be printed as string
print(oct(oct_a)) #prints '0o17'

#if we want to print hexadecimal number as hexadecimal number, we need to use hex() function, but that will be printed as string
print(hex(hex_a)) #prints '0x1a'
#for printing uppercase hexadecimal number, we must use format(), not hex()
#just remember this right now, we will discuss more about format() later 
print(format(hex_a, '#X')) #prints '0X1A'
print()
#remember one thing, 
#if you store bin(), hex(), oct(), format() in variables, that will be string variables
#for example: abc = bin(bin_a), here 'abc' will be string variable  

#now we will see how to print the binary, hexadecimal and octal of a decimal number
dec_a = 30
print(oct(dec_a)) #prints '0o36'
print(bin(dec_a)) #prints '0b11110'
print(hex(dec_a)) #prints '0x1e'
print(format(dec_a, '#X')) #prints '0X1E'
print()



# Exponential numbers
#Exponential numbers are float numbers. They have 'e', where left side of e is base and right side of e is power
#Even uppercase 'E' can be used 
exp_a = 2e20 #means '2 to the power 20' or pow(2, 10)
exp_b = 3E20 #means '3 to the power 20' or pow(3, 10)
print(exp_a) #prints '2e+20'
print(exp_b) #prints '3e+20'
print()





# Update the value of variable
age = 20
print("Your age is ", age)
age = 30 #age value 20 is updated as 30
print("Your age is ", age)
print()

x = 2
print("x = ", x)
x = x + 2 #x value 2 is updated as x + 2 = 2 + 2 = 4
print("x = ", x)
print()

# In python, you can declare multiple variables in one line
p, q, r, s = 10, 20, 'Hello', True
print(p) #prints '10'
print(q) #prints '20'
print(r) #prints 'Hello'
print(s) #prints 'True'
print()

# You can use () for this case too 
t, u, v, w = (False, 'Nothing', 100, 99.5)
print(t) #prints 'False'
print(u) #prints 'Nothing'
print(v) #prints '100'
print(w) #prints '99.5'
print()


# Automatically declaring tuples
tup = 10, 20, 30, 40
print(tup) #prints '(10, 20, 30, 40)'
print()


# Automatically declaring list
mn, *ex, em = 10, 20, 30, 40, 50
print(mn) #prints '10'
print(ex) #prints '[20, 30, 40]'
print(em) #prints '50'
print()

# Assigning same values to multiple variables
mm = nn = oo = 100
print(mm) #prints '100'
print(nn) #prints '100'
print(oo) #prints '100'
print()

# Swapping variables' values 
aa, bb = 10, 20
print(aa, bb) #prints '10, 20'
aa, bb = bb, aa
print(aa, bb) #prints '20, 10'

