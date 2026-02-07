## OOP Static Method
#In Python programming, static methods are methods that belong to a class rather than an instance of the class.
#We can call static method independently, without using self 

class Sum:
    def __init__(self, num):
        self.num = num
    
    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b): #not needed 'self'
        return a + b

result = Sum.add(1, 2) #using independently, without making any object
print(result) #prints '3', not needed 'self' 
a = Sum(5)
a.addtonum(6)
print(a.num) #prints '11', needed 'self' and it is just update
