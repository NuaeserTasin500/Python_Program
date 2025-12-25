## input function


a = input()
print("Your name is ", a)

#you can add string in input function
b = input("Input your age: ")
print("Your name is ", b)

#but problem is input() only take string, 
#just look, b is string
print(type(b))

print()

#so we use datatype conversion
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("First number + second number = ", x+y)

#we can also do that for float and others.
