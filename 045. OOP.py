## Object-Oriented Programming (OOP)
#Python is an object-oriented programming language like Java

# Classes and Objects in Pyhton OOP
class Student:
    name = "John"
    roll = 34
    cgpa = 3.75
    # For printing, you can't print a class directly outside the class.
    # That would show <__main__.Student object at 0x...>
    # You need to use a function with self parameter
    def info(self):
        print(f'Student name: {self.name}.\nRoll: {self.roll}.\nCGPA: {self.cgpa}')



john = Student() #creating 'john' object

john.info() #prints 'Student name: John.<newline>Roll: 34.<newline>CGPA: 3.75' as default
print()


# Changing name, roll, cgpa of class and print that
steve = Student() #creating 'steve' object
steve.name = "Steve"
steve.roll = 35
steve.cgpa = 4.00
steve.info() #prints 'Student name: Steve.<newline>Roll: 35.<newline>CGPA: 4.0' 
print()

# This shows the fundamental OOP workflow:
# 1. Creating objects
# 2. Modifying their attributes  
# 3. Accessing their methods
# Here 'john' and 'steve' are distinct objects with independent data
