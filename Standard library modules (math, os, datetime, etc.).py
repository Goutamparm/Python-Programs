#Program-1: Using the math Module for Mathematical Operations
import math

number = 25
print("Square root:", math.sqrt(number))

num1, num2 = 56, 98
print("GCD:", math.gcd(num1, num2))

print("2 raised to the power of 3:", math.pow(2, 3))

#Program-2: Using the os Module for System Operations
import os

print("Current Directory:", os.getcwd())

print("Directory Contents:", os.listdir())

os.mkdir("example_dir")
print("Directory created:", os.path.exists("example_dir"))
os.rmdir("example_dir")
print("Directory removed:", not os.path.exists("example_dir"))

#Program-3: Using the datetime Module to Work with Dates and Times
from datetime import datetime, timedelta

current_time = datetime.now()
print("Current Time:", current_time)

print("Formatted Date:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

future_date = current_time + timedelta(days=5)
print("Date 5 Days from Now:", future_date)

#Program-4: Using the random Module for Random Number Generation
import random

print("Random Integer:", random.randint(1, 100))

choices = ['apple', 'banana', 'cherry']
print("Random Choice:", random.choice(choices))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled List:", numbers)

#Program-5: Using the statistics Module for Statistical Calculations
import statistics

data = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(data))

print("Median:", statistics.median(data))

print("Standard Deviation:", statistics.stdev(data))

#Program-6: Using the collections Module for Special Data Structures
from collections import Counter, namedtuple, defaultdict

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
color_count = Counter(colors)
print("Color Count:", color_count)

Point = namedtuple('Point', 'x y')
p = Point(10, 20)
print("Namedtuple Point:", p.x, p.y)

dd = defaultdict(int)
dd['a'] += 1
print("Defaultdict:", dd)

#Program-7: Using the itertools Module for Combinatorics
from itertools import permutations, combinations, product

data = [1, 2, 3]
print("Permutations:", list(permutations(data)))

print("Combinations of 2:", list(combinations(data, 2)))

list1 = [1, 2]
list2 = ['a', 'b']
print("Product:", list(product(list1, list2)))

#Program-8: Using the time Module to Measure Execution Time
import time

start_time = time.time()

sum = 0
for i in range(100000):
    sum += i

end_time = time.time()
print("Elapsed Time:", end_time - start_time, "seconds")

#Program-9: Using the re Module for Regular Expressions
import re

text = "The rain in Spain falls mainly in the plain."

matches = re.findall(r'ain', text)
print("Occurrences of 'ain':", matches)

if re.match(r'^The', text):
    print("Text starts with 'The'")

updated_text = re.sub(r'Spain', 'France', text)
print("Updated Text:", updated_text)

#Program-10: Using the json Module to Handle JSON Data
import json

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

person_json = json.dumps(person)
print("JSON String:", person_json)

person_dict = json.loads(person_json)
print("Python Dictionary:", person_dict)