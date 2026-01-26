## Function

#declaring function by def
def thank_you():
    print("Thank you for this proceed.", end=" ")

#declaring function by def and arguments
def add(x, y):
    add_result = x + y
    return add_result

def mul(x, y):
    return x * y #you can return result of mathematical calculation without using variable




#After whatever I write here are considered as codes of main function
a = int(input("Enter first number: "))
print("You first number is", a, end=". ")
thank_you()
b = int(input("\nEnter second number: "))
print("You second number is", a, end=". ")
thank_you()
print()
print(a, "+", b, "=", add(a,b))
print(a, "*", b, "=", mul(a,b))
print("multiplying both results =" , mul(mul(a,b), add(a,b)))
thank_you()

#Just notice this, I don't need to write "Thank you for this proceed." sentence several times,
#rather I have just used thank_you function.
#also I have easily interpreted (a*b)*(a+b) as mul(mul(a,b), add(a,b))
#these are the advantages of using functions 


#if I make another function here then it won't be considered as a part of main function
def cheers():
    return "You are good in mathematics" #return string without print

#after whatever I write will be considered as main function
print(cheers())

#it means you can make function everywhere




# ============================================================================= #



# Store function's return in a variable
def double(x):
    return 2 * x

number1 = double(2) #stored a functional return in a variable
print(number1) #prints '4'  

number2 = 10
number3 = double(number2)
print("The number of", number2, "is", number3) #prints 'The number of 10 is 20'
print()




# Condition Return Function <S>
#In Python, if we return condition in function, it will give true or false
def even(x):
    return x % 2 == 0

print(even(1)) #prints 'False'
print(even(10)) #prints 'True'
