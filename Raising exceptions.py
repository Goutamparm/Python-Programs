#Program-1: Raise a ValueError for Invalid Input
def check_positive(num):
    if num < 0:
        raise ValueError("Number must be positive.")
    return num

print(check_positive(5))
print(check_positive(-3))

#Program-2: Raise a ZeroDivisionError Manually
def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))

#Program-3: Raise a TypeError for Incorrect Data Type
def check_string(value):
    if not isinstance(value, str):
        raise TypeError("Expected a string value.")
    return value.upper()

print(check_string("hello"))
print(check_string(123))

#Program-4: Raise a KeyError for Missing Dictionary Key
def get_value(dictionary, key):
    if key not in dictionary:
        raise KeyError(f"Key '{key}' not found in dictionary.")
    return dictionary[key]

data = {"name": "Alice", "age": 25}
print(get_value(data, "name"))
print(get_value(data, "height"))

#Program-5: Raise a FileNotFoundError for Missing File
def read_file(file_name):
    if not file_name.endswith('.txt'):
        raise FileNotFoundError("Only .txt files are supported.")
    print("File opened successfully!")

read_file("example.txt")
read_file("example.pdf")

#Program-6: Raise a NotImplementedError for Abstract Methods
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Circle(Shape):
    pass

c = Circle()
c.area()

#Program-7: Raise an IndexError for Out-of-Range Index
def get_element(lst, index):
    if index >= len(lst):
        raise IndexError("Index out of range.")
    return lst[index]

my_list = [1, 2, 3]
print(get_element(my_list, 1))
print(get_element(my_list, 5))

#Program-8: Raise a RuntimeError for Invalid State
def process_data(data):
    if not data:
        raise RuntimeError("No data to process.")
    print("Processing data...")

process_data([1, 2, 3])
process_data([])

#Program-9: Raise an AttributeError for Missing Attribute
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
if not hasattr(p, "age"):
    raise AttributeError("Person object has no attribute 'age'.")

#Program-10: Raise a CustomException (User-Defined Exception)
class CustomException(Exception):
    pass

def check_value(value):
    if value < 0:
        raise CustomException("Value cannot be negative.")

check_value(10)
check_value(-5)