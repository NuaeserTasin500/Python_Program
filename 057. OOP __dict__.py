## OOP __dict__
#The __dict__ dunder attribute in Python is a special built‑in dictionary that stores an object’s namespace.

class Student:
    schoolName = "ABC High School"
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa

    def info(self):
        print(f'Name: {self.name}\nRoll: {self.roll}\nCGPA: {self.cgpa}\nSchoolName: {self.schoolName}')

    
    @classmethod
    def changeSchool(cls, newSchool):
        cls.schoolName = newSchool

student1 = Student("John", 34, 3.75)
dict1 = student1.__dict__
print(dict1) #prints '{'name': 'John', 'roll': 34, 'cgpa': 3.75}'
