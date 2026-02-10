## Enumerate function


# Enumerate function for list
country = ["Afghanistan", "Pakistan", "Tajikistan", "Turkmenistan"]
for index, x in enumerate(country):
    print(f"{index}. {x}") 
print()
#it prints:-
# 0. Afghanistan
# 1. Pakistan
# 2. Tajikistan
# 3. Turkmenistan

#Here 'x' is loop variable of country list's each element and 'index' is loop variable of country list's index
#This is how enumerate works





# Enumerate function for tuple
towns = ('Tokyo', 'New York', 'Sydney', 'Cape Town')
for index, x in enumerate(towns):
    print(f"{index}. {x}") 
print()
#it prints:-
# 0. Tokyo
# 1. New York
# 2. Sydney
# 3. Cape Town




# Enumerate function for strings
str1 = 'tokyo'
for index, x in enumerate(str1):
    print(f"{index}. {x}") 
print()
#it prints:-
# 0. t
# 1. o
# 2. k
# 3. y
# 4. o



# Changing the start index
country = ["Afghanistan", "Pakistan", "Tajikistan", "Turkmenistan"]
for index, x in enumerate(country, start=1):
    print(f"{index}. {x}") 
print()
#it prints:-
# 1. Afghanistan
# 2. Pakistan
# 3. Tajikistan
# 4. Turkmenistan
