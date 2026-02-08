## OOP Super Keyword
#In Python OOP, super keyword is used for calling parent class' methods.

class ParentClass:
    def parent_method(self):
        print("This is the parent method")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method")
        super().parent_method()

child_obj = ChildClass()
child_obj.child_method()
#prints 'This is the child method <newline> This is the parent method



