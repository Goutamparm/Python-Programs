#Program-1: Basic Module Import
import math
print(math.sqrt(16))

#Program-2: Importing Specific Functions from a Module
from math import sqrt, pi

print(sqrt(25))
print(pi)

#Program-3: Using Aliases for Modules
import datetime as dt

print(dt.datetime.now())

#Program-4: Importing All Functions from a Module
from math import *

print(sin(pi / 2))
print(factorial(5))


#Program-5: Importing a Custom Module
def greet(name):
    return f"Hello, {name}!"

import mymodule

print(mymodule.greet("Alice"))

#Program-6:Using as to Alias a Function
from math import factorial as fact

print(fact(5))

#Program-7: Importing Multiple Modules
import math
import random

print(math.sqrt(49))
print(random.randint(1, 10))

#Program-8: Importing from the datetime Module
from datetime import date

today = date.today()
print("Today's date:", today)

#Program-9: Using the os Module for File Operations
import os

print(os.getcwd())

print(os.listdir('.'))


#Program-10: Importing a Module Only When Needed
def calculate_circle_area(radius):
    import math
    return math.pi * radius ** 2

print(calculate_circle_area(5))