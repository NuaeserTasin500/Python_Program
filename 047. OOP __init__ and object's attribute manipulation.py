## OOP __init__ and object's attribute manipulation

# ================================================ #

# OOP __init__ dunder method constructor

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
print()


# ======================================================= #

# Object's attribute manipulation
#in python - self.name, self.roll etc are attributes.
#we can manipulate that

class Teacher:
    def __init__(self, name, subject):
        self.name = name #self.name is an attribute
        self.subject = subject #self.subject is an attribute

    def info(self):
        print(f"Teacher Name: {self.name}.\nSubject: {self.subject}.")
    
#Now we will create two teacher object 'Henry' and 'Bruce'
henry = Teacher("Henry", "English")
bruce = Teacher("Bruce", "Mathematics")

#without using info(), we can print their attributes individually
print(f"{henry.name} teaches {henry.subject}") #prints 'Henry teaches English'
print(f"{bruce.name} teaches {bruce.subject}") #prints 'Bruce teaches Mathematics'

#we can change attribute's values too
#suppose we want to make Bruce's subject as "Physics"
bruce.subject = "Physics"
print(f"{bruce.name} teaches {bruce.subject}") #prints 'Bruce teaches Physics'. It has changed!
print()

#even using info() would say same thing!
bruce.info() #prints 'Teacher Name: Bruce.<newline>Subject: Physics.'
