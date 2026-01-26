## Lambda function
# in Python programming, Lambda functions are single-expression functions, which let us write small functions more concisely.
 
double = lambda x: x * 2 
print(double(5)) # prints '10' 
print()

# This double = lambda x: x * 2 is equivalent to:-
# def double(x): 
# return x * 2 
# 
# Lambda is shorter, and better for defining simple function

cube = lambda x: x ** 3
a = cube(3) #store '27'
print(a) #prints '27'
print()


#We can input multiple values in lambda function
#for example: three values' average
average = lambda x, y, z : (x + y + z)/3
print(average(10, 11, 12)) #prints '11.0' as float
print(int(average(10, 11, 12))) #print '11' as int
print()



# Anonymous lambda function
#In Python programming, anonymous lambda functioare defined without a name. 
#It is used for one-time tasks.
print((lambda x: x ** 2)(3)) #prints '9'
print()
#Here (anonymous lambda function)(value passed to the anonymous lambda function) 



# Lambda Function passing to function
#We can pass lambda function to a function
def function(passed_function, value):
    return 10 + passed_function(value)

square = lambda x : x ** 2
print(function(square, 6)) #prints '46' 
#We can also use anonymous functions here
print(function(lambda x: x**3, 6)) #prints '226'
print()


# Lambda function passing to another lambda function
func1 = lambda a_func, value: a_func(value)
func2 = lambda x: 10*x
print(func1(func2, 12)) #prints '120'
print()


# Conditional Lambda function
cond = lambda x: x > 3
print(cond(3)) #prints 'False'
print(cond(4)) #prints 'True'
