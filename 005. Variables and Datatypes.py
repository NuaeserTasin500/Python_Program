## variables and datatypes
# in python, variable declaration doesn't need data type declaration like other programming languages

#declaring variables
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

#printing variables' values
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

print()

#getting datatypes of variables
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


# Type of type() function <S>
print("Datatypes of type() function is: ")
print(type(type(k))) #prints '<class 'type'>' which means Type Datatype
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

