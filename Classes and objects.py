#Program-1: Creating a Simple Class and Object
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()


#Program-2: Class with an Initializer (__init__ Method)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person1 = Person("Alice", 30)
person1.introduce()


#Program-3: Instance Variables and Methods
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.show_details()
car2.show_details()


#Program-4: Class Variables
class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

emp1 = Employee("John", 50000)
emp2 = Employee("Sarah", 60000)

emp1.show_details()
emp2.show_details()


#Program-5: Private Attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.__balance}")

account = BankAccount("Alice", 1000)
account.show_balance()


#Program-6: Getters and Setters
class Student:
    def __init__(self, name, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid marks!")

student1 = Student("John", 85)
print("Marks:", student1.get_marks())

student1.set_marks(90)
print("Updated Marks:", student1.get_marks())


#Program-7: Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()


#Program-8: Method Overriding
class Bird:
    def speak(self):
        print("Bird chirps")

class Parrot(Bird):
    def speak(self):
        print("Parrot talks")

parrot = Parrot()
parrot.speak()


#Program-9: Polymorphism
class Cat:
    def sound(self):
        print("Cat meows")

class Cow:
    def sound(self):
        print("Cow moos")

def make_sound(animal):
    animal.sound()

cat = Cat()
cow = Cow()

make_sound(cat)
make_sound(cow)

#Program-10: Class with a Static Method
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

result = MathOperations.add(5, 3)
print("Sum:", result)