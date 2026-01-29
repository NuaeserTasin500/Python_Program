## OOP __init__ dunder method constructor
#We have known about how to create class, objects and changing value where name 'John' was default 
#Now we will use __init__ dunder method constructor so that we don't need to make John as default.

class Student:
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa

    def info(self):
        print(f"Student Name: {self.name}.\nRoll: {self.roll}.\nCGPA: {self.cgpa}.") 

#Now we will create two student object 'John' and 'Steve'
john = Student("John", 34, 3.75)
steve = Student("Steve", 35, 4.00)

#Now we will print their info 
john.info() #prints 'Student name: John.<newline>Roll: 34.<newline>CGPA: 3.75'
print()
steve.info() #prints 'Student name: Steve.<newline>Roll: 35.<newline>CGPA: 4.0'

