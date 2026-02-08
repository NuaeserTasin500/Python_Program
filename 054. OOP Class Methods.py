## OOP Class Methods
#For changing class variables permanently, we can use @classmethod

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
student1.info()
print()
student1.changeSchool("DEF High School")
student1.info() #Shows "DEF High School"
print()
student2 = Student("Steve", 35, 4.00)
student2.info() #Still shows "DEF High School"
