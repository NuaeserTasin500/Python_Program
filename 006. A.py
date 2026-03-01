## Arithmetic operation and Bitwise operation


# ============================================================== #


## Arithmetic operation

a = 10
b = 3

# storing arithmetic operations into new variables
c = a + b #additon
d = a - b #subtraction
e = a * b #multiplication
f = a / b #division
g = a // b #floor division
h = a % b #remainder
i = a ** b #exponential (a to the power b)


# printing the arithmetic operation stored variables
print("a =", a)
print("b =", b)
print("a + b =", c)
print("a - b =", d)
print("a * b =", e)
print("a / b =", f)
print("a // b =", g)
print("a % b =", h)
print("a ** b =", i)

print()



# printing arithmetic operation without storing
#Note: operations that are not stored in variables can only be used for printing and execution one time.
#by storing them in variables, you can use them for future calculations and later reuse
#
a1 = 50
b1 = 30

print("a1 =", a1)
print("b1 =", b1)
print("a1 + b1 =", a1 + b1)
print("a1 - b1 =", a1 - b1)
print("a1 * b1 =", a1 * b1)
print("a1 / b1 =", a1 / b1)
print("a1 // b1 =", a1 // b1)
print("a1 % b1 =", a1 % b1)
print("a1 ** b1 =", a1 ** b1)

print()


# storing arithmetic operation by using values directly
n1 = 7 + 4
n2 = 5 - 3
n3 = 10 * 5
n4 = 10 / 5
n5 = 11 // 5
n6 = 11 % 5
n7 = 10 ** 2
print(n1) 
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print()



# printing arithmetic operation by using values directly (without storing those arithmetic operations in variables)
#Note: Arithmetic operations that are not stored in variables can only be used for printing and execution one time.
#by storing them in variables, you can use them for future calculations and later reuse
#
print("7 + 4 =", 7 + 4)
print("7 - 4 =", 7 - 4)
print("7 * 4 =", 7 * 4)
print("7 / 4 =", 7 / 4)
print("7 // 4 =", 7 // 4)
print("7 % 4 =", 7 % 4)
print("7 ** 4 =", 7 ** 4)
print()



# we also can do operation between a variable and a value
var1 = 10
add1 = var1 + 2
sub1 = var1 - 2
#similary we can do as mul1 = var1 * 2, div1 = var1 / 2 and so on......
print(add1) #prints '12'
print(sub1) #prints '8'
#similar operation we can print without storing any variable
print(var1 + 1) #prints '11'
print(var1 / 2) #prints '5.0'
print()



# In place arithmetic operations (+=, -=, *=, /=, //=, %=, **=) <SAWDT> 
p = 10 
q = 2
p += q #means p = p + q, which means p + q = 10 + 2 = 12 and 12 will be stored to p
print(p) #prints '12'. Now x's value is not 10, rather it is 12.
p1 = 12
q1 = 3
p1 -= q1 #means p1 = p1 - q1, which means p1 - q1 = 12 - 3 = 9 and 9 will be stored to p1
print(p1) #prints '9'. Now p1's value is not 12, rather it is 9
#
#we can do these operation between a variable and a value also
p2 = 14
p2 *= 3 #means p2 = p2 * 3, which means p2 * 3 = 14 * 3 = 42 and 42 will be stored to p2
print(p2) #prints '42' and p2's value is not 14, rather it is 42
p3 = 10
p3 /= 2 #means p2 = p2 / 2, which means p2 / 2 = 10 / 2 = 5.0 and 5.0 will be stored to p3
print(p3) #prints '5.0' and p3's value is not 10, rather it is 5.0
p4 = 11
p4 //= 2 #means p4 = p4 // 2, which means p4 // 2 = 11 // 2 = 5 and 5 will be stored to p4
print(p4) #prints '5' and p4's value is not 11, rather it is 5
p5 = 11
p5 %= 2 #means p5 = p5 % 2, which means p5 % 2 = 11 % 2 = 1 and 1 will be stored to p5
print(p5) #prints '1' and p5's value is not 11, rather it is 1
p6 = 10
p6 **= 2 #means p6 = p6 ** 2, which means p6 ** 2 = 10 ** 2 = 100 and 100 will be stored to p6
print(p6) #prints '100' and p6's value is not 10, rather it is 100
print()




# =========================================================================#




## Bitwise Operation <SAWDT> <AI>

#in bitwise operation, there are:
#'&' (and) operator --> example: 1 & 0 = 0
#'|' (or) operator --> example: 1 | 0 = 1
#'^' (xor) opertor --> example: 1 ^ 0 = 1
#'>>' (right shift) operator
#'<<' (left shift) operator
#'~' (not) operator (works as ~x = -(x+1))
#in bitwise operation, the binary value of integer operands are involved in this calculation bitwisely.
#
#At first we will see and, or, xor and not
 

x1 = 4 #binary value of 4 is 100
y1 = 5 #binary value of 5 id 101
z1 = x1 & y1 #100 & 101 = 100 (bitwisely 1 & 1 = 1; 0 & 0 = 0; 0 & 1 = 0)
z2 = x1 | y1 #100 | 101 = 101 (bitwisely 1 | 1 = 1; 0 | 0 = 0; 0 | 1 = 1)
z3 = x1 ^ y1 #100 ^ 101 = 001 (bitwisely 1 ^ 1 = 0; 0 ^ 0 = 0; 0 ^ 1 = 1)
z4 = ~x1 #~100 = -(100+1) = -(101) 
print(z1) #prints '4' because the decimal value of 100 is 4
print(z2) #prints '5' because the decimal value of 101 is 5
print(z3) #prints '1' because the decimal value of 001 is 1
print(z4) #prints '-5' because the decimal value of 101 is 5 and -(101) = -(5) = -5
#For flipping bits, as all 1 will be 0 and all 1 will be 0, then we need to do is ~x & 0x<maximum value>
#since x1 = 4's binary value is 100 (which is 3 bits), then maximum value is = (2**3) - 1 = 8 - 1 = 7 (binary value of 7 is 111) 
z5 = ~x1 & 7
print(z5) #prints '3' as negation of 100 is 011 
print()


# we can print these operations in without storing variables
#Note: Bitwise operations that are not stored in variables can only be used for printing and execution one time.
#by storing them in variables, you can use them for future calculations and later reuse
#
print(x1 & y1)
print(x1 | y1)
print(x1 ^ y1)
print(~y1)
print()
#
#also we can store bitwise operation by using values directly and can print them
zz1 = 7 & 5
zz2 = 7 | 5
zz3 = 7 ^ 5
zz4 = ~(6)
print(zz1)
print(zz2)
print(zz3)
print(zz4)
print()

# printing operation bitwise operation by using values directly (without storing those bitwise operations in variables)
#Note: Bitwise operations that are not stored in variables can only be used for printing and execution one time.
#by storing them in variables, you can use them for future calculations and later reuse
#
print(7 & 4) #prints '4'
print(7 | 4) #prints '7'
print(7 ^ 4) #prints '3'
print(~(2)) #prints '-3'
print()


# we also can do bitwise operation between a variable and a value 
z6 = x1 & 2 
z7 = x1 | 2
z8 = x1 ^ 3 
print(z6)
print(z7)
print(z8)
print()
#
# also we can directly print the result of this type of operation without storing to the variable
#Note: Bitwise operations that are not stored in variables can only be used for printing and execution one time.
#by storing them in variables, you can use them for future calculations and later reuse
#
print(x1 & 2)
print(x1 | 2)
print(x1 ^ 3)
print()




# Now let's talk about >> (right shift) and << (left shift)
#Right shift (>>) removes bits from the right side of binary number
#Left shift (<<) adds 0 to the right side of binary number
#
#Understanding of left shift,
#x << 1 means you add 1 bit (a zero) to the right side of binary number
#x << 2 means you add 2 bit (two zeros) to the right side of binary number
#x << 3 means you add 3 bit (three zeros) to the right side of binary number 
#and so on.....
#
#Understanding of right shift
#x >> 1 means you removed 1 bit from the right side of binary number
#x << 2 means you removed 2 bit from the right side of binary number
#x << 3 means you removed 3 bit from the right side of binary number 
#and so on.....
#
# Here I will use these bitwise operations between a variable 'c' and just 1, 2 values (which are not stored in variables) for better understanding
#
c = 50 #the binary number of 50 is 110010
d = c << 1 #it adds a 0 to the right side of of 110010 and now it becomes 1100100, stored in d 
e = c << 2 #it adds two 0 to the right side of c's binary value 110010 and now it becomes 11001000, stored in e
print(c) #prints '50' (binary value of 50 is 110010)
print(d) #prints '100' (decimal value of 1100100 is 100)
print(e) #prints '200' (decimal value of 11001000 is 200)
d1 = c >> 1 #it removes a bit from the right side of 110010 and now it becomes 11001, stored in d1
e1 = c >> 2 #it removes two bits from the right side of of 110010 and now it becomes 1100, stored in e1
print(d1) #prints '25' (decimal value of 11001 is 25)
print(e1) #prints '12' (decimal value of 1100 is 12)
print()
#
#
# We can do these bitwise operation like this:-
c1 = 50
c2 = 1
c3 = 2
dd1 = c1 << c2
ee1 = c1 << c3
print(dd1)
print(ee1)
dd2 = c1 >> c2
ee2 = c1 >> c2
print(dd2)
print(ee2)
print()
#
# and like this:-
dd3 = 50 << 1
dd4 = 50 >> 1
print(dd3)
print(dd4)
print()
#
# and like this:-
print(c1 >> c2)
print(c1 << c2)
print()
#
# and also like this:-
print(50 >> 2)
print(50 << 2)  
print()
#
#But remember one thing:-
#Left shift and right shift Bitwise operations that are not stored in variables can only be used for printing and execution one time.
#by storing them in variables, you can use them for future calculations and later reuse
#So the choice is yours that how to use it



# Using binary number in bitwise operation
#For using binary number 
a2 = 0b101
b2 = 0b110
print(bin(a2 & b2)) #prints '0b100'
print(bin(a2 | b2)) #prints '0b111'
print(bin(a2 ^ b2)) #prints '0b11' (binary number don't show 0 in MSB)
print(bin(a2 << 2)) #prints '0b10100'
print(bin(a2 >> 2)) #prints '0b1'
print()



# ==================================================== #

## Storing operations by declaring multiple variables in one line <S>
a = 10
b = 30
x, y, z, n, m = 10 + 20, b - a, b >> 2, a & b, 2 | 3
print(x) #prints '30'
print(y) #prints '20'
print(z) #prints '7'
print(n) #prints '10'
print(m) #prints '3'
print()
