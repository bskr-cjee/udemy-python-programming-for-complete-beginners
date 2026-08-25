
"""List Operations: Indexing, Slicing, Modifying
This file contains examples and explanations to help you review list operations in Python."""


# --------------------------------------------
# Section 1: Creating and Accessing Lists
# --------------------------------------------

# Create a list with various data types
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Accessing elements by index
# Indexing starts at 0. Negative indices access elements from the end.
print("First element (index 0):", my_list[0])
print("Last element (index -1):", my_list[-1])

# --------------------------------------------
# Section 2: Slicing Lists
# --------------------------------------------

# Slicing extracts a portion of the list. The syntax is [start:end].
print("Elements from index 1 to 2:", my_list[1:3])  # Includes index 1, excludes index 3
print("Elements from start to index 2:", my_list[:3])  # Up to, but not including, index 3
print("Elements from index 2 to end:", my_list[2:])  # From index 2 to the end

# Nested list indexing
nested_list = [[88, 99], 2.0, 3.0, True, 'Hello']
print("Nested list:", nested_list)
print("First element of nested list:", nested_list[0])
print("Second element of the first sub-list:", nested_list[0][1])

# --------------------------------------------
# Section 3: Modifying Lists
# --------------------------------------------

# Modifying elements by index
my_list[2] = 'Z'  # Replace the element at index 2 with 'Z'
print("List after modification:", my_list)

# --------------------------------------------
# Section 4: Adding Elements
# --------------------------------------------

# Append adds an element to the end of the list
my_list.append(99)
print("List after appending 99:", my_list)

# Insert adds an element at a specific index
my_list.insert(1, 88)
print("List after inserting 88 at index 1:", my_list)

# Extend adds multiple elements to the end of the list
my_list.extend([101, 102])
print("List after extending:", my_list)

# --------------------------------------------
# Section 5: Removing Elements
# --------------------------------------------

# Remove deletes the first occurrence of a value
my_list.remove(88)
print("List after removing 88:", my_list)

# Pop removes and returns the element at a specific index (default is the last element)
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

# Deleting an element by index
del my_list[2]
print("List after deleting element at index 2:", my_list)

# --------------------------------------------
# Section 6: Sorting Lists
# --------------------------------------------

# Sorting a list in ascending order
unsorted_list = [4, 5, 2, 1, 3]
unsorted_list.sort()
print("Sorted list:", unsorted_list)

# Sorting in descending order
unsorted_list.sort(reverse=True)
print("List sorted in descending order:", unsorted_list)
