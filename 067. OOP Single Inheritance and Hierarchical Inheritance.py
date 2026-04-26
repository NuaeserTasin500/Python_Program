## OOP Single Inheritance and Hierarchical Inheritance

#Single Inheritance is as same as we have learned in 'OOP Inheritance' chapter 
#Syntax of single inheritance:- class child_classname(parent_classname)

#In OOP inheritance, we have learned that we can push student's important info to a parent class "Student" (name, roll, cgpa) etc and use child class "scholarship_Student" for updating scholarship to that student
#But in reality, we need to push important info to a child class where parent class remains as "Root".
#We have learned in Method overriding that we can push info to a child class and child class is really connect with parent root
#Still, we will learn again about this

#Suppose, we are making Animal class (which is parent root class) and child classes are cat, dog etc. 
#But we can create cat, dog objects etc by these child classes. These child classes has pet names too.

class Animal:
    species_legs = 4 #every animal species has four legs 
    def __init__(self, species_name, species_sound):
        self.species_name = species_name
        self.species_sound = species_sound

    def info(self):
        return f"Species_name: {self.species_name}\nLegs: {self.species_legs}\nSound: {self.species_sound}\n"


#Cat is a child class of Animal here
class Cat(Animal):
    species_name = "Cat"
    species_sound = "Meow"
    def __init__(self, pet_name):
        self.pet_name = pet_name
        super().__init__(self.species_name, self.species_sound) 

    def __str__(self):
        return f"Name: {self.pet_name}\n{super().info()}" 
    
#let's create a cat object
luna = Cat("Luna")
print(luna) #Name: Luna <newline> Species_name: Cat <newline> Legs: 4 <newline> Sound: Meow

#this is called single inheritance. 
#Single inheritance means one parent class has one child class
#Here one parent class "Animal" has one child class "Cat"

#Now let's make another child class "Dog"
#Dog is a child class of Animal here
class Dog(Animal):
    species_name = "Dog"
    species_sound = "Woof"
    def __init__(self, pet_name):
        self.pet_name = pet_name
        super().__init__(self.species_name, self.species_sound)
    
    def __str__(self):
        return f"Name: {self.pet_name}\n{super().info()}" 
        

# Now let's create some cat and dog objects here
tom = Cat("Tom")
bella = Cat("Bella")
spike = Dog("Spike")
max = Dog("Max")
print(tom) #prints 'Name: Tom <newline> Species_name: Cat <newline> Legs: 4 <newline> Sound: Meow'
print(bella) #prints 'Name: Tom <newline> Species_name: Cat <newline> Legs: 4 <newline> Sound: Meow'
print(spike) #prints 'Name: Spike <newline> Species_name: Dog <newline> Legs: 4 <newline> Sound: Woof'
print(max) #prints 'Name: Max <newline> Species_name: Dog <newline> Legs: 4 <newline> Sound: Woof'

#This is called Hierarchical inheritance
#Hierarchical inheritance means one parent class has multiple child classes
#Here one parent class "Animal" has two child classes "Cat" and "Dog"


#Here parent class 'Animal' works as root of dogs and cats, and we don't need to use this parent class directly.

