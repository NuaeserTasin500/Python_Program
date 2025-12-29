# F-string
place = "London"
name = "Jack"
print(f"Hey, my name is {name} and I am from {place}")

# another method of of f-string
place = "America"
name = "Jill"
str1 = f"Hey, my name is {name} and I am from {place}"
print(str1)
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
print(txt14)
