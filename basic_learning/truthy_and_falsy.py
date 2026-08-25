# Truthiness in Python: Basics
# In Python, conditions in if-statements evaluate to boolean values: True or False.

# Example of a boolean condition
if 5 == 5:
    print('The condition is True')  # This will print
    print(type(5 == 5))  # Outputs: <class 'bool'>

# Truthy and Falsy Values
# Python considers certain values as "Truthy" or "Falsy".
# Truthy values are treated as True, and Falsy values are treated as False.

# Examples of Truthy and Falsy Values

# Numeric Values
if 5:  # Non-zero numbers are Truthy
    print('5 is Truthy')

if -5:  # Negative numbers are also Truthy
    print('-5 is Truthy')

if 0:  # Zero is Falsy
    print('0 is Truthy')  # This will not print

# Strings
if "Hello":  # Non-empty strings are Truthy
    print('"Hello" is Truthy')

if "":  # Empty strings are Falsy
    print('Empty string is Truthy')  # This will not print

if "   ":  # Strings with spaces are also Truthy
    print('String with spaces is Truthy')

# Variables
my_var = 5
if my_var:  # Any non-zero or non-empty variable is Truthy
    print(f'{my_var} is Truthy')  # Outputs: 5 is Truthy

my_var = 0
if my_var:  # Zero is Falsy
    print(f'{my_var} is Truthy')  # This will not print

my_var = ""
if my_var:  # Empty strings are Falsy
    print(f'{my_var} is Truthy')  # This will not print

my_var = None
if my_var:  # None is Falsy
    print('None is Truthy')  # This will not print

my_var = False
if my_var:  # The value False is Falsy
    print('False is Truthy')  # This will not print

# Summary of Falsy Values
# Python considers the following values as Falsy:
# - None
# - False
# - 0 (integer)
# - 0.0 (float)
# - "" (empty string)
# - [] (empty list)
# - {} (empty dictionary)
# - set() (empty set)

# Everything else is considered Truthy.
