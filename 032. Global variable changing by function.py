## Global variable changing by function

x = 100 #global variable
print(f"x value is {x}") #prints 'x value is 100'

def func1():
    x = 4 #local variable
    print(f"x value is {x}")

func1() #prints 'x value is 4'
print(f"x value is {x}") #still prints 'x value is 100', and x won't be assigned as 4


# So question comes that how can we change global variable's value by using function.
# Well, we need to use 'global' word into the function

def func2():
    global x #declation for grabbing global variable x
    x = 5 # x will be assigned as 5 globally
    print(f"x value is {x}")

func2() #prints 'x value is 5'
print(f"x value is {x}") #prints 'x value is 5' successfully
