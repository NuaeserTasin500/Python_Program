## OOP Access modifier

# Public Access Modifier
class Student:
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
    

student1 = Student("John", 34, 3.75)
print(student1.name) #prints 'John' because it is publically accessable
print()



# Private Access Modifier
class pr_Student:
    def __init__(self, name, roll, cgpa):
        self.__name = name #making private by (__)
        self.__roll = roll
        self.__cgpa = cgpa

student1 = pr_Student("John", 34, 3.75)
#print(student1.__name) will be error because we can not access directly
print(student1.__dir__()) #shows all attributes
print(student1._pr_Student__name) #prints 'John' as we can access indirectly
print()



# Protected Access Modifier
class po_Student:
    def __init__(self, name, roll, cgpa):
        self._name = name #making protected by (_)
        self._roll = roll
        self._cgpa = cgpa

student1 = po_Student("John", 34, 3.75)
print(student1._name) #Directly accessable 
