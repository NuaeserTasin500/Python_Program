## OOP Dunder methods
#__init, __len__, __str__, __repr__ are dunder methods of OOP
class Student:
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
    
    def showDetalis(self):
        print(f'Student name: {self.name}.\nRoll: {self.roll}.\nCGPA: {self.cgpa}')

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self):
        return f"The name of the student is {self.name}"
    
    def __repr__(self):
        return f"{self.name}'s roll is {self.roll}"
    


student1 = Student("John", 34, 3.75)
print(len(student1)) #prints '4' which is the length of John name
print(student1) #prints 'The name of the student is {self.name}' as __str__ 
print(str(student1)) #still prints 'The name of the student is {self.name}'
print(repr(student1)) #prints 'John's roll is 34'
