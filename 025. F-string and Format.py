## F-string And Format

#====================================================================#
## F-string
#In Python programming language, f-string is a string which is prefixed with 'f'. It allows you to create string with directly interpolation by using the curly braces. 

place = "London"
name = "Jack"
print(f"Hey, my name is {name} and I am from {place}") #prints 'Hey, my name is Jack and I am from London'

# another method of of f-string
place = "America"
name = "Jill"
str1 = f"Hey, my name is {name} and I am from {place}"
print(str1) #prints 'Hey, my name is Jill and I am from America'
print()

# list method 
name = ['Anna', 'Steve', 'Rakib']
place = ['United States', 'United Kingdom', 'Bangladesh']
hobby = ['Gardening', 'Programming', 'Solo-Travelling']

for i in range(len(name)): 
    #length of name, place and hobby lists are same
    print(f"Hello! My name is {name[i-1]}. I am from {place[i-1]}. My hobby is {hobby[i-1]}.")
print()

# decimal point control
price = 50.7644850304
txt14 = f"This product's price is {price:.2f}$" #keeping two numbers after points
print(txt14) #prints 'This product's price is 50.76$'
print()

# f-string contains function <S>
def circle_area(r):
    area = 3.1416 * (r**2)
    return area
radius = 30
print(f'if radius of a circle is {radius}, then the area of radius is {circle_area(radius)}') #prints 'if radius of a circle is 30, then the area of radius is 2827.44'

# function returns f-string <S>
def mul (x, y):
    return f'The multiplication of {x} and {y} is {x*y}' #return f-string
a = 30
b = 40
print(mul(a, b)) #prints 'The multiplication of 30 and 40 is 1200'
print()


# =============================================================================== #

## Format <AI>
#in python programming, format is used for dynamically inserting values in a string template.
#learning material: https://geekpython.medium.com/4-ways-of-string-formatting-in-python-guide-931600465eb2

# using {}
text1 = "Hello {}".format("World")
print(text1) #prints 'Hello World'
name = "Alice"
text2 = "My name is {}".format(name)
print(text2) #prints 'My name is Alice'
print()



# using {} with numbers
text3 = "Hello {0}. My name is {1}. I am {2} years old.".format("everyone", "Jack", 25)
print(text3) #prints 'Hello everyone. My name is Jack. I am 25 years old.'
print()
#bulking text <S>
info = "This laptop's name is {0}"
print(info.format("Lenovo")) #prints 'This laptop's name is Lenovo'
print(info.format("Acer")) #prints 'This laptop's name is Acer'
print(info.format("Asus")) #prints 'This laptop's name is Asus'
print()
#bulking text by set and for loop <S>
info1 = "Student name is {0}"
std_names = ['John', 'Alex', 'Rachel']
for x in std_names:
    print(info.format(x))
print()



# using {} with variables
text4 = "I have a {thing}. It has a {thing1}".format(thing='laptop', thing1='processor')
print(text4) #prints 'I have a laptop. It has a processor
#bulking text <S>
info = "This laptop's name is {laptop_name}"
print(info.format(laptop_name="Lenovo")) #prints 'This laptop's name is Lenovo 
print(info.format(laptop_name="Acer")) #prints 'This laptop's name is Acer
print(info.format(laptop_name="Asus")) #prints 'This laptop's name is Asus
print()
#bulking text by set and for loop <S>
info1 = "Programmer name is {name}"
prg_names = ['Asif', 'Rahman', 'Akash']
for x in prg_names:
    print(info1.format(name=x))
print()
#Reusing variable
info2 = "{country_name} is a beautiful country. {country_name}'s people are nice. I love {country_name} very much.".format(country_name="Ireland")
print(info2) #prints 'Ireland is a beautiful country. Ireland's people are nice. I love Ireland very much.'
print()



# using %
#%s — for string
#%d — for integers
#%f — for floating-point values
#%e — for floating-point exponent
goods = 'Printer'
price = 1000.50
print("I am going to buy this %s. This costs $%.2f" %(goods, price)) #prints 'I am going to buy this printer. This costs $1000.50'  
print("This costs $%f" %price) #prints 'This costs $1000.500000'
print("This printer's name is %s. Serial number is %i" %("zen", 324)) #prints 'This printer's name is zen. Serial number is 324'
print("This printer is %s" %'beautiful') #prints 'This printer is beautiful'
print("The speed of light is %e" %3e8) #prints 'The speed of light is 3.000000e+08'

