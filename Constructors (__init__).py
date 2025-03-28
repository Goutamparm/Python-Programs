#Program-1: Basic Constructor Example
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")

p1 = Person("John")
p1.display_name()


#Program-2: Constructor with Multiple Parameters
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

s1 = Student("Alice", 20)
s1.display_info()


#Program-3: Default Constructor Values
class Employee:
    def __init__(self, name="Unknown", salary=30000):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

e1 = Employee("Bob", 50000)
e2 = Employee()
e1.display_employee()
e2.display_employee()


#Program-4: Constructor for Calculating Area of a Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r1 = Rectangle(4, 5)
print("Area of rectangle:", r1.area())


#Program-5: Constructor for Bank Account Details
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: ${self.balance}")

account = BankAccount("Sarah", 1500)
account.display_balance()


#Program-6: Constructor for Student Grades
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return f"Student {self.name} has a grade of {self.grade}"

s1 = Student("David", "A")
print(s1.get_grade())


#Program-7: Constructor with Nested Classes
class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, model, engine_power):
        self.model = model
        self.engine = Engine(engine_power)

    def car_info(self):
        print(f"Car Model: {self.model}, Engine Power: {self.engine.power} HP")

car1 = Car("Toyota", 150)
car1.car_info()


#Program-8: Constructor with Input Validation
class Product:
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self.price = price
        else:
            self.price = 0

    def display_product(self):
        print(f"Product Name: {self.name}, Price: ${self.price}")

p1 = Product("Laptop", 800)
p2 = Product("Tablet", -150)
p1.display_product()
p2.display_product()


#Program-9: Constructor for a Circle with Default Radius
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c1 = Circle(3)
c2 = Circle()
print("Area of Circle 1:", c1.area())
print("Area of Circle 2:", c2.area())

#Program-10: Constructor to Store and Display a List of Subjects
class SubjectList:
    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def display_subjects(self):
        print("Subjects:", ", ".join(self.subjects))

s = SubjectList("Math", "Science", "History")
s.display_subjects()