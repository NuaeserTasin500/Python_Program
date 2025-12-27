## Function

#declaring function by def
def thank_you():
    print("Thank you for this proceed.", end=" ")

#declaring function by def and arguments
def add(x, y):
    add_result = x + y
    return add_result

def mul(x, y):
    mul_result = x * y
    return mul_result



#After whatever I write here are considered as codes of main function
a = int(input("Enter first number: "))
print("You first number is", a, end=". ")
thank_you()
b = int(input("\nEnter second number: "))
thank_you()
print(a, "+", b, "=", add(a,b))
print(a, "*", b, "=", mul(a,b))
print("multiplying both results =" , mul(mul(a,b), add(a,b)))
thank_you()

#Just notice this, I don't need to write "Thank you for this proceed." sentence several times,
#rather I have just used thank_you function.
#also I have easily interpreted (a*b)*(a+b) as mul(mul(a,b), add(a,b))
#this is the advantages of using functions 
