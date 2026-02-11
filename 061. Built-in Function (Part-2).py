## Built-in Function (Part-2)
#Found from: https://docs.python.org/3/library/functions.html
#and https://dev.to/onyxwizard/python-built-in-functions-ultimate-cheat-sheet-6n0


# id()
#returns memory address of object
str1 = "hello"
print(id(str1)) #return address of str1
print()



# input()
#take input from user
name = input("Enter your name: ")
print(f"Your name is {name}")
print()



# int()
#converting values as integer
a = 10.5
b = "100"
print(int(a)) #prints '10.5'
print(int(b)) #prints '100'
print()



# isinstance()
#Returns True if value fullfilled the datatype
print(isinstance(5, int)) #prints 'True' because 5 is an integer
print(isinstance(10, float)) #prints 'False' becuase 10 is not an float
print(isinstance(10.5, float)) #prints 'True' because 10.5 is an float
print()



# issubclass() 
#Returns True if class is subclass
class Student:
    def __init__(self, std_name, std_roll, std_cgpa):
        self.std_name = std_name
        self.std_roll = std_roll
        self.std_cgpa = std_cgpa
    
    def info(self):
        print(f"Name: {self.std_name}\nRoll: {self.std_roll}\nCGPA: {self.std_cgpa}")
    
class Scholarship_Student(Student):
    def scholarship(self, schol_name):
        self.schol_name = schol_name

    def info_schol(self):
        print(f"{self.std_name} has {self.schol_name} scholarship")

class Employee:
    def __init__(self, emp_name, emp_age):
        self.emp_name = emp_name
        self.emp_age = emp_age 
    
    def emp_info(self):
        print(f"Name: {self.std_name}\nRoll: {self.std_roll}\nCGPA: {self.std_cgpa}")

print(issubclass(Scholarship_Student, Student)) #prints 'True' because Scholarship_Student is an subclass of Student by inheritance
print(issubclass(Employee, Student)) #prints 'False' because Employee is not an subclass of Student
print()



# iter() and next()
#iter() returns elements of iteration object
#next() helps this iteration
list1 = [1, 2, 3]
iter1 = iter(list1)
print(next(iter1)) #prints '1'
print(next(iter1)) #prints '2'
print(next(iter1)) #prints '3'
print()



# len()
#returns length of a string
str2 = "Bangladesh"
len1 = len(str2)
print(len1) #prints '10'
print()



# list()
#it converts to list
tuple1 = (1, 2, 3)
list2 = list(tuple1)
print(tuple1) #prints [1, 2, 3]
print()



# locals()
#returns local variable dictionary
print(locals()) #prints '{'__name__': '__main__', '__doc__': None, '__package__': None, .....' something
print()



# map()
#it applies a given function to every elements of an iterable (i.e. list, tuple, etc.) and returns a map object.
tuple_a = (100, 200, 300, 400, 500)
tuple_b = tuple(map(lambda x: x/100, tuple_a))
print(tuple_b) #prints '(1.0, 2.0, 3.0, 4.0, 5.0)'
print()



# max() and min()
#max() returns maximum value where min() returns minimum value
list3 = [1, 2, 3, 4, 5]
print(max(list3)) #prints '5'
print(min(list3)) #prints '1'
print()



# memoryview()
#access internal data without copying
mv1 = memoryview(b"Hello")
print(mv1) #prints '<memory at 0x.....>' something
print()


# object()
#it returns a new featureless object
obj = object()
print(obj) #prints '<object object at 0x......>' something
print()



# oct()
#it returns octal representation
a = 10
print(oct(a)) #prints '0o12'
print()



# open()
#it opens file. Right now I can't show this method



# ord()
#it returns ASCII Code for a character
char1 = 'A'
print(ord(char1)) #prints '65'
print()



# pow()
#it raises a number to a power
a1 = pow(10, 3) #it means 10^3 
print(a1) #prints '1000'
print()



