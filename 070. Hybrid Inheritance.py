## OOP Hybrid Inheritance
#In Python Programming, hybrid inheritance is a type of inheritance where combines two or more type of inheritance


#For example: In this code, ChildClass_1 and ChildClass_2 are inherited by ParentClass which is hierarchical inheritance
#But, Hybrid_Class is inherited by ChildClass_1 and ChildClass_2 which is multiple inheritance
#this hierarchical inheritance and multiple inheritance together have made hybrid inheritance
class ParentClass:
    pass

class ChildClass_1(ParentClass):
    pass

class ChildClass_2(ParentClass):
    pass

class Hybrid_Class(ChildClass_1, ChildClass_2):
    pass
