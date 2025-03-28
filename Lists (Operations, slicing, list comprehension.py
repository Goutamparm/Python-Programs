#Program-10: Basic List Operations (Add, Remove, and Access Elements)
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.remove('banana')
print("Fruits list:", fruits)
print("First fruit:", fruits[0])

#Program-2: List Slicing to Access Subsets
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("First three numbers:", numbers[:3])
print("Last two numbers:", numbers[-2:])
print("Alternate numbers:", numbers[::2])

#Program-3: Concatenating Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Concatenated list:", combined_list)

#Program-4: Finding the Length of a List
fruits = ['apple', 'banana', 'cherry', 'orange']
print("Number of fruits:", len(fruits))

#Program-5: List Comprehension to Create a List of Squares
squares = [x**2 for x in range(1, 6)]
print("List of squares:", squares)

#Program-6: List Comprehension with a Condition (Even Numbers)
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

#Program-7: List of Tuples Using List Comprehension
coordinates = [(x, y) for x in range(3) for y in range(3)]
print("List of coordinates:", coordinates)

#Program-8: Reversing a List
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

#Program-9: Using in to Check if an Element Exists in a List
fruits = ['apple', 'banana', 'cherry']
print("Is 'banana' in the list?", 'banana' in fruits)
print("Is 'grape' in the list?", 'grape' in fruits)

#Program-10: Flattening a Nested List Using List Comprehension
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flat_list)