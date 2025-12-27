## variables and datatypes
# in python, variable declaration doesn't need data type declaration like other programming languages

#declaring variables
a = 123 #integer
b = "John" #string
c = 12.3 #float
d = 4+8j #complex
e = True #boolean
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
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
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
