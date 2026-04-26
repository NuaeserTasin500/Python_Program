## OOP Multilevel Inheritance
#Multilevel Inheritance is an OOP concept where a class is derived from a child class. 
#For example: class A (parent) --> class B (child) --> class C (derived from child class B!)
#Here class A is indirect parent class of class C


#Suppose our parent (root) class is Technology, its derived class is Smartphone
#Smartphone's derived class is Android and iPhone
#Think it like: Techonlogy --> Smartphone --> Android (Android phone is a type of a Smartphone and Smartphone is a technology)
#Similarly: Technology --> Smartphone --> iPhone (iPhone is a type of a Smartphone and Smartphone is a technology)  

class Technology:
    def __init__(self, tech_name):
        self.tech_name = tech_name
    def __str__(self):
        return f"{self.tech_name} is a technology\n"

class Smartphone(Technology):
    def __init__(self, smartphone_type):
        self.smartphone_type = smartphone_type
        super().__init__("Smartphone")
    def __str__(self):
        return f"Smartphone type: {self.smartphone_type}\n{super().__str__()}"
    
class Android(Smartphone):
    def __init__(self, brand_name, user_name, imei_number):
        self.brand_name = brand_name
        self.user_name = user_name
        self.imei_number = imei_number
        super().__init__("Android")
    def __str__(self):
        return f"Brand name: {self.brand_name}\nUsername: {self.user_name}\nIMEI: {self.imei_number}\n{super().__str__()}"
    
class IPhone(Smartphone):
    def __init__(self, user_name, imei_number):
        self.brand_name = "Apple"
        self.user_name = user_name
        self.imei_number = imei_number
        super().__init__("iPhone")
    def __str__(self):
        return f"Brand name: {self.brand_name}\nUsername: {self.user_name}\nIMEI: {self.imei_number}\n{super().__str__()}"
    
user222 = Android("Realme", "user222", 43040430)
user405 = IPhone("user405", 49923839)
samuel = Android("Oppo", "Samuel", 39494494)
print(user222) #prints 'Brand name: Realme <newline> Username: user222 <newline> IMEI: 43040430 <newline> Smartphone type: Android <newline> Smartphone is a technology'
print(user405) #prints 'Brand name: Apple <newline> Username: user405 <newline> IMEI: 49923839 <newline> Smartphone type: iPhone <newline> Smartphone is a technology'
print(samuel) #prints 'Brand name: Oppo <newline> Username: Samuel <newline> IMEI: 39494494 <newline> Smartphone type: Android <newline> Smartphone is a technology'


#So this is how multilevel inheritance works


# MRO of multilevel inheritance
#Let's check the MRO of Android
print(Android.mro()) #prints '[<class '__main__.Android'>, <class '__main__.Smartphone'>, <class '__main__.Technology'>, <class 'object'>]'

