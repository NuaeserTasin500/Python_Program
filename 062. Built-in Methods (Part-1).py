## Built-in Methods (Part-1)
#Note: This topic is made by the help of AI and help(int) documentation
#<AI>



# .add()
#it adds an element in list and set
set1 = {1, 2, 3}
set1.add(4)
print(set1) #prints '{1, 2, 3, 4}'
print()



# .as_integer_ratio()
a2 = 10
a3 = 10.6
print((a2).as_integer_ratio()) #prints '(10, 1)'
print((a3).as_integer_ratio()) #prints some garbled numbers because a3 is not an integer
print()



# .bit_count()
#Number of ones in the binary representation of the absolute value of self. Also known as the population count.
a4 = 100
bitc = (a4).bit_count()
print(bitc) #prints '3'
print()



# .bit_length()
a5 = 298
bitl = (a5).bit_length()
print(bitl) #prints '9'
print()



# .conjugate()
#Returns the complex conjugate. For int, it just returns itself.
a6 = 10
cplx1 = (10+8j)
print((a6).conjugate()) #prints '10'
print((cplx1).conjugate()) #prints '(10-8j)'
print()



# .is_integer()
#Always returns True for int.
a7 = 1200
a8 = 12.24
print(a7.is_integer()) #prints 'True'
print(a8.is_integer()) #prints 'False' because a8 is not an Integer
print()



# .to_bytes()
#syntax: .to_bytes(length, byteorder, signed) 
#it converts the integer into a bytes representation.
#length: The number of bytes to use for the representation. An OverflowError occurs if the integer cannot fit in this size.
#byteorder: Determines how bytes are ordered.
#'big' used for Most significant byte comes first; and 'little' used for Least significant byte comes first.
# signed: (Optional) True for using two's complement to represent the number, allowing for negative integers.
a9 = 10940
a10 = -10940
data1 = (a10).to_bytes(2, 'big', signed=True) #used signed=True because a10 is a negative number [P.S. you can't use signed=False for a negative number]
print(data1) #prints 'b'\xd5D'' with two's complement 
data2 = (a9).to_bytes(2, 'big', signed=False) #used signed=False as no two's complement [P.S. for positive number, you can also use signed=True as two's complement]
print(data2) #prints 'b'*\xbc' with no two's complement
print()



# .from_bytes()
#syntax: .from_bytes(byte_data, byteorder, signed) 
#it converts the bytes representation into a integer.
#byteorder: Determines how bytes are ordered.
#'big' used for Most significant byte comes first; and 'little' used for Least significant byte comes first.
# signed: (Optional) True for using two's complement to represent the number, allowing for negative integers.
data3 = b'\xd5D' #this has two compliment and negative number
data4 = b'*\xbc'
a11 = int.from_bytes(data3, "big", signed=True) #you can use signed=False here but that would show definitely different value
print(a11) #prints '-10940'
a12 = int.from_bytes(data4, "big", signed=False) #you can use signed=True here and that would show same value
print(a12) #prints '10940'
print()







# ========================================================================= #
#Note: This topic is made by the help of AI and help(float) documentation
#<AI>



# .hex()
#Returns a hexadecimal representation of a float
a = -0.1
b = 1.343
print(a.hex()) #prints '-0x1.999999999999ap-4'
print(b.hex()) #prints '0x1.57ced916872b0p+0'
print()



# .fromhex()
#it is a class method which create a floating-point number from a hexadecimal string.
print(float.fromhex('0x1.ffffp10')) #prints '2047.984375'
print(float.fromhex('-0x1p-1074')) #prints '-5e-324'
print()



# ========================================================================= #
#Note: This topic is made by the help of AI and help(float) documentation
#<AI>



# .capitalize()
#Return a capitalized version of the string.
str1 = 'hello'
print(str1.capitalize()) #prints 'Hello'
print()



# .casefold()
#Return a version of the string suitable for caseless comparisons.
str2 = 'Straße'
print(str2.casefold()) #prints 'strasse'
print()



# .center()
#Return a centered string of length width.
#Syntax: .center(width, fillchar=' ')
str3 = 'hi'
print(str3.center(6, '-')) #prints '--hi--' which length is 6
print(str3.center(8, '=')) #prints '===hi===' which length is 8
print()



# .count()
#Return the number of non-overlapping occurrences of substring sub in string
#Syntax: .count(substring, start, end)
text1 = "banana"
#Count all 'a'
print(text1.count("a")) #prints '3'
#Count 'a' only in slice [1:5]
print(text1.count("a", 1, 5)) #prints '2'
#Count substring 'na'
print(text1.count("na")) #prints '2'
print()



# .encode()
#it converts a string into bytes using the specified encoding.
print(text1.encode("utf-8", errors='strict')) #prints 'b'banana''
print()



# .endswith(), .startswith()
#.endswith(): it checks if the string ends with the given suffix.
#.startswith(): it check if string starts with prefix.
print(text1.endswith("na")) #prints 'True'
print(text1.startswith("ba")) #prints 'True'
print()



# .expandtabs()
#replaces \t with spaces, using the given tab size.
print("a\tb".expandtabs(5)) #prints 'a    b'
print()



# .find(), rfind()
#.find() returns lowest index of substring, or -1 if not found.
#.rfind() returns highest index of substring, or -1 if not found.
text2 = "banana"
print(text2.find("na")) #prints '2'
print(text2.rfind("na")) #prints '4'



