# # #Program-1. Custom Exception for Division by a Negative Number
# # class NegativeDivisionError(Exception):
# #     pass
# #
# # def divide(a, b):
# #     if b < 0:
# #         raise NegativeDivisionError("Cannot divide by a negative number!")
# #     return a / b
# #
# # try:
# #     print(divide(10, -2))
# # except NegativeDivisionError as e:
# #     print("Error:", e)
# #
# #
# # #Program-2. Custom Exception for Invalid Age
# # class InvalidAgeError(Exception):
# #     pass
# #
# # def validate_age(age):
# #     if age < 0:
# #         raise InvalidAgeError("Age cannot be negative.")
# #     print("Valid age:", age)
# #
# # try:
# #     validate_age(-5)
# # except InvalidAgeError as e:
# #     print("Error:", e)
# #
# #
# # #Program-3. Custom Exception for Non-Alphabetic Names
# # class InvalidNameError(Exception):
# #     pass
# #
# # def check_name(name):
# #     if not name.isalpha():
# #         raise InvalidNameError("Name must contain only alphabets.")
# #     print("Valid name:", name)
# #
# # try:
# #     check_name("John123")
# # except InvalidNameError as e:
# #     print("Error:", e)
# #
# #
# # #Program-4. Custom Exception for Insufficient Balance
# # class InsufficientBalanceError(Exception):
# #     pass
# #
# # def withdraw(balance, amount):
# #     if amount > balance:
# #         raise InsufficientBalanceError("Insufficient balance for this transaction.")
# #     return balance - amount
# #
# # try:
# #     print("Remaining balance:", withdraw(500, 1000))
# # except InsufficientBalanceError as e:
# #     print("Error:", e)
# #
# #
# # #Program-5. Custom Exception for Invalid Email
# # class InvalidEmailError(Exception):
# #     pass
# #
# # def validate_email(email):
# #     if "@" not in email or "." not in email:
# #         raise InvalidEmailError("Invalid email address.")
# #     print("Valid email:", email)
# #
# # try:
# #     validate_email("invalid_email.com")
# # except InvalidEmailError as e:
# #     print("Error:", e)
# #
# #
# # #Program-6. Custom Exception for Out-of-Range Numbers
# # class OutOfRangeError(Exception):
# #     pass
# #
# # def check_number(num):
# #     if num < 1 or num > 100:
# #         raise OutOfRangeError("Number is out of the valid range (1-100).")
# #     print("Valid number:", num)
# #
# # try:
# #     check_number(150)
# # except OutOfRangeError as e:
# #     print("Error:", e)
# #
# #
# # #Program-7. Custom Exception for Invalid File Format
# # class InvalidFileFormatError(Exception):
# #     pass
# #
# # def check_file_format(file_name):
# #     if not file_name.endswith(".txt"):
# #         raise InvalidFileFormatError("Only .txt files are allowed.")
# #     print("Valid file:", file_name)
# #
# # try:
# #     check_file_format("document.pdf")
# # except InvalidFileFormatError as e:
# #     print("Error:", e)
# #
# #
# # #Program-8. Custom Exception for Unauthorized Access
# # class UnauthorizedAccessError(Exception):
# #     pass
# #
# # def access_resource(user_role):
# #     if user_role != "admin":
# #         raise UnauthorizedAccessError("Only admins can access this resource.")
# #     print("Access granted.")
# #
# # try:
# #     access_resource("guest")
# # except UnauthorizedAccessError as e:
# #     print("Error:", e)
# #
# #
# # #Program-9. Custom Exception for Negative Numbers in a List
# # class NegativeNumberError(Exception):
# #     pass
# #
# # def check_list(numbers):
# #     for num in numbers:
# #         if num < 0:
# #             raise NegativeNumberError("Negative numbers are not allowed in the list.")
# #     print("All numbers are valid.")
# #
# # try:
# #    check_list([1, 2, -3, 4])
# # except NegativeNumberError as e:
# #     print("Error:", e)
# #
# #
# # #Program-10. Custom Exception for Invalid Password
# # class InvalidPasswordError(Exception):
# #     pass
# #
# # def validate_password(password):
# #     if len(password) < 8:
# #         raise InvalidPasswordError("Password must be at least 8 characters long.")
# #     print("Valid password.")
# #
# # try:
# #     validate_password("pass")
# # except InvalidPasswordError as e:
# #     print("Error:", e)
#
#
# # list =[1,2,3,4,5]
# # print(list.append(8))
# # a= "akash"
# # print(a[1])
# # dict={ "name": "akash"}
# # for key in dict.items():
# #     print(key)
#
# # def num(a,b):
# #     return a+b
# # numb=num(2,3)
# # print(numb)
#
# # score=45
# # if score>=90:
# #   print('A grade')
# # elif score>=80 and score<=89:
# #   print('B Grade')
# # elif score>=70 and score<=79:
# #   print('C grade')
# # elif score>=60 and score<=69:
# #   print('D grade')
# # else:
# #  print('F Grade')
# #
# # fruits="red"
# # if fruits == "yellow":
# #    print("ripe")
# # elif fruits == "green":
# #    print("unripe")
# # elif fruits =="brown":
# #   print("overripe")
# # else:
# #   print("not found color to match")
# # distance=3
# # mode="bike"
# # if distance<=3:
# #    mode="walk"
# #    print(mode)
# # elif distance>3 and distance<=15:
# #    mode="bike"
# #    print(mode)
# # elif distance>15:
# #      mode="car"
# #      print(mode)
# # else:
# #     print("wrong value")
# #
# # order = "small"
# # extra = "NA" if order in ["small","medium","large"] else "na"
# #
# # # print(order,"with", extra)
# # passw="rahittadav"
# # length=len(passw)
# # if length<=6:
# #    print("weak")
# # elif length>=6 and length<=10:
# #    print("medium")
# # else:
# #    print("strong")
#
# # num = [1,-2,3,-4,5,6,-7,-8,9,10]
# # positive_number_count=0
# # for i in num:
# #     if i>0:
# #       positive_number_count+=1
# # print(positive_number_count)
#
# # num =10
# # sum_even=0
# # for i in range(1,num+1):
# #   if i%2==0:
# #    sum_even+=1
# # print(sum_even)
#
# # def num(a,b):
# #     num1=a+b
# #
# #     print(num1)
# # num(2,5)
#
# # class Person:
# #     name="name"
# #     age="age"
# #     address="Address"
# #     # def info(self):
# #     #     print(f"myname is{self.name}, my age is {self.age}, my address is {self.address}")
# #
# # a=Person()
# # a.name="akash"
# # a.age=25
# # a.address="1453 colo baag"
# # # a.info()
# # print(a.name, a.age, a.address)
#
# # class Person:
# #     def __init__(self,name,age):
# #       self.name= name
# #       self.age= age
# #     def info(self):
# #           print(f"my name is{self.name} & age {self.age}")
# #
# # a=Person("Akash",25)
# # b=Person("rahul",47)
# #
# # a.info()
# # b.info()
#
# # def decorator(func):
# #     def wrapper():
# #       print("befor the call")
# #       func()
# #       print("afer the call")
# #     return wrapper()
# #
# # @decorator
# # def Hello():
# #    print("hello")
# #
# # Hello
#
# # def is_prime(n):
# #   if n<2:
# #     return False
# #   for i in range(2,int(n**0.5+1)):
# #       if n%i==0:
# #        return False
# #   return True
# #
# # num=17
# # print(f"{num} is prime:{is_prime(num)}")
# #
# # def is_prime(n):
# #     if n < 2:
# #         return False
# #     for i in range(2, int(n ** 0.5) + 1):
# #         if n % i == 0:
# #             return False
# #     return True
# #
# # # Example usage
# # num = 24
# # print(f"{num} is prime: {is_prime(num)}")
#
# # # reversed string
# # def reves_string(s):
# #     revesed_str=" "
# #     for char in s:
# #         revesed_str= char + revesed_str
# #     return revesed_str
# # str ="hello"
# # print(f"reversed: {reves_string(str)}")
#
# # def reverse_string(s):
# #     reversed_str = ""
# #     for char in s:
# #         reversed_str = char + reversed_str  # Prepend each character
# #     return reversed_str
# #
# # # Example usage
# # text = "Hello"
# # print(f"Reversed: {reverse_string(text)}")
#
# # arra sum is 12
# # def find_Pairs(arr,target):
# #     pairs=[]
# #     for i in range(len(arr)):
# #         for j in range(i+1, len(arr)):
# #             if arr[i] + arr[j] == target:
# #                 pairs.append((arr[i],arr[j]))
# #     return pairs
# # arr =[3,4,6,7,8,0,6,5,6,7]
# # target = 12
# # print(find_Pairs(arr,target))
#
# # hallow star patten in tringle
# # def hallow_triangle(n):
# #     for i in range(n):
# #         for j in range(i+1):
# #             if j==0 or j==i or i==n-1:
# #                 print("*",end="")
# #             else:
# #                 print(" ",end="")
# #         print()
# #
# # hallow_triangle(5)
#
# # # Pyramid pattern
# # def Pyramid_pattern(n):
# #     for i in range(1,n+1):
# #         print(" "*(n-i)+"*"*(2*i-1))
# #
# # Pyramid_pattern(5)
#
# # # inerted Pyramid
# # def inverted_Pattern(n):
# #     for i in range(n,0,-1):
# #         print(" "*(n-i)+"*"*(2*i-1))
# # inverted_Pattern(5)
#
# # second largest number
# # def second_largest(arr):
# #     unique_number= list(set(arr))
# #     if len(unique_number) < 2:
# #         return "this is no second largest number"
# #     unique_number.sort(reverse=True)
# #     return unique_number[1]
# # number=[1,64,89,49,75,36,14,92,]
# # print("Second Largest:" ,second_largest(number))
#
# #frquency of character
# def frequency_chart(s):
#     frequency = {}
#     for char in s:
#         frequency[char] = frequency.get(char,0)+1
#     return frequency
# text="hello"
# print(frequency_chart(text))

# Empoyee salary
# class Employee:
#     def __init__(self,name,salary):
#         self.name =name
#         self.salary =salary
#
#     def details(self):
#         print(f"Employee Name {self.name}")
#         print(f"Employee Name {self.salary}")
#
# emp1 = Employee("goutam",54000)
# emp1.details()

# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#     def make_sound(self):
#         return "some generic sound"
#
# class Dog(Animal):
#     def make_sound(self):
#         return "bark-bark"
#
# name=Dog("Tommy")
# print(f"dog name:,{name.name}")
# print(f"make sound,{name.make_sound()}")

#bank account

# class Account:
#     def __init__(self,holder_name,balance=0.0):
#         self.balance= balance
#         self.holder_name= holder_name
#
#     def deposit(self, amount):
#         if amount>0:
#             self.balance += amount
#             print(f"{amount} deposited successfully,New Balance:{self.balance} ")
#         else:
#             print("Your balance is greater than zero ")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance-=amount
#             print(f"{amount} withdraw successfully . New balance {self.balance}")
#
#     def get_balace(self):
#         return f"{self.balance}"
#
# account=Account("Goutam",50000)
# print(account.get_balace())
#
# account.deposit(17500)
# account.withdraw(150)
# account.withdraw(1500)
# print(account.get_balace())

