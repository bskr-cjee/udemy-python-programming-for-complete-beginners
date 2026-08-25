"""Python Tuples: Basics and Operations
This file demonstrates how to work with tuples, a data type used for storing ordered, immutable collections."""


# --------------------------------------------
# Section 1: Creating Tuples
# --------------------------------------------

# Creating a tuple with multiple elements
my_tuple = (1, 2, 3, 4, 5)
print("Tuple with multiple elements:", my_tuple)

# Creating an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Creating a tuple with a single element (note the trailing comma)
single_element_tuple = (1,)
print("Tuple with a single element:", single_element_tuple)

# Tuples can hold mixed data types
mixed_tuple = (1, 2.0, 3.0, True, "Hello")
print("Tuple with mixed data types:", mixed_tuple)

# Nested tuples
nested_tuple = ((1, 2, 3), (4, 5, 6))
print("Nested tuple:", nested_tuple)

# --------------------------------------------
# Section 2: Accessing Elements
# --------------------------------------------

# Access elements by index
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Access elements in nested tuples
print("First element of the first tuple in nested_tuple:", nested_tuple[0][0])

# --------------------------------------------
# Section 3: Tuple Operations
# --------------------------------------------

# Count the occurrences of a value
my_tuple = (1, 2, 3, 4, 5, 5)
print("Count of 5 in my_tuple:", my_tuple.count(5))

# Find the index of a value
print("Index of 3 in my_tuple:", my_tuple.index(3))

# --------------------------------------------
# Section 4: Advantages of Tuples
# --------------------------------------------

# Tuples are faster and use less memory compared to lists
my_list = [1, 2, 3, 4, 5, 5]
print("List:", my_list)
print("Tuple:", my_tuple)

# --------------------------------------------
# Section 5: Practical Uses of Tuples
# --------------------------------------------

# Storing RGB color values
sky_blue = (135, 206, 235)
print("RGB for Sky Blue:", sky_blue)

# Storing geographic coordinates
london_coordinates = (51.5074, -0.1278)
print("Geographic coordinates for London:", london_coordinates)

# Grouping related data
name = "John Doe"
role = "Engineer"
salary = 100000
employee = (name, role, salary)
print("Employee record:", employee)

# Unpacking tuples
name, role, salary = employee
print("Name:", name)
print("Role:", role)
print("Salary:", salary)

