#Program-1: Program to Return a Greeting Message
def greet():
    return "Hello, welcome to Python programming!"

message = greet()
print(message)


#Program-2: Program to Return the Sum of Two Numbers
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)


#Program-3: Program to Return the Factorial of a Number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))


#Program-4: Program to Return a Boolean Value for Prime Check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))
print("Is 4 prime?", is_prime(4))


#Program-5: Program to Return the Fibonacci Sequence up to n Terms
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print("Fibonacci sequence (5 terms):", fibonacci(5))


#Program-6: Program to Return the Maximum of Three Numbers
def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print("Max of 3, 7, 5:", find_max(3, 7, 5))


#Program-7: Program to Return the Sum of First n Natural Numbers (Recursive)
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

print("Sum of first 5 natural numbers:", sum_natural(5))


#Program-8: Program to Return the Count of Vowels in a String
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print("Number of vowels in 'Hello':", count_vowels("Hello"))


#Program-9: Program to Return the Sum of Variable-Length Arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of 1, 2, 3:", sum_all(1, 2, 3))
print("Sum of 5, 10, 15, 20:", sum_all(5, 10, 15, 20))


#Program-10: Program to Return a Reversed String
def reverse_string(s):
    return s[::-1]

print("Reversed string of 'Python':", reverse_string("Python"))