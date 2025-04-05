####################### Create Password ########################

import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '|']

num_letter = int(input("How many letter in password:"))
num_number = int(input("How many Number in password:"))
num_symbol = int(input("How many symbol in password:"))

# easy Level

password=""
for char in range(0,num_letter):
    password += random.choice(letter)
for char in range(0, num_number):
    password += random.choice(number)
for char in range(0, num_symbol):
    password += random.choice(symbol)

print(password)

# hard Level
password =[]
for char in range(0, num_letter):
    password.append(random.choice(letter))
for char in range(0, num_number):
    password.append(random.choice(number))
for char in range(0, num_symbol):
    password.append(random.choice(symbol))

print(password)
random.shuffle(password)
print(password)

password=""
for char in password:
    password+=char
print(password)
