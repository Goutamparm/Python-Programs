# # def is_adjacent(matrix, node1, node2):
# #     return matrix[node1][node2]==1
# #
# # matrix1 = [
# #     [0, 1, 0, 0],
# #     [1, 0, 1, 1],
# #     [0, 1, 0, 1],
# #     [0, 1, 1, 0]
# # ]
# # print(is_adjacent(matrix1, 0, 1))
# # print(is_adjacent(matrix1, 0, 2))
#
# def dac(value):
#     refrenece_voltage= 5.00
#     max_voltage_value=1023
#     analog_voltage= (value/max_voltage_value)*refrenece_voltage
#     return analog_voltage
# print(dac(3))

# int,str = str,int
# def int_ti_str(n):
#     return str(n)
# def str_to_int(s):
#     return int(s)
#
# a=6
# b="6"
# print(int_ti_str(a))
# print(str_to_int(b))

# def shift_to_right(x,y):
#     x=4666
#     y=6
#     z=x/(2**y)
#     return z
# a=-512
# b=10
# print(shift_to_right(a,b))

# def find_largest(n):
#     if len(n)==1:
#         return n[0]
#     r=find_largest(n[1:])
#     return r if r>=n[0] else n[0]
#
# a = [-1, 3, 5, 6, 99, 12, 2]
# print(find_largest(a))

# def len_gth(num):
#     return num
# a="hello"
# print(len_gth(len(a)))

# def number_length(num):
#     length=0
#     for i in str(num):
#         length += 1
#     return length
# a="hello"
# print(number_length(a))

# def number_length(n):
#     s=0
#     if n%3==0:
#         return "Fizz"
#     elif n%5==0:
#         return "Buzz"
#     elif n%3==0 and n%5==0:
#         return "FizzBuzz"
#     else:
#         return str(n)
# a=3
# print(number_length(a))

# import math
# def len_length1(point1,point2):
#     x1,y1=point1
#     x2,y2=point2
#     length=math.sqrt((x2-x1)**2 + (y2-y1)**2)
#     return round(length,2)
#
# print(len_length1([2,5],[2,6]))

# def sum_odd_even(n):
#     odd,even=0,0
#     for i in n:
#         if i%2:
#             odd+=i
#         else :
#             even +=i
#     return (odd,even)
# a=[1,6,8,9,74,6,67,236]
# print(sum_odd_even(a))

# def total_over(ball):
#     over = ball//6
#     remaining_ball= ball%2
#     return float(f"{over}.{remaining_ball}")
# print(total_over(50))

# def total_pet(items,name):
#     if name in items:
#         return name.capitalize() +" is gone...."
#
#     return name.capitalize() + " is here..."
#
# item={"loverly": 40, "sweaty": 60, "prt" : 70 }
# print(total_pet(item,"loverly"))

# def top_notes(student):
#     return {"name":student["name"],"top_note":max(student["notes"])}
#
# print(top_notes({"name":"john","notes":[2,6,7]}))

# def profit(data):
#     total_cost=data["cost_price"]*data["inventory"]
#     total_sell=data["sell_price"]*data["inventory"]
#     total_profit= total_sell-total_cost
#     return total_profit
#
# print(profit({"cost_price":26,"sell_price":78, "inventory":150}))

# def world_landmass(name,area):
#        name="name"
#        area= "area"
#
#        return
#
# name="Usa"
# area= 197850/14894000
# print(world_landmass(name, area))

# def interview(times,total_time):
#        limit=[5,5,10,10,15,15,20,20]
#        if len(times)!=len(limit) or total_time>120:
#               return "disqualified"
#
#        for i,time in enumerate(times):
#               if time>limit[i]:
#                      return "disqualified"
#
#        return "qualified"
# print(interview([5,5,10,10,15,15,20,20],120))
#
#
#
# # Test cases
# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))  # ➞ "qualified"
# print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))  # ➞ "qualified"
# print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))  # ➞ "disqualified"
# print(interview([5, 5, 10, 10, 15, 15, 20], 120))  # ➞ "disqualified"
# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))  # ➞ "disqualified"

