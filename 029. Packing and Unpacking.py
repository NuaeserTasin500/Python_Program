## Packing and Unpacking data
#In Python, we can pack data as tuple, dictionary; and we can unpack tuple, list, dictionary
#For packing, we can pack data as tuple, dictionary (not set, list)
#For unpacking, we can unpack tuple, set, list, dictionary


# Packing data as tuple
def pack(*nums):
    print(f'Packed: {nums}')

pack(1, 2, 3) #prints 'Packed: (1, 2, 3)'
print()



# Unpacked list, tuple etc data 
def unpack(a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

num = [1, 2, 3]
unpack(*num) #prints 'a = 1 <newline> b = 1 <newline> c = 1'
print()



# Packing as Dictionary
def pack_dict(**keyword_args):
    print(f'packed_dictionary: {keyword_args}')
    for k in keyword_args:
        print(f'Packed: {k} = {keyword_args[k]}')

pack_dict(name="John", age=46, occupation="Doctor") #prints 'packed_dictionary: {'name': 'John', 'age': 46, 'occupation': 'Doctor'}
#prints Packed: name = John <newline> Packed: age = 46 <newline> Packed: occupation = Doctor
print()


# Unpacking a dictionary
def unpacking_dict(name, age, occupation):
    print('Unpacking a dictionary')
    print(f'Name = {name}')
    print(f'Age = {age}')
    print(f'Occupation = {occupation}')

d = dict(name="Jill", age=30, occupation="Computer Operator")
unpacking_dict(**d) #prints 'Unpacking a dictionary <newline> Name = Jill <newline> Age = 30 <newline> Occupation = Computer Operator
