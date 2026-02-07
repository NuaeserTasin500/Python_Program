## OOP Inheritance

class Student:
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
    
    def showDetalis(self):
        print(f'Student name: {self.name}.\nRoll: {self.roll}.\nCGPA: {self.cgpa}')

student1 = Student("John", 34, 3.75)
student1.showDetalis()
print()

student2 = Student("Steve", 35, 4.00)
student2.showDetalis()
print()

#Suppose Steve has scholarship
#Now we want to add scholarship in student option. But unfortunately we can't. Because student class is used.
#Changing an used class could affect objects.
#So we need to create inheritance class as 'scholarship_Student'

#Syntax of inheritance:- class inheritance_classname(parent_classname)
#Student is a parent class

class scholarship_Student(Student):
    def scholarship(self, scholarship_name):
        self.scholarship_name = scholarship_name
    
    def showScholar(self):
        print(f"{self.name} has {self.scholarship_name} scholarship")


student2 = scholarship_Student("Steve", 35, 4.00)
student2.showDetalis()
student2.scholarship("Full-Free")
student2.showScholar()

#Here scholarship_Student is an inherited class
