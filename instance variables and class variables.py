#Program-1: Basic Program Demonstrating Instance and Class Variables
class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

emp1 = Employee("Alice")
emp2 = Employee("Bob")

print(emp1.company)
print(emp2.company)
print(emp1.name)
print(emp2.name)


#Program-2: Modifying Class Variable and Instance Variable Separately
class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

emp1 = Employee("Alice")
emp2 = Employee("Bob")

Employee.company = "CodeCorp"
print(emp1.company)

emp1.name = "Charlie"
print(emp1.name)


#Program-3: Using Class Variables as Counters
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print("Total objects created:", Counter.count)


#Program-4: Different Instance Variables for Each Object
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

car1 = Car("Toyota", 2010)
car2 = Car("Honda", 2015)

print(car1.model, car1.year)
print(car2.model, car2.year)


#Program-5: Accessing Class Variables through Instances
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

circle1 = Circle(5)
print("Value of pi through instance:", circle1.pi)


#Program-6: Calculating Total Salary with Class and Instance Variables
class Employee:
    base_salary = 30000

    def __init__(self, bonus):
        self.bonus = bonus

    def total_salary(self):
        return Employee.base_salary + self.bonus

emp1 = Employee(5000)
print("Total salary:", emp1.total_salary())


#Program-7: Tracking Number of Students in a Class
class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1

s1 = Student("John")
s2 = Student("Emily")
s3 = Student("Sam")

print("Number of students:", Student.student_count)


#Program-8: Shared Class Variable among Instances
class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name

dog1 = Dog("Max")
dog2 = Dog("Bella")

print(dog1.species, dog1.name)
print(dog2.species, dog2.name)


#Program-9: Changing Class Variables through Class
class Animal:
    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name

print(Animal.kingdom)
animal1 = Animal("Lion")
print(animal1.kingdom)

Animal.kingdom = "Mammalia"
print(animal1.kingdom)

#Program-10: Using Class and Instance Variables in Methods
class Rectangle:
    default_color = "Blue"

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def change_color(self, new_color):
        Rectangle.default_color = new_color

rect = Rectangle(4, 5)
print("Area:", rect.area())

rect.change_color("Green")
print("Rectangle color:", Rectangle.default_color)