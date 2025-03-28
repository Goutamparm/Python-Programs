#Program-1: Creating and Accessing a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Name:", person["name"])
print("Age:", person["age"])

#Program-2: Adding and Updating Key-Value Pairs
person = {"name": "Alice", "age": 25}
person["city"] = "New York"
person["age"] = 26
print("Updated dictionary:", person)

#Program-3: Removing Key-Value Pairs from a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
del person["age"]
print("After removing 'age':", person)

#Program-4: Checking if a Key Exists in a Dictionary
person = {"name": "Alice", "age": 25}
print("Is 'name' a key in the dictionary?", "name" in person)
print("Is 'city' a key in the dictionary?", "city" in person)

#Program-5: Looping Through a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

#Program-6: Getting Keys and Values Separately
person = {"name": "Alice", "age": 25, "city": "New York"}
keys = person.keys()
values = person.values()
print("Keys:", list(keys))
print("Values:", list(values))

#Program-7: Merging Two Dictionaries
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

#Program-8: Using the get() Method to Retrieve Values
person = {"name": "Alice", "age": 25}
print("Name:", person.get("name"))
print("City:", person.get("city", "Not found"))

#Program-9: Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print("Dictionary of squares:", squares)

#Program-10: Finding the Length of a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Number of key-value pairs in the dictionary:", len(person))
