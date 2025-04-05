# def greet(name):
#     return f"hello,{name}! welcome to python"

# def add_number(a,b):
#     return a+b
# add_number(2,3)

# def is_even(a):
#     if a%2==0:
#         return True
#     return False
# is_even(2)

# def square(a):
#     return a**2
# square(2)

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# a=5
# print(factorial(a))

# def reverse_string(a):
#     return str(a)[::-1]
#
# b=123
# print(reverse_string(b))
#
# def count_vowel(a):
#     count=0
#     vowel="aeiou"
#     for i in a:
#         if i in vowel:
#             count+=1
#     return count
#
# a="education"
# print(count_vowel(a))

# def is_palindrome(a):
#     a=str(a)
#     return a==a[::-1]
#
# a=12
# print(is_palindrome(a))

###################################################################################################################################################################

# def find_max(a):
#     return max(a)
#
# a=[45,69,7,8,6,4,946,694,567,6974,6796,]
# print(find_max(a))

# def is_prime(a):
#     if a<2:
#         return False
#     for i in range(2,int(a**0.5)+1):
#         if a%i==0:
#             return False
#     return True
#
# a=60
# print(is_prime(a))

# def sum_of_digit(n):
#     a,b=0,1
#     for _ in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
#
# n=5
# sum_of_digit(n)