# print()
#we already knows that



# range()
#creates sequence of numbers
rg = range(1, 10) #1, 2, 3, 4, 5, 6, 7, 8, 9
list4 = list(rg) #it creates [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list4) #prints '[1, 2, 3, 4, 5, 6, 7, 8, 9]'



# repr()
#returns string representation
a = 10
print(a) #prints '10' as integer
b = repr(a)
print(b) #prints '10' as string
print(type(b)) #shows <class 'str'> because using repr() returns string representation of 'a' variable
print()



# reversed()
#it makes iterator's elements as reversed
list5 = [10, 11, 12, 13, 14, 15]
tuple2 = (20, 22, 24, 26, 28)
rev_list5 = list(reversed(list5))
rev_tuple2 = tuple(reversed(tuple2))
print(rev_list5) #prints '[15, 14, 13, 12, 11, 10]'
print(rev_tuple2) #prints '(28, 26, 24, 22, 20)'
print()



# round()
#rounds a float number
a = 12.452397
print(round(a, 1)) #prints '12.5' 
print(round(a, 2)) #prints '12.45'
print(round(a, 3)) #prints '12.452'
print(round(a, 4)) #prints '12.4524'
print()


# set()
#Creates a set
set1 = set([1, 2, 3])
print(set1) #prints '{1, 2, 3}' or element can't be in order
print()



# setattr()
#it sets an attribute of an object
class Car:
    pass

setattr(Car, "color", "blue")
print(Car.color) #prints 'blue'
print()



# slice()
#represent slicing
a = [0, 1, 2, 3, 4, 5]
s = slice(1, 4) #slicing 1 to 4-1=3; so 1, 2, 3
print(a[s]) #prints '[1, 2, 3]' because slice(1, 4) means 1 to 3, so a[1], a[2], a[3]
s1 = slice(0, 2) #slicing 0 to 2-1=1; so 0, 1
print(a[s1]) #prints '[0, 1]' because slice(0, 2) means 0 to 2, so a[0], a[1]

#we can use steps for slicing as slice(start, stop, steps)
s2 = slice(0, 4, 2) #slicing 0 to 4-1=3 by 2 steps; so 0, 2
print(a[s2]) #prints '[0, 2]' because slice(0, 4, 2) means 0 to 3 by 2 steps, so a[0], a[2]
print()



# sorted()
#returns sorted list
list6 = [100, 65, 73, 50, 94, 99, 30]
sort_list6 = sorted(list6)
print(sort_list6)
print()



# sum()
#it adds all items
print(sum([1, 2, 3, 4])) #prints '10'
print(sum((10, 11, 12, 13))) #prints '46'
print()



# super()
#it calls parent class method, and we have seen that in OOP



# tuple()
#it creats tuple
list7 = [1, 2, 3, 4]
tuple3 = tuple(list7)
print(tuple3) #prints '(1, 2, 3, 4)'
print()



# type()
#returns type() of object
aaa = 300
print(type(aaa)) #prints '<class 'int'>'
print()



# vars()
#returns dictionary of an object
class Student2:
    def __init__(self, std1_name, std1_roll, std1_cgpa):
        self.std1_name = std1_name
        self.std1_roll = std1_roll
        self.std1_cgpa = std1_cgpa
    
    def showDetalis(self):
        print(f'Student name: {self.std1_name}.\nRoll: {self.std1_roll}.\nCGPA: {self.std1_cgpa}')

std_1 = Student2("John", 34, 3.79)
dict_std_1 = vars(std_1) 
print(dict_std_1) #prints '{'std1_name': 'John', 'std1_roll': 34, 'std1_cgpa': 3.79}'
print()



# zip()
#it pairs items from multiple iterables
list8 = [1, 2]
list9 = ['a', 'b']
zip_process = zip(list8, list9)
zip_list = list(zip_process)
print(zip_list) #prints '[(1, 'a'), (2, 'b')]'