# .index(), .rindex()
#.index(): Like find, but raises ValueError if not found.
#.rindex():  Like rfind, but raises ValueError if not found.
print(text2.index("na")) #prints '2'
print(text2.rindex("na")) #prints '4'
print()




# .format()
#Performs string formatting with {} placeholders.
print("Hello, {}".format("world"))



# .format_map()
#Like format, but takes a dict directly.
print("{x} + {y}".format_map({"x":1,"y":2}))
print()



# .isalnum(), .isalpha(), .isascii(), .isdecimal(), .isdigit()
#.isalnum() returns 'True' if all characters are alphanumeric.
#.isalpha() returns 'True' if all characters are alphabetic
#.isascii() returns 'True' if all characters are ASCII
#.isdecimal() returns 'True' if all characters are decimal digits.
#.isdigit() returns 'True' if all characters are digits (includes superscripts, etc.). 
print("abc123".isalnum()) #prints 'True'
print("abcdef".isalpha()) #prints 'True'
print("abcdef".isascii()) #prints 'True'
print("123".isdecimal()) #prints 'True'
print("²".isdigit()) #prints 'True'
print()



# .isidentifier(), .isnumeric(), .isprintable(), .isspace()
#.isidentifier() returns True if the string is a valid Python identifier.
#.isnumeric() returns True if all characters are numeric (includes fractions, Roman numerals).
#.isprintable() returns True if all characters are printable.
#.isspace() returns True if all characters are whitespace.
print("var_name".isidentifier()) #prints 'True'
print("⅕".isnumeric()) #prints 'True'
print("hello".isprintable()) #prints 'True'
print(" ".isspace()) #prints 'True'
print()



# .islower(), .isupper()
#.islower() returns True if all cased characters are lowercase.
#.isupper() returns True if all cased characters are uppercase.
print("hello".islower()) #prints 'True'
print("HELLO".isupper()) #prints 'True'
print()



# .istitle()
#.istitle() returns True if string is title-cased.
print("Hello World".istitle()) #returns 'True'
print()



# .join()
#Concatenate strings with the caller as separator.
list1 = ['My', 'name', 'is', 'John']
str4 = " ".join(list1) 
print(list1)
print()



# .ljust(), .rjust()
#.ljust(): Left-justify string in a field.
#.rjust(): Right-justify string in a field.
#Syntax: .ljust(width, fillchar), .rjust(width, fillchar)
str5 = "Hi"
print(str5.ljust(6, "-")) #prints 'Hi----' by 6 length
print(str5.rjust(6, "-")) #prints '----Hi' by 6 length
print()



# .lower(), .upper(), .swapcase()
#.lower() makes a string in lowercase
#.upper() makes a string in uppercase
#.swapcase(): swaps the case of a string
str6 = "HELlo"
print(str6.lower()) #prints 'hello'
print(str6.upper()) #prints 'HELLO'
print(str6.swapcase()) #prints 'helLO'
print()



# .lstrip(), .rstrip(), strip()
#.lstrip(): Remove leading whitespace or given chars.
#.rstrip(): Remove trailing whitespace or chars.
#.strip(): Remove leading/trailing whitespace or chars.
str7 = " hi"
str8 = "hi "
str9 = " hi "
print(str7.lstrip()) #prints 'Hi'
print(str8.rstrip()) #prints 'Hi'
print(str9.strip()) #prints 'Hi'
print()



# .maketrans() [STATIC METHOD]
#creates a translation table (a dictionary mapping Unicode ordinals to their translations) which is then used by the str.translate() method to replace or remove characters in a string. 
text3 = "Hello Sam"
#Create a translation table to replace 'S', 'a', 'm' with 'J', 'o', 'n'
oldname = "Sam"
newname = "Jon"
replacement = str.maketrans(oldname, newname)
print(text3.translate(replacement)) #prints 'Hello Jon'
print()



# .partition(), .rpartition()
#.partition(): Split into 3 parts around first occurrence.
#.rpartition(): Like partition, but from the right.
str10 = "Hello=World"
str11 = "Hello=World=Go"
print(str10.partition('=')) #prints '('Hello', '=', 'World')'
print(str11.rpartition('=')) #prints '("Hello=World","=","Go")'
print()



# .removeprefix(), .removesuffix()
#.removeprefix(): Remove prefix if present.
#.removesuffix(): Remove suffix if present.
str12 = 'unhappy'
str13 = 'sadly'
print(str12.removeprefix('un')) #prints 'happy'
print(str13.removesuffix('ly')) #prints 'sad'
print()



# .replace()
#replace characters or substrings of a string
str14 = "Zig-Zag"
print(str14.replace('Z', 'S')) #prints 'Sig-Sag'
print()



# .rsplit(), .split()
#.rsplit(): Split from the right.
#.split(): Split from the left.
str15 = "a, b, c"
print(str15.rsplit(", ", 1)) #prints '["a,b","c"]'
print(str15.rsplit(", ", 2)) #prints '["a", "b", "c"]'
print(str15.split(", ", 1)) #prints '["a", "b, c"]'
print(str15.split(", ", 2)) #prints '["a", "b", "c"]'
print()



# .splitlines()
#Split at line breaks.
str16 = "a\nb"
list2 = str16.splitlines()
print(list2) #prints '["a", "b"]'
print()



# .title()
#Title-case words.
str17 = "hello world"
print(str17.title()) #print 'Hello World'
print()



# .translate()
#Map characters using a translation table.
print("abc".translate({97:65})) #print 'Abc'
print()



# .zfill()
#Pad with zeros on the left.
a13 = 42
print(str(a13).zfill(5)) #print 00042


