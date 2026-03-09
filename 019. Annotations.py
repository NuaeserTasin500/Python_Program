## Annotations <SAWDT><AI>
#In python, we declare variables and create function parameteres without writing datatypes
#But in annotations, we can declare variables and arguements with writing datatypes

# Annotations for declaring variables
num1: int = 10
num2: float = 10.2
name: str = "Wasim"
one_answer: bool = True
positive_nums: list = [1, 2, 3, 4]
negative_nums: tuple = (-1, -2, -3, -4)
z: set = {-3, -2, -1, 0, 1, 2, 3}
comp_val: complex = (3+8j)
identity: dict = {'Name':'Sofia', 'Nationality':'Polish', 'Age':20}

print(num1) #prints '10'
print(num2) #prints '10.2'
print(name) #prints 'Wasim'
print(one_answer) #prints 'True'
print(positive_nums) #prints '[1, 2, 3, 4]'
print(negative_nums) #prints '(-1, -2, -3, -4)'
print(z) #prints '{-3, -2, -1, 0, 1, 2, 3}' (elements can be shuffled in set)
print(comp_val) #prints '(3+8j)'
print(identity) #prints '{'Name':'Sofia', 'Nationality':'Polish', 'Age': 20}'

print()



# Annotations for function
def add(x: int, y: int) -> int:
    #This means x should be integer and y should be integer, and return should be integer
    return x + y

print(add(10, 20)) #prints '30'

def mul(x: int, y: int) -> str:
    #This means x should be integer and y should be integer, and return should be string
    return x * y

print(mul(10, 20)) #prints '200' but it is integer!
print(type(mul(10,20))) #we have checked and it shows that the return type is integer!

#because, Annotations are type hints only; Python does not enforce them at runtime.
 

