#Program-1: Polymorphism with a Common Method Name
class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)

#Program-2: Polymorphism with Built-in Functions
print(len("Hello"))
print(len([1, 2, 3, 4]))
print(len({"a": 1, "b": 2}))


#Program-3: Method Overriding in Single Inheritance
class Parent:
    def display(self):
        return "This is the parent class"

class Child(Parent):
    def display(self):
        return "This is the child class"

obj = Child()
print(obj.display())


#Program-4: Polymorphism with Inheritance
class Shape:
    def draw(self):
        return "Drawing a shape"

class Circle(Shape):
    def draw(self):
        return "Drawing a circle"

class Square(Shape):
    def draw(self):
        return "Drawing a square"

shapes = [Circle(), Square(), Shape()]
for shape in shapes:
    print(shape.draw())


#Program-5: Method Overriding with Constructor
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some sound"

class Bird(Animal):
    def sound(self):
        return f"{self.name} chirps"

bird = Bird("Parrot")
print(bird.sound())

#Program-6: Polymorphism with Abstract Classes
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())


#Program-7: Polymorphism with a Function as Argument
class Rectangle:
    def area(self, length, width):
        return length * width

class Circle:
    def area(self, radius):
        return 3.14 * radius * radius

def print_area(shape, *args):
    print(shape.area(*args))

rectangle = Rectangle()
circle = Circle()
print_area(rectangle, 5, 3)
print_area(circle, 4)


#Program-8: Polymorphism with Duck Typing
class Car:
    def start(self):
        return "Car started"

class Bike:
    def start(self):
        return "Bike started"

def start_vehicle(vehicle):
    print(vehicle.start())

car = Car()
bike = Bike()
start_vehicle(car)
start_vehicle(bike)


#Program-9: Method Overriding in Multiple Inheritance
class ClassA:
    def display(self):
        return "ClassA method"

class ClassB(ClassA):
    def display(self):
        return "ClassB method"

class ClassC(ClassA):
    def display(self):
        return "ClassC method"

class ClassD(ClassB, ClassC):
    pass

obj = ClassD()
print(obj.display())

#Program-10: Polymorphism with Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2
print(result)