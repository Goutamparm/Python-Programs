#Program-1: Lambda Function to Add Two Numbers
add = lambda a, b: a + b
print("Sum:", add(5, 3))

#Program-2: Lambda Function to Find Maximum of Two Numbers
maximum = lambda a, b: a if a > b else b
print("Maximum:", maximum(10, 20))

#Program-3: Lambda Function to Square a Number
square = lambda x: x * x
print("Square of 4:", square(4))

#Program-4: Lambda Function to Check if a Number is Even
is_even = lambda x: x % 2 == 0
print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))

#Program-5: Lambda Function to Find the Length of a String
length = lambda s: len(s)
print("Length of 'Python':", length('Python'))

#Program-6: Lambda Function for Multiplication of Two Numbers
multiply = lambda a, b: a * b
print("Multiplication of 6 and 7:", multiply(6, 7))

#Program-7: Lambda Function to Filter Even Numbers from a List
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#Program-8: Lambda Function to Double Each Number in a List
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled)

#Program-9: Lambda Function to Sort a List of Tuples by the Second Value
pairs = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted by second value:", sorted_pairs)

#Program-10: Lambda Function to Find the Factorial of a Number Using reduce()
from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n+1))
print("Factorial of 5:", factorial(5))