# # inheritance
# class Animal:
#     def sound(self):
#         print(f" genratic sound")
#
# class Dog(Animal):
#      def make_sound(self):
#          print("bark-Bark")
#
# name = Dog()
# name.make_sound()

# # polymorphism
# class Cat:
#     def sound(self):
#         print("meaw")
# class Dog:
#     def sound(self):
#         print("berk-berk")
#
# def make_sound(animal):
#     animal.sound()
#
# dog=Dog()
# cat=Cat()
# make_sound(dog)
# make_sound(cat)

# Abstract

# from abc import ABC,abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#           def sound(self):
#               return "bark-bark"
#
# class Cat(Animal):
#     def sound(self):
#         return "meaw"
#
# dog=Dog()
# cat=Cat()
#
# print(dog.sound())
# print(cat.sound())

# num = 17
# is_prime = True
# if num<1:
#     is_prime=False
# else:
#     for i in range(2,num):
#         if num%2==0:
#             is_prime=False
#             break
#
# print(is_prime)

# num =15
# is_prime=True
# if num<1:
#    is_prime=False
# else:
#     for i in range(2,num):
#         if num%2==0:
#             is_prime=False
#
#     print(is_prime)

# def decorator(s):
#     def deco():
#       print("before call")
#       s()
#       print("after call")
#     return deco()
#
# @decorator
# def hello():
#     print("hello")
#
# hello

# def reverse_string(s):
#     revesed=""
#     for char in s:
#      revesed =char+revesed
#     return revesed
#
# text="hello"
# print(f"{reverse_string(text)}")

# def find_pairs(arr,target):
#     pairs=[]
#     for i in range(len(arr)):
#         for j in range (i+1,len(arr)):
#             if arr[i] + arr[j] == target:
#                 pairs.append(arr[i],arr[j])
#     return pairs
#
# arr = [6]

# def hollow_pattern(n):
#      for i in range(n):
#           for j in range(i+1):
#                if j==0 or i==n-1 or j==i:
#                     print("*",end="")
#                else:
#                     print(" ",end="")
#           print()
#
# hollow_pattern(5)

# def pyramid(n):
#      for i in range(n,0,-1):
#           print(" "*(n-i) + "*"*(2*i-1))
#      print()
#
# pyramid(5)

# def lar_gest(arr):
#     unqu_num = list(set(arr))
#     if len(unqu_num) < 2:
#         return "there string no more then two"
#         # noinspection PyUnreachableCode
#     unqu_num.sort(reverse=True)
#     return unqu_num[1]
#
#
# num = [2,67,97,36,894,5489,489,599]
# print(lar_gest(num))
