# Program-1: Print Numbers from 1 to 10

# Using For Loop
for i in range(1,11):
    print(i)
# Using While Loop
i=1
while i<=10:
    print(i)
    i+=1

# Program-2: Print the Multiplication Table of a Given Number

# Using For Loop
a = int(input('Enter the Number:'))
for i in range(1,11):
    print(f"{a} x {i} = {a*i}")
# Using While Loop
a = int(input('Enter the Number:'))
i=0
while i<=10:
    print(f"{a} x {i} = {a*i}")
    i+=1

# Program-3: Calculate the Sum of First n Natural Numbers

# Using For Loop
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of first", n, "natural numbers is:", total)
# Using While  Loop
n = int(input("Enter a number: "))
total, i = 0, 1
while i <= n:
    total += i
    i += 1
print("Sum of first", n, "natural numbers is:", total)


# Program-4: Count the Number of Digits in a Given Number

# Using For Loop
num = input("Enter a number: ")
count = 0
for digit in num:
    count += 1
print("Number of digits:", count)
# Using While Loop
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits:", count)

# Program-5: Find Factorial of a Given Number

# Using For Loop
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)
# Using While Loop
num = int(input("Enter a number: "))
factorial, i = 1, 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial of", num, "is:", factorial)

# Program-6: Print Even Numbers within a Given Range

# Using For Loop
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")
# Using While Loop
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
while start <= end:
    if start % 2 == 0:
        print(start, end=" ")
    start += 1


# Program-7: Reverse a Given String

# Using For Loop
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string is:", reversed_string)
# Using While Loop
string = input("Enter a string: ")
reversed_string = ""
i = len(string) - 1
while i >= 0:
    reversed_string += string[i]
    i -= 1
print("Reversed string is:", reversed_string)

# Program-8: Find the Sum of Digits of a Given Number

# Using For Loop
num = input("Enter a number: ")
total = 0
for digit in num:
    total += int(digit)
print("Sum of digits is:", total)
# Using While Loop
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num = num // 10
print("Sum of digits is:", total)

# Program-9: Check if a Number is Prime

# Using For Loop
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
# Using While Loop
num = int(input("Enter a number: "))
i = 2
is_prime = True
if num > 1:
    while i <= int(num ** 0.5):
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
else:
    print(num, "is not a prime number.")

# Program-10: Print Fibonacci Sequence up to n Terms

#Using for loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Sequence:", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
# Using While Loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
print("Fibonacci Sequence:", end=" ")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
