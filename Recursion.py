#Program-1: Factorial of a Number Using Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")


#Program-2: Fibonacci Sequence Using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = 10
for i in range(n_terms):
    print(fibonacci(i), end=" ")


#Program-3: Sum of First N Natural Numbers Using Recursion
def sum_of_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_n(n - 1)

n = 10
print(f"Sum of first {n} natural numbers is {sum_of_n(n)}")

#Program-4: Power of a Number Using Recursion
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

base = 2
exp = 3
print(f"{base}^{exp} = {power(base, exp)}")

#Program-5: Find the Greatest Common Divisor (GCD) Using Recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = 56, 98
print(f"GCD of {a} and {b} is {gcd(a, b)}")


#Program-6: Check if a String is Palindrome Using Recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

string = "madam"
print(f"Is '{string}' a palindrome? {is_palindrome(string)}")


#Program-7: Find the Sum of Digits of a Number Using Recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

num = 1234
print(f"Sum of digits of {num} is {sum_of_digits(num)}")


#Program-8: Binary Search Using Recursion
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 7
result = binary_search(arr, 0, len(arr) - 1, x)
print(f"Element {x} is at index {result}")

#Program-9. Reverse a String Using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

string = "hello"
print(f"Reversed string: {reverse_string(string)}")

#Program-10: Tower of Hanoi Problem Using Recursion
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')