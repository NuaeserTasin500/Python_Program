## OOP Multiple Inheritance

#In Python programming, multiple inheritance allows a child class to inherit multiple parents
#Syntax of multiple inheritance:- class child_classname(parent_classname_1, parent_classname_2, ...)

#We have learned in single inheritance that cat and dogs are child classes of Animal parent class.
#Now suppose, we have added another domestic pet animal species goat. So we have three species: cat, dog, and goat 
#Now we will give diet attributes to them that as that species is carnivore, harbivore or omnivore.
#So we will create another parent class 'diet'. Now there are two parent classes - Animal and Diet

class Animal:
    species_legs = 4 #every animal species has four legs 
    def __init__(self, species_name, species_sound):
        self.species_name = species_name
        self.species_sound = species_sound

    def info(self):
        return f"Species_name: {self.species_name}\nLegs: {self.species_legs}\nSound: {self.species_sound}\n"

class Diet:
    def __init__(self, diet_name):
        self.diet_name = diet_name
    
    def info(self):
        return f'Diet: {self.diet_name}\n'

#For multiple inheritance, we can't use super().__init__() or super().info() becuase both 'Animal' and 'Diet' has __init__() and info()
#we need to use Animal.__init__() and Animal.info() for Animal parent class (with using self also) <AI>
#we need to use Diet.__init__() and Diet.info() for Diet parent class (with using self also) <AI>

#Cat is here a child class of Animal
class Cat(Animal, Diet): 
    species_name = "Cat" 
    species_sound = "Meow"
    diet_name = "Carnivore"
    def __init__(self, pet_name): 
        self.pet_name = pet_name
        Animal.__init__(self, self.species_name, self.species_sound) 
        Diet.__init__(self, self.diet_name)

    def __str__(self):
        return f"Name: {self.pet_name}\n{Animal.info(self)}{Diet.info(self)}" 
    

#Dog is here a child class of Animal
class Dog(Animal, Diet):
    species_name = "Dog"
    species_sound = "Woof"
    diet_name = "Carnivore"
    def __init__(self, pet_name):
        self.pet_name = pet_name
        Animal.__init__(self, self.species_name, self.species_sound)
        Diet.__init__(self, self.diet_name)
    
    def __str__(self):
        return f"Name: {self.pet_name}\n{Animal.info(self)}{Diet.info(self)}" 
        
#Goat is here a child class of Animal
class Goat(Animal, Diet):
    species_name = "Goat"
    species_sound = "Bleat"
    diet_name = "Harbivore"
    def __init__(self, pet_name):
        self.pet_name = pet_name
        Animal.__init__(self, self.species_name, self.species_sound)
        Diet.__init__(self, self.diet_name)
    
    def __str__(self):
        return f"Name: {self.pet_name}\n{Animal.info(self)}{Diet.info(self)}" 


# Now let's create some cat, dog and goat objects here
tom = Cat("Tom")
bella = Cat("Bella")
spike = Dog("Spike")
max = Dog("Max")
stewart = Goat("Stewart")
hazel = Goat("Hazel")
print(tom) #prints 'Name: Tom <newline> Species_name: Cat <newline> Legs: 4 <newline> Sound: Meow <newline> Diet: Carnivore'
print(bella) #prints 'Name: Tom <newline> Species_name: Cat <newline> Legs: 4 <newline> Sound: Meow <newline> Diet: Carnivore'
print(spike) #prints 'Name: Spike <newline> Species_name: Dog <newline> Legs: 4 <newline> Sound: Woof <newline> Diet: Carnivore'
print(max) #prints 'Name: Max <newline> Species_name: Dog <newline> Legs: 4 <newline> Sound: Woof <newline> Diet: Carnivore'
print(stewart) #prints 'Name: Stewart <newline> Species_name: Goat <newline> Legs: 4 <newline> Sound: Bleat <newline> Diet: Harbivore'
print(hazel) #prints 'Name: Hazel <newline> Species_name: Goat <newline> Legs: 4 <newline> Sound: Bleat <newline> Diet: Harbivore'

 


# Multiple Inheritence priority and MRO (Method Resolution Order)
#Let's suppose that, A and B are parent classes and C is a child class inherited by A and B
class A:
    def __init__(self, input):
        self.input = input

    def show(self):
        return f"{self.input} is in class A"

class B:
    def __init__(self, input):
        self.input = input

    def show(self):
        return f"{self.input} is in class B"
    
class C(A, B):
    def __init(self, input):
        self.input = input


#now, let's make object of C class 
obj1 = C(10) #here 10 is an input
print(obj1.show()) #prints '10 is in class A' 

#here we can see that C class prioritize A parent over B, that's why obj1.show() shows '10 is in class A'
#because in class C(A, B), here A is first, that's why A gets priority
#if we make another child class D, where B is first -
class D(B, A):
    def __init(self, input):
        self.input = input

#and create object of D class
obj2 = D(10)
print(obj2.show()) #now it prints '10 is in class B' because B is first in D
print()


# .mro() (Method Resolution Order)
#let's check mro of both obj1 and obj2 
print(C.mro()) #it shows [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>] which means A has priority before B
print(D.mro()) #it shows [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>] which means B has priority before A
print()


#So how to solve this problem?
#Ans:
#1) If we want to print two parent classes' return function simultanously, then we must use __str__ and method overriding in child class and use both show function in return f string 
#(i.e Animal and Diet parent classes both have same return function info(), but we have used them by __str__ and method overriding, mentioned them in child classes)
#2) If we don't want to print two parent classes' return function simultanously, then we must give different name of return functions
#i.e. suppose we will make parent class A1, B1 and one child class C1, where A1's return function is show1() and B1's return function is show2()
class A1:
    def __init__(self, input):
        self.input = input 

    def show1(self):
        return f"{self.input} is in class A1" 
    
class B1:
    def __init__(self, input):
        self.input = input

    def show2(self):
        return f"{self.input} is in class B1"
    
class C1(A1, B1):
    def __init__(self, input):
        self.input = input

#now let's create obj3 which is the object of class C1
obj3 = C1(10)
print(obj3.show1()) #prints '10 is in class A1'
print(obj3.show2()) #prints '10 is in class B1'
#so this is how we can print both parent classes' returns differently! 
