## OOP Method Overriding
#In Python programming, Method Overriding is a feature that allows to redefine a method in a child class.

#Suppose, we want to make classes of 3D objects which will show the volume of them
#Now a 3D object's volume is normally cubic (length * width * height).
#So shape's default thing will be length * width * height
#As a result, Shape is now default and parent class which determines volume as length * width * height 
class Shape:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def volume(self):
        return self.length * self.width * self.height

#Now we want to make subclass of 3D default object. Suppose, we want to make subclass of Sphere
#But, wait a sec.... Sphere has no length, width, height. It has only radius.
#Now we will use our common sense. 
#Since we have said that 3D object's volume is normally cubic, so for sphere, we can use 'Shape' default class as three times of radius multiplication (r * r * r)
#And we know that Sphere's volume is (4 / 3) * 3.14 * r * r * r
#So we will push the radius into default 'Shape' class by super() keyword 
#and determine Sphere's volume by default 'Shape' class by super() keyword
#This is called Method Overriding
class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius, radius)

    def volume(self):
        return (4 / 3) * 3.14 * super().volume()

sphere001 = Sphere(5)
print(sphere001.volume()) #prints '523.3333333333334' which is the volume of the sphere

#This is how we can create more subclasses for 3D objects

#Cuboid
class Cuboid(Shape):
    def __init__(self, length, width, height): #Same as Shape parent class, but Shape is default, and cuboid is a subclass
        self.length = length
        self.width = width
        self.height = height
        super().__init__(length, width, height)
    
    def volume(self):
        return super().volume()
    
#Cube
class Cube(Shape):
    def __init__(self, side): #Cube's length, width, height are identical and called as side
        self.side = side
        super().__init__(side, side, side)
    
    def volume(self):
        return super().volume()
    
#Cylinder
class Cylinder(Shape):
    def __init__(self, radius, height): 
        self.radius = radius
        self.height = height
        super().__init__(radius, radius, height) 
    
    def volume(self):
        return 3.14 * super().volume()
    
#Cone
class Cone(Shape):
    def __init__(self, radius, height): 
        self.radius = radius
        self.height = height
        super().__init__(radius, radius, height) 
    
    def volume(self):
        return (1 / 3) * 3.14 * super().volume()
    

#Now lets test
cone100 = Cone(5, 10)
print(f"If cone's radius is {cone100.radius} and height is {cone100.height}, then it's volume is {cone100.volume()}")

cuboid100 = Cuboid(7, 12, 15)
print(f"If cuboid's length is {cuboid100.length}, width is {cuboid100.width} and height is {cone100.height}, then it's volume is {cuboid100.volume()}")

cube100 = Cube(11)
print(f"If cube's length is {cube100.side}, then it's volume is {cube100.volume()}")

cylinder100 = Cylinder(6, 16)
print(f"If cube's radius is {cylinder100.radius} and height is {cylinder100.height}, then it's volume is {cylinder100.volume()}")
