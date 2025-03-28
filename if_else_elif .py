# Program-1: Print Numbers from 1 to 10
for i in range(1,11):
    print(i)

# Program-2: Check if a year is Leap Year
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, 'is a leap year.')
else:
    print(year, 'is not a leap year.')

# Program-3: Find the largest of three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

# Program-4: Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, 'is Even.')
else:
    print(num, 'is Odd.')

# Program-5: Check if a letter is a vowel or consonant
letter = input("Enter a letter: ").lower()
if letter in ('a', 'e', 'i', 'o', 'u'):
    print(letter, 'is a vowel.')
else:
    print(letter, 'is a consonant.')

# Program-6: Check eligibility to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Program-7: Check if a Triangle is valid based on angles
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")

# Program-8: Grading system based on marks
marks = float(input("Enter the marks: "))
if marks >= 90:
    print('Grade: A')
elif marks >= 80:
    print('Grade: B')
elif marks >= 70:
    print('Grade: C')
elif marks >= 60:
    print('Grade: D')
else:
    print('Grade: F')

# Program-9: Check if a character is alphabet, digit, or special character
ch = input("Enter a character: ")
if ch.isalpha():
    print(ch, 'is an alphabet.')
elif ch.isdigit():
    print(ch, 'is a digit.')
else:
    print(ch, 'is a special character.')

# Program-10: Simple Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation: +, -, *, /")
operation = input("Enter the operation: ")

if operation == '+':
    print('Result:', num1 + num2)
elif operation == '-':
    print('Result:', num1 - num2)
elif operation == '*':
    print('Result:', num1 * num2)
elif operation == '/':
    if num2 != 0:
        print('Result:', num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation.")
