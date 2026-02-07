## OOP Instance vs Class Variables
#In Python OOP, Class variables are shared across all instances unless overridden.
#Instance variables are unique to each object.


class Student:
    #Suppose this Student class is only for 'ABC High School'
    #In this case we can declare class variable schoolName = "ABC High School"


    schoolName = "ABC High School" #This is a Class Variable
    def __init__(self, name, roll, cgpa):
        self.name = name #This is an Instance
        self.roll = roll #This is an Instance
        self.cgpa = cgpa #This is an Instance
        self.goodStudent = True #This is an Instance (Default)
    
    def info(self):
        print(f'Name: {self.name}\nRoll: {self.roll}\nCGPA: {self.cgpa}\nGood Student: {self.goodStudent}\nSchoolName: {self.schoolName}')

student1 = Student("John", 34, 3.75)
student1.info()
print()
student2 = Student("Steve", 35, 4.00)
student2.info()
print()

#Now suppose Steve is not a good student and he transferred in DEF High school
#In this case we can change schoolName class variable and goodStudent instance.


student2.schoolName = 'DEF High School'
student2.goodStudent = False
student2.info()
print()

#schoolName and goodStudent of John's info won't be changed after that
student1.info()
print()
