#Program-1: Simple Function to Print a Message
def greet():
    print("Hello, welcome to Python programming!")

greet()

#Program-2: Function with Parameters (Addition of Two Numbers)
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)

#Program-3: Function with Default Parameter Value
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()  # Uses default value
greet_user("Alice")  # Passes an argument

#Program-4: Function to Find the Factorial of a Number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))

#Program-5: Function to Check if a Number is Prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))
print("Is 4 prime?", is_prime(4))

#Program-6: Function to Return Fibonacci Sequence up to n Terms
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print("Fibonacci sequence (5 terms):", fibonacci(5))

#Program-7: Function to Find Maximum of Three Numbers
def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print("Max of 3, 7, 5:", find_max(3, 7, 5))


#Program-8: Recursive Function to Find the Sum of First n Natural Numbers
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

print("Sum of first 5 natural numbers:", sum_natural(5))


#Program-9: Function to Count the Number of Vowels in a String
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print("Number of vowels in 'Hello':", count_vowels("Hello"))


#Program-10: Function with Variable-Length Arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of 1, 2, 3:", sum_all(1, 2, 3))
print("Sum of 5, 10, 15, 20:", sum_all(5, 10, 15, 20))
