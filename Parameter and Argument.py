#Program-1: Simple Function with Positional Arguments
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


#Program-2: Function with Multiple Positional Arguments
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)


#Program-3: Function with Default Arguments
def greet(name, message="Good morning"):
    print(f"{message}, {name}!")

greet("Alice")
greet("Bob", "Good evening")


#Program-4: Function with Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(name="Alice", age=25)
introduce(age=30, name="Bob")


#Program-5: Function with *args (Variable-Length Arguments)
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # Output: 10
print(add_all(10, 20))      # Output: 30


#Program-6: Function with **kwargs (Keyword Variable-Length Arguments)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, job="Developer")


#Program-7: Combining Positional, *args, and **kwargs
def order_food(dish, *sides, **extras):
    print(f"Main dish: {dish}")
    print("Sides:")
    for side in sides:
        print(f"- {side}")
    print("Extras:")
    for key, value in extras.items():
        print(f"{key}: {value}")

order_food("Burger", "Fries", "Salad", drink="Coke", sauce="Ketchup")


#Program-8: Function Returning Multiple Values
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    product = a * b
    return sum_, diff, product

result = calculate(10, 5)
print(result)


#Program-9: Passing a List as an Argument
def find_max(numbers):
    return max(numbers)

numbers = [2, 8, 3, 5, 7]
print(find_max(numbers))


#Program-10: Recursive Function with Parameter
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))