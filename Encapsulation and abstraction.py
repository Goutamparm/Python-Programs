#Program-1: Basic Encapsulation with Private Variables
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_details(self):
        return f"Name: {self.__name}, Age: {self.__age}"

student = Student("Alice", 21)
print(student.get_details())


#Program-2: Encapsulation with Getter and Setter Methods
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

employee = Employee("John", 50000)
print("Initial Salary:", employee.get_salary())
employee.set_salary(55000)
print("Updated Salary:", employee.get_salary())


#Program-3: Encapsulation with Property Decorators
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount

account = BankAccount(1000)
print("Initial Balance:", account.balance)
account.balance = 1500
print("Updated Balance:", account.balance)

#Program-4: Abstraction with Abstract Base Class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print("Circle Area:", circle.area())


#Program-5: Abstraction with Private Methods
class Robot:
    def __init__(self):
        self.__secret_code = "XYZ123"

    def greet(self):
        self.__show_secret()

    def __show_secret(self):
        print("Secret Code:", self.__secret_code)

robot = Robot()
robot.greet()


#Program-6: Encapsulation with Method Restrictions
class Library:
    def __init__(self, book_list):
        self.__book_list = book_list

    def get_books(self):
        return self.__book_list

library = Library(["Python 101", "Learn Django", "Machine Learning"])
print("Available Books:", library.get_books())


#Program-7: Encapsulation with Private Variables and Methods
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        return f"Name: {self.__name}, Age: {self.__age}"

    def __update_age(self, new_age):
        self.__age = new_age

person = Person("Mike", 30)
print(person.display())

#Program-8: Abstraction Using Abstract Class for a Vehicle
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine starting"

class Bike(Vehicle):
    def start(self):
        return "Bike engine starting"

car = Car()
bike = Bike()
print(car.start())
print(bike.start())


#Program-9: Encapsulation Example with Controlled Access
class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = Account("12345", 1000)
account.deposit(500)
account.withdraw(300)
print("Remaining Balance:", account.get_balance())

#Program-10: Combining Encapsulation and Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self):
        return f"Processing credit card payment of {self.amount}"

class PayPalPayment(Payment):
    def process_payment(self):
        return f"Processing PayPal payment of {self.amount}"

payment1 = CreditCardPayment(100)
payment2 = PayPalPayment(200)
print(payment1.process_payment())
print(payment2.process_payment())