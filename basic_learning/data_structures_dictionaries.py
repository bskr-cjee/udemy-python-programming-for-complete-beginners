"""Python Dictionaries: Basics and Operations
This file demonstrates how to work with dictionaries,
a data type used for storing key-value pairs."""


# --------------------------------------------
# Section 1: Creating Dictionaries
# --------------------------------------------

# Creating a dictionary with key-value pairs
my_dict = {'name': 'Raj', 'role': 'Coder', 'salary': 120000}
print("Original dictionary:", my_dict)

# Creating an empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# --------------------------------------------
# Section 2: Accessing Values
# --------------------------------------------

# Accessing values using keys
print("Accessing 'name':", my_dict['name'])

# Using the get() method to access a value
print("Using get for 'role':", my_dict.get('role'))

# Using get() with a default value for missing keys
print("Using get with a missing key:", my_dict.get('age', 'Unknown'))

# --------------------------------------------
# Section 3: Modifying Dictionaries
# --------------------------------------------

# Updating a value
my_dict['salary'] = 130000
print("Dictionary after updating 'salary':", my_dict)

# Adding a new key-value pair
my_dict['age'] = 30
print("Dictionary after adding 'age':", my_dict)

# Removing a key-value pair using pop()
removed_value = my_dict.pop('age')
print("Value removed using pop():", removed_value)
print("Dictionary after pop():", my_dict)

# --------------------------------------------
# Section 4: Dictionary Methods
# --------------------------------------------

# Getting all keys
all_keys = my_dict.keys()
print("All keys:", all_keys)

# Getting all values
all_values = my_dict.values()
print("All values:", all_values)

# Getting all key-value pairs
all_items = my_dict.items()
print("All items:", all_items)

# --------------------------------------------
# Section 5: Nested Dictionaries
# --------------------------------------------

# Creating a nested dictionary
employees = {
    'Raj': {'role': 'Coder', 'salary': 130000},
    'Sam': {'role': 'Designer', 'salary': 115000}
}
print("Nested dictionary:", employees)

# Accessing nested dictionary values
print("Raj's salary:", employees['Raj']['salary'])

# Updating a value in the nested dictionary
employees['Raj']['salary'] = 135000
print("Nested dictionary after updating Raj's salary:", employees)

# --------------------------------------------
# Section 6: Dictionary Valid Keys and Values
# --------------------------------------------

# Keys must be immutable; common examples include strings, numbers, and tuples
valid_keys_dict = {
    'string_key': 'value',
    1: 'integer_key',
    1.0: 'float_key',
    (1, 2, 3): 'tuple_key'
}
print("Dictionary with valid keys:", valid_keys_dict)

# Values can be of any data type, including lists, tuples, or other dictionaries
complex_values_dict = {
    'list_key': [1, 2, 3],
    'tuple_key': (1, 2, 3),
    'dict_key': {'inner_key': 'inner_value'}
}
print("Dictionary with complex values:", complex_values_dict)

