## Arithmetic operation and Bitwise operation


# ============================================================== #


## Arithmetic operation

a = 10
b = 3

# storing operations into new variables
c = a + b #additon
d = a - b #subtraction
e = a * b #multiplication
f = a / b #division
g = a // b #floor division
h = a % b #remainder
i = a ** b #exponential (a to the power b)


# printing the operation stored variables
print("a = ", a)
print("b = ", b)
print(a, "+", b, "=", c)
print(a, "-", b, "=", d)
print(a, "*", b, "=", e)
print(a, "/", b, "=", f)
print(a, "//", b, "=", g)
print(a, "%", b, "=", h)
print(a, "**", b, "=", i)

print()


a1 = 50
b1 = 30

# printing operation without storing
print("a1 = ", a1)
print("b1 = ", b1)
print(a1, "+", b1, "=", a1 + b1)
print(a1, "-", b1, "=", a1 - b1)
print(a1, "*", b1, "=", a1 * b1)
print(a1, "/", b1, "=", a1 / b1)
print(a1, "//", b1, "=", a1 // b1)
print(a1, "%", b1, "=", a1 % b1)
print(a1, "**", b1, "=", a1 ** b1)

print()


#printing operation without using variables
print(7, "+", 4, "=", 7 + 4)
print(7, "-", 4, "=", 7 - 4)
print(7, "*", 4, "=", 7 * 4)
print(7, "/", 4, "=", 7 / 4)
print(7, "//", 4, "=", 7 // 4)
print(7, "%", 4, "=", 7 % 4)
print(7, "**", 4, "=", 7 ** 4)


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
print("x1 = ", x1) 
print("y1 = ", y1)
print(x1 & y1) #prints '4' because 100 & 101 = 100 (bitwisely 1 & 1 = 1; 0 & 0 = 0; 0 & 1 = 0)
print(x1 | y1) #prints '5' because 100 | 101 = 101 (bitwisely 1 | 1 = 1; 0 | 0 = 0; 0 | 1 = 1)
print(x1 ^ y1) #prints '1' because 100 ^ 101 = 001 (bitwisely 1 ^ 1 = 0; 0 ^ 0 = 0; 0 ^ 1 = 1)
print(~x1) #prints '5' because ~100 = -(100+1) = -101 = -5
#For flipping bits, as all 1 will be 0 and all 1 will be 0, then we need to do is ~x & 0x<maximum value>
#since x1 = 4's binary value is 100 (which is 3 bits), then maximum value is = (2**3) - 1 = 8 - 1 = 7 (binary value of 7 is 111) 
print(~x1 & 7) #prints '3' as negation of 100 is 011 
print()

#we can store these operations in variables like 
#z1 = x1 | y1
#z2 = x1 ^ y1
#z3 = ~y1
#and so on.... 

# printing operation without using variables
print(7, "&", 4, "=", 7 & 4)
print(7, "|", 4, "=", 7 | 4)
print(7, "^", 4, "=", 7 ^ 4)
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

# Using binary number in bitwise operation
#For using binary number 
a2 = 0b101
b2 = 0b110
print(bin(a2 & b2)) #prints '0b100'
print(bin(a2 | b2)) #prints '0b111'
print(bin(a2 ^ b2)) #prints '0b11' (binary number don't show 0 in MSB)
print(bin(a2 << 2)) #prints '0b10100'
print(bin(a2 >> 2)) #prints '0b1'

