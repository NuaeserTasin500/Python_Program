## Datatype conversion (aka Typecasting)

#Converting string into int
a = "1"
b = "2"
c = a + b
print(c) #result won't be 3, rather it will be 12 and that is string 

d = int(a) #converting string 1 as integer 1
e = int(b) #converting string 2 as integer 2
f = d + e
print(f) #result will be 3, and that is integer


g = int(c) 
print(g) #result is 12 and that is integer


print()


#Converting int into string
a1 = 1 #integer
b1 = str(a1) #converting integer 1 as string 1
print(b1)

print()


#other datatype conversion
print(float(123)) #integer to float
print(str(12.43)) #float to string
print(bool("True")) #string to boolean
print(complex(123)) #integer to complex
print(str(3+7j)) #complex to string
#and so on.....


print()



# Exponential number 
a2 = 3e20
#if we want to see this big number with zero, we need to convert it as int, since exponential numbers are float
b2 = int(a2)
print(b2) #prints '300000000000000000000'
