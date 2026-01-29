## Decorators
#In Python programming, decorators are powerful tool that allow us to modify the behavior of function

def greeting(fx): #greeting is a decorator and fx is a function parameter
    def modified_function():
        print("Good Morning")
        fx()
        print("Thanks for this decorator")
    return modified_function


@greeting #func1 will go to the greeting decorator
def func1():
    print("Hello World")

def func2(): #func2 won't go to the greeting decorator because it has no @greeting
    print("Hello World")


func1() #prints Hello World with decorators
print()
func2() #prints only 'Hello World'
print()
print()


# for functions with parameters, decorator *args and **kwargs to accept any argument
# Just remember these *args and **kwargs things in your brain right now. I will later explain these *args and **kwargs
def greeting002(fx):
    def modified_function002(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Well done!") 
    return modified_function002

@greeting002
def add(a, b):
    print(a + b)

@greeting002
def func3():
    print("Python is awesome")

add(3, 4) #prints 7 with decorators
print()
func3() #prints 'Python is awesome' with decorators. It means it will be work for string also
print()
print()



# Decoration working for 'Returning functions' <S>
def greeting003(fx):
    def modified_function003(*args, **kwargs):
        print("YES!")
        result = fx(*args, **kwargs)
        print("BRAVO!") 
        return result
    return modified_function003

@greeting003
def sub(a, b):
    return a - b

@greeting003
def strreturn():
    return f'E=mc^2'

@greeting003
def strprint(): #non-returning function for test
    print("F=ma")


print(sub(12, 2)) #prints 2 with decorators
print()
print(strreturn()) #prints E=mc^2 with decorators
print()
strprint() #prints F=ma with decorators! Even non-returning functions can work here! 
print()
