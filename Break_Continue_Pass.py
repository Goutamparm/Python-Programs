#Program-1: Break in a For Loop (Find First Even Number)
numbers = [1, 3, 7, 8, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
#Program-2: Break in a While Loop (Stop at 5)
i = 1
while i <= 10:
    if i == 5:
        print("Stopped at:", i)
        break
    print(i)
    i += 1

#Program-3: Continue in a For Loop (Skip Even Numbers)
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#Program-4: Continue in a While Loop (Skip Multiples of 3)
i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

#Program-5: Pass in a For Loop (Placeholder for Future Code)
for i in range(5):
    pass  # Placeholder for future logic

#Program-6: Break in Nested Loops (Exit Inner Loop on Condition)
for i in range(1, 6):
    for j in range(1, 6):
        if j == 3:
            break
        print(f"i = {i}, j = {j}")

#Program-7: Continue in Nested Loops (Skip Certain Values)
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            continue
        print(f"i = {i}, j = {j}")

#Program-8: Pass in a Function with For Loop (Empty Function)
def my_function():
    for i in range(5):
        pass  # Function logic to be implemented later
my_function()

#Program-9: Break in a While Loop (End After 3 Attempts)
attempts = 0
while True:
    attempts += 1
    if attempts > 3:
        print("Exceeded number of attempts")
        break
    print(f"Attempt {attempts}")

#Program-10: Continue in a For Loop (Skip Negative Numbers)
numbers = [-5, 3, -1, 9, -2, 6]
for num in numbers:
    if num < 0:
        continue
    print(f"Positive number: {num}")