#float value representation
#%x.yf -> here x is a minimum number of digits in a string yf represents how many integers have to display after the decimal point.
#suppose 1280.396 is a float number where digit before point is 4. If x<=4 then, then that float value remains same. if x>5, then it might be padded with whitespace.
floatvalue = 1280.396
print("Value is = %0.0f" %floatvalue) #prints 'Value is = 1280'
print("Value is = %0.1f" %floatvalue) #prints 'Value is = 1280.4'
print("Value is = %0.2f" %floatvalue) #prints 'Value is = 1280.40'
print("Value is = %0.3f" %floatvalue) #prints 'Value is = 1280.396'
print("Value is = %10.0f" %floatvalue) #prints 'Value is =       1280'
print("Value is = %10.1f" %floatvalue) #prints 'Value is =     1280.4'
print("Value is = %10.2f" %floatvalue) #prints 'Value is =    1280.40'
print("Value is = %10.3f" %floatvalue) #prints 'Value is =   1280.396'
print("Value is = %20.0f" %floatvalue) #prints 'Value is =                 1280'
print("Value is = %20.1f" %floatvalue) #prints 'Value is =               1280.4'
print("Value is = %20.2f" %floatvalue) #prints 'Value is =              1280.40'
print("Value is = %20.3f" %floatvalue) #prints 'Value is =             1280.396'
print()



# indexing format <S>
#s — for string
#d — for integers
#f — for floating-point values
#e — for floating-point exponent
print("My name is {0:s}".format("Sarjis", "Hasanat")) #prints 'My name is Sarjis'
print("My name is {1:s}".format("Sarjis", "Hasanat")) #prints 'My name is Hasanat'
print("(12, 9) point's x = {0:d}".format(12, 9)) #prints '(12, 9) point's x = 12'
print("(12, 9) point's x = {1:d}".format(12, 9)) #prints '(12, 9) point's x = 9'
print("(12.36, 9.6) point's x = {0:.2f}".format(12.36, 9.6)) #prints '(12.36, 9.6) point's x = 12.36'
print("(12.36, 9.6) point's x = {1:.2f}".format(12.36, 9.6)) #prints '(12.36, 9.6) point's x = 9.60'
print("Big number = {0:e}".format(1e10, 1e-10)) #prints 'Big number = 1.000000e+10'
print("Small number = {1:e}".format(1e10, 1e-10)) #prints 'Small number = 1.000000e-10'
print()



# Format Specification Mini-Language <AI><SAWDT>
#'s' — for string
#'d' — for integers
#'f' — for floating-point values
#'e' — for floating-point exponent
#'E' — for floating-point exponent (uppercase)
#'%' — Percentage (multiplies by 100 and adds %).
#'x' — Hexadecimal (base 16, lowercase).
#'X' — Hexadecimal (base 16, uppercase).
#'b' — Binary (base 2, unsigned).
#'#b' — Binary (base 2, signed).
#'o' — Octal (base 8).
name300 = 'John'
age300 = 20
balance300 = 19000.25
exp300 = 3e8 
print(f"His name is {name300:s}. His age is {age300:d}. His bank balance is {balance300:.2f}. He knows that light's speed is {exp300:e}")
#prints 'His name is John. His age is 20. His bank balance is 19000.25. He knows that light's speed is 3.000000e+08'
print(f"Light's speed is {exp300:E}") #prints 'Light's speed is 3.000000E+08'
float_num = 0.3
int_num = 200
print(f"The percentage of {float_num:.2f} is {float_num:%}") #prints 'The percentage of 0.30 is 30.000000%'
print(f"The lower hexadecimal value of {int_num:d} is {int_num:x}") #prints 'The lower hexadecimal value of 200 is c8'
print(f"The upper hexadecimal value of {int_num:d} is {int_num:X}") #prints 'The upper hexadecimal value of 200 is C8'
print(f"The unsigned binary value of {int_num:d} is {int_num:b}") #prints 'The unsigned binary value of 100 is 1100100'
print(f"The signed binary value of {int_num:d} is {int_num:#b}") #prints 'The signed binary value of 100 is 0b1100100'
print(f"The octal value of {int_num:d} is {int_num:o}") #prints 'The octal value of 200 is 310'

#we can directly use value in Format Specification Mini-Language.
print(f"The value of PI is {3.1416:.4f}") #prints 'The value of PI is 3.1416'
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
print(f"Hello {str1:<8}. How are you?") #prints 'Hello World   . How are you?'
print(f"Hello {str1:>8}. How are you?") #prints 'Hello    World. How are you?'
print(f"{int1:=8}") #prints '-    120'
print(f"This {str1:^12} is good") #prints 'This    World     is good'
print(f"The temperature is between {theta1:+} and {theta2:+} degrees celsius.") #prints 'The temperature is between -3 and +7 degrees celsius.'
print(f"The temperature is between {theta1:-} and {theta2:-} degrees celsius.") #prints 'The temperature is between -3 and 7 degrees celsius.'
print(f"The temperature is between {theta1: } and {theta2: } degrees celsius.") #prints 'The temperature is between -3 and  7 degrees celsius.'
print(f"My bank balance is {balance:,} BDT") #prints 'My bank balance is 1,000,000 BDT'
print(f"Light speed is {accurate_lightspeed:_}") #prints 'Light speed is 299_792_458'
print()
