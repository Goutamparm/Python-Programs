#Program-1: Single Inheritance: Basic Example
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof! Woof!"

dog = Dog()
print(dog.sound())
print(dog.bark())


#Program-2: Single Inheritance with Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

emp = Employee("Alice", 30)
print(emp.display())


#Program-3: Single Inheritance with Method Overriding
class Vehicle:
    def fuel(self):
        return "Diesel"

class Car(Vehicle):
    def fuel(self):
        return "Petrol"

my_car = Car()
print(my_car.fuel())


#Program-4: Multiple Inheritance: Basic Example
class Father:
    def height(self):
        return "Tall"

class Mother:
    def eye_color(self):
        return "Brown"

class Child(Father, Mother):
    pass

child = Child()
print("Height:", child.height())
print("Eye Color:", child.eye_color())


#Program-5: Multiple Inheritance with Constructor Initialization
class A:
    def __init__(self):
        print("Class A Constructor")

class B:
    def __init__(self):
        print("Class B Constructor")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Class C Constructor")

c = C()


#Program-6: Method Resolution Order (MRO) in Multiple Inheritance
class X:
    def method(self):
        print("Method from X")

class Y(X):
    def method(self):
        print("Method from Y")

class Z(X):
    def method(self):
        print("Method from Z")

class W(Y, Z):
    pass

w = W()
w.method()
print(W.mro())


#Program-7: Single Inheritance: Accessing Parent Class Method
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")
        super().show()

child = Child()
child.show()


#Program-8: Multiple Inheritance with Same Method Name in Parent Classes
class Base1:
    def greet(self):
        print("Hello from Base1")

class Base2:
    def greet(self):
        print("Hello from Base2")

class Derived(Base1, Base2):
    pass

d = Derived()
d.greet()


#Program-9: Single Inheritance with Private Variables
class Base:
    def __init__(self):
        self.__private_var = "Private Variable"

    def get_private_var(self):
        return self.__private_var

class Derived(Base):
    pass

d = Derived()
print(d.get_private_var())

#Program-10: Multiple Inheritance with Different Functionality
class Engine:
    def start(self):
        return "Engine started"

class Radio:
    def play_music(self):
        return "Playing music"

class Car(Engine, Radio):
    def drive(self):
        return "Car is driving"

my_car = Car()
print(my_car.start())
print(my_car.play_music())
print(my_car.drive())