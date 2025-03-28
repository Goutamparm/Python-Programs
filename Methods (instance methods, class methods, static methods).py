#Program-1: Basic Example of Instance Method
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

p = Person("Alice")
print(p.greet())


#Program-2: Class Method Example
class Company:
    company_name = "TechCorp"

    @classmethod
    def get_company_name(cls):
        return cls.company_name

print(Company.get_company_name())


#Program-3: Static Method Example
class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

print(MathOperations.add_numbers(5, 3))


#Program-4: Using All Three Methods Together
class Student:
    school_name = "Springfield High"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_details(self):
        return f"Student: {self.name}, Grade: {self.grade}"

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod
    def is_adult(age):
        return age >= 18

student = Student("John", "A")
print(student.get_details())

print(Student.get_school_name())

print(Student.is_adult(16))


#Program-5: Counting Instances with Class Method
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def total_instances(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
print("Total instances:", Counter.total_instances())


#Program-6: Modifying Class Variables with Class Method
class Animal:
    kingdom = "Animalia"

    @classmethod
    def set_kingdom(cls, new_kingdom):
        cls.kingdom = new_kingdom

    def get_kingdom(self):
        return self.kingdom

a1 = Animal()
print(a1.get_kingdom())

Animal.set_kingdom("Mammalia")
print(a1.get_kingdom())


#Program-7: Checking Leap Year using Static Method
class Year:
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(Year.is_leap_year(2024))
print(Year.is_leap_year(2023))


#Program-8: Example with Data Validation in Static Method
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def is_valid_temp(temp):
        return -273.15 <= temp <= 1000

    def set_temperature(self, temp):
        if Temperature.is_valid_temp(temp):
            self.celsius = temp
        else:
            print("Invalid temperature.")

temp = Temperature(25)
temp.set_temperature(-500)


#Program-9: Combining Instance, Class, and Static Methods in a Banking System
class BankAccount:
    interest_rate = 0.03

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print("Balance:", acc.balance)

BankAccount.set_interest_rate(0.05)
print("New interest rate:", BankAccount.interest_rate)

print("Is amount valid?", BankAccount.is_valid_amount(-100))


#Program-10: Class and Static Methods in Employee Management
class Employee:
    minimum_salary = 30000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_minimum_salary(cls, new_salary):
        cls.minimum_salary = new_salary

    @staticmethod
    def is_eligible_for_loan(salary):
        return salary >= Employee.minimum_salary

Employee.set_minimum_salary(35000)

print(Employee.is_eligible_for_loan(40000))
print(Employee.is_eligible_for_loan(25000))