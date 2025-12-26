## String

name = "John"
friend = "Steve"
print("The friend of", name, "is", friend)
print()

#new line consumption in string variable
Poem = '''Twinkle Twinkle, Little Star
How I wonder what you are!
Up above the also high
Like a diamond in the sky
'''
print(Poem)
print()

#String's considered as array. So we can print every individual character by using []
person = "Jason"
print(person[0]) #first character of string is considered as 0
print(person[1])
print(person[2])
print(person[3])
print(person[4])
print()

#new line also considered as character.
twoperson = '''Jason
Malik'''
print(twoperson[4]) #print n
print(twoperson[5]) #print newline
print(twoperson[6]) #print M
print()



# String Length-wise print
names = "Jack, Sally"
print(names[0:]) #prints 'Jack, Sally'
print(names[0:1]) #prints 'J'
print(names[0:2]) #prints 'Ja'
print(names[0:4]) #prints 'Jack'
print(names[0:8]) #prints 'Jack, Sa'
print()
print(names[1:]) #prints 'ack, Sally'
print(names[1:2]) #prints 'a'
print(names[1:4]) #prints 'ack'
print(names[1:8]) #prints 'ack, Sa'
print()


# Getting length of a string
bird = "eagle"
len_bird = len(bird)
print(bird, "is a", len_bird, "letter word.")
print()


# Minus lengthwise
thing = "tissue"
print(len(thing))
print(thing[:-3]) #means thing[:len(thing)-3] = thing[:6-3] = thing[:3]
print()

# Making Strings uppercase and lowercase
str1 = "AbCdEfGh"
up_str1 = str1.upper() #convert it in uppercase
dn_str1 = str1.lower() #convert it in lowercase
print(str1)
print(up_str1)
print(dn_str1)
print()

# Checking uppercase and lowercase
bool1_up_str1 = up_str1.isupper()
print(bool1_up_str1) #prints 'True'
bool2_up_str1 = up_str1.islower()
print(bool2_up_str1) #prints 'False' because entire string is not in lower case
bool1_dn_str1 = dn_str1.isupper()
print(bool1_dn_str1) #prints 'False' because entire string is not in upper case
bool2_dn_str1 = dn_str1.islower()
print(bool2_dn_str1) #prints 'True'
print()

# Capitalization
sentence1 = "welcome to this tutorial"
sentence2 = sentence1.capitalize()
print(sentence1) #prints 'welcome to this tutorial'
print(sentence2) #prints 'Welcome to this tutorial'
print()




#Replacement
str2 = "John is a good boy"
str3 = str2.replace("John", "Sally")
print(str2) #prints 'John is a good boy'
print(str3) #prints 'Sally is a good boy'
print()


#Stripping by replacement
str4 = "!!!!!You!!!!!"
str5 = str4.replace("!", "\0") # \0 means null
print("Messy string: ", str4)
print("Cleared string: ", str5)
print()



#making string words as list elements by split()
sentence3 = "Hello! How are you?"
list1 = sentence3.split(" ")
print(list1)
print()

#center method
sentence4 = sentence3.center(50)
print(sentence4)
print()

#startswith and endswith
boolean1 = sentence3.endswith("you?")
boolean2 = sentence3.startswith("Hello!")
print(boolean1) #prints 'True'
print(boolean2) #prints 'False'
print()



#find
sentence5 = "Where are you going?"
idx1 = sentence5.find("are")
print(idx1) #prints '6' because 'are' word's 'a' is in 6th index
idx2 = sentence5.find("arehh")
print(idx2) #prints '-1' because 'arehh' isn't in sentence5 string
print()

#isalnum()
str6 = "WelcomeToTheGermany"
str6_bool = str6.isalnum()
print(str6_bool) #prints 'True'
str7 = "Welcome To The Germany"
str7_bool = str7.isalnum() 
print(str7_bool) #prints 'False' because isalnum() gives 'True' when entire string is based on a-z, A-Z, 0-9
print()

#isalpha
str6_alp = str6.isalpha()
print(str6_alp) #prints 'True'
str8 = "WelcomeToTheGermany00"
str8_alp = str8.isalpha()
print(str8_alp) #prints 'False' because isalpha() gives 'True' when entire string is based on a-z, A-Z. 
print()

#isprintable()
str9 = "Welcome to the Java programming"
str9_bool = str9.isprintable()
print(str9_bool) #prints 'True'
str10 = "Welcome to the Java programming\n"
str10_bool = str10.isprintable()
print(str10_bool) #prints 'False' because newline is invisible 
print()

#isspace()
str11 = "    "
str11_bool = str11.isspace()
print(str11_bool) #prints 'True'. Only having space or tab will be true
print()


#swapcase()
str12 = "English is an International Language"
str12_case = str12.swapcase()
print(str12_case) #prints str12 as uppercase is lowercase; and lowercase is uppercase
print()


#title()
str12 = "french is an european langauge"
str12_title = str12.title()
print(str12_title) #prints 'French Is An European Langauge'
print()

#Chcecking title
bool_str12 = str12.istitle()
print(bool_str12) #prints 'False' because str12 is not title
bool_str12title = str12_title.istitle()
print(bool_str12title) #prits 'True' because str12_title is title
print()

