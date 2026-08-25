# Define a sample string
my_string = "Hello World"

# Length of the string
length = len(my_string)  # Returns 11

# Check string characteristics
is_lower = my_string.islower()  # Returns False
is_upper = my_string.isupper()  # Returns False
is_alpha = my_string.isalpha()  # Returns False (due to space)
is_digit = my_string.isdigit()  # Returns False
is_alnum = my_string.isalnum()  # Returns False (due to space)
is_space = my_string.isspace()  # Returns False

# Convert string case
lower_str = my_string.lower()  # 'hello world'
upper_str = my_string.upper()  # 'HELLO WORLD'
cap_str = my_string.capitalize()  # 'Hello world'
title_str = my_string.title()  # 'Hello World'
swap_str = my_string.swapcase()  # 'hELLO wORLD'

# Stripping spaces
strip_str = my_string.strip()  # 'Hello World'
lstrip_str = my_string.lstrip()  # 'Hello World  ' (left strip)
rstrip_str = my_string.rstrip()  # '  Hello World' (right strip)

# Prefix and Suffix checks
starts_with_hello = my_string.startswith("Hello")  # True
ends_with_world = my_string.endswith("World")  # True

# Replacing substrings
replaced_str = my_string.replace("World", "Python")  # 'Hello Python'

# Finding substrings
find_world = my_string.find("World")  # Returns 6
find_l = my_string.find("l")  # Returns 2
find_nonexist = my_string.find("abc123")  # Returns -1 (not found)

# Counting substrings
count_l = my_string.count("l")  # Returns 3
count_world = my_string.count("World")  # Returns 1
count_nonexist = my_string.count("abc123")  # Returns 0

# Output examples
print("Original String:", my_string)
print("Lowercase:", lower_str)
print("Uppercase:", upper_str)
print("Title Case:", title_str)
print("Replaced String:", replaced_str)
print("First 'l' found at index:", find_l)
print("Count of 'l':", count_l)



#  Splitting and Joining

# .split(separator) splits the string into a list of substrings based on a separator.
print("Split into list:", my_string.split())  # Output: ['Hello', 'World']

# .join(iterable) joins a list of strings into a single string, separated by the specified separator.
words = ['Hello', 'World']
print("Joined list into string:", " ".join(words))  # Output: Hello World
