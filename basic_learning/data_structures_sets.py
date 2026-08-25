"""Python Sets: Operations and Examples
This file covers the basics of working with sets and common operations such as adding, removing,
updating, and performing mathematical set operations."""

# --------------------------------------------
# Section 1: Creating Sets
# --------------------------------------------

# Create a set with unique elements
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Sets automatically remove duplicates
duplicate_list = [1, 1, 1, 1, 1]
unique_set = set(duplicate_list)
print("Set created from list with duplicates:", unique_set)

# Create an empty set
empty_set = set()
print("Empty set:", empty_set)

# --------------------------------------------
# Section 2: Adding and Updating Elements
# --------------------------------------------

# Add a single element to the set
my_set.add(6)
print("Set after adding 6:", my_set)

# Add multiple elements using update
my_set.update([7, 8, 9])
print("Set after updating with [7, 8, 9]:", my_set)

# --------------------------------------------
# Section 3: Removing Elements
# --------------------------------------------

# Remove an element using remove (throws an error if not found)
my_set.remove(9)
print("Set after removing 9:", my_set)

# Remove an element using discard (does not throw an error)
my_set.discard(10)  # 10 is not in the set, no error
print("Set after discarding 10:", my_set)

# Clear all elements from the set
my_set.clear()
print("Set after clearing all elements:", my_set)

# --------------------------------------------
# Section 4: Mathematical Set Operations
# --------------------------------------------

# Create two sets for operations
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}

# Union: Combines all elements from both sets
union_set = set_1 | set_2
print("Union of set_1 and set_2:", union_set)

# Intersection: Elements common to both sets
intersection_set = set_1 & set_2
print("Intersection of set_1 and set_2:", intersection_set)

# Difference: Elements in set_1 but not in set_2
difference_set = set_1 - set_2
print("Difference of set_1 and set_2:", difference_set)

# Symmetric Difference: Elements in either set_1 or set_2 but not both
symmetric_difference_set = set_1 ^ set_2
print("Symmetric difference of set_1 and set_2:", symmetric_difference_set)