import socket
# def get_domain(ip_address):
#        try:
#               return socket.gethostbyaddr(ip_address)[0]
#        except socket.herror:
#               return "domain not found"
#
# print(get_domain("8.8.8.8"))



# def arithmetic_operator(expression: str):
#     num1,op,num2=expression.split()
#     num1,num2=int(num1),int(num2)
#
#     if op=="+":
#        return num1+num2
#     elif op=="-":
#        return num1-num2
#     elif op=="*":
#        return num1*num2
#     elif op=="//":
#        return num1//num2 if num2!=0 else -1
#
# print(arithmetic_operator("12+12"))

#
# def arithmetic_operation(expression: str):
#        num1,op,num2 = expression.split()
#        num1, num2 = int(num1), int(num2)
#
#        if op == '+':
#               return num1 + num2
#        elif op == '-':
#               return num1 - num2
#        elif op == '*':
#               return num1 * num2
#        elif op == '//':
#               return num1 // num2 if num2 != 0 else -1
#
#
# # Test Cases
# print(arithmetic_operation("12 + 12"))  # 24
# print(arithmetic_operation("12 - 12"))  # 0
# print(arithmetic_operation("12 * 12"))  # 144
# print(arithmetic_operation("12 // 0"))  # -1

# def dec_desarium(n):
#     digitals = list(map(int,str(n)))
#     return sum(d**(i+1)for i,d in enumerate(digitals))==n
#
# print(dec_desarium(135))

# def pentagonal(n):
#     count=1
#     for i in range(1,n):
#         count+=5*i
#     return count
# print(pentagonal(8))

# def encryption(n):
#     translate_table=str.maketrans("aeiu","0123")
#     return n[::-1].translate(translate_table)+"aca"
#
# print(encryption("banana"))

# import datetime
# def has_friday_13(month,year):
#     return datetime.date(year,month,13).weekday()==4
#
# print(has_friday_13(4,2078))

# def consecutive_comb(lst1,lst2):
#     combined=sorted(lst1+lst2)
#     for i in range(len(combined)-1):
#         if combined[i]+1 != combined[i+1]:
#             return False
#     return True
#
# print(consecutive_comb([2,6,7,9,4,6],[1,5,49,7,691]))

# def tellast_skyscrper(grid):
#     rows,cols = len(grid),len(grid[0])
#     max_height =0
#     for j in range(cols):
#         for i in range(rows):
#             if grid[i][j]==1:
#                 max_height=max(max_height,rows-i)
#                 break
#     return max_height

# def convert_hex(s):
#     return ''.join(hex(ord(c))[2:] for c in s)
#
# print(convert_hex("hello world"))

# def unconser(text,vowel):
#     vowel_iter=iter(vowel)
#     return ' '.join(next(vowel_iter) if char == "*" else char  for char in text)
#
# print(unconser("abcd",""))

# def bonus(days):
#     if days<=32:
#         return 0
#     elif days<=40:
#         return (days-32)*325
#     elif days<=48:
#         return (8*325)+(days-40)*550
#     else:
#         return (8*325)+(8*550)+(days-48)*600
#
# print(bonus(45))

# def altburn(text):
#     def tranform(c):
#         if 'A' <= c <= 'Z':
#             return chr(155-ord(c))
#         elif 'a' <= c <= 'z':
#             return chr(219-ord(c))
#         return c
#     return " ".join(tranform(c) for c in text)
# print(altburn("hello"))

def can_see_stage(matrix):
    rows,cols = len(matrix),len(matrix[0])
    for j in range(cols):
        for i in range(rows - 1):
            if matrix[i][j] >= matrix[i+1][j]:
                return False
    return True

print(can_see_stage([[1,2,3],[4,5,6],[7,8,9]]))


