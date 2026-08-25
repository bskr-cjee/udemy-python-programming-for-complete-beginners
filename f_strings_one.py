name = "YourName"
print(f"My name is {name}!")
print(f"{name = }")


# Demonstrating various f-string usages with "Hello World"

my_string = "Hello World"

# Basic Usage
# Expected Output: My string says: Hello World
print(f"My string says: {my_string}")

# String Truncation
# Expected Output: Truncated string: Hello
print(f"Truncated string: {my_string:.5}")

# Case Manipulation
# Expected Output: Uppercase: HELLO WORLD
print(f"Uppercase: {my_string.upper()}")
# Expected Output: Lowercase: hello world
print(f"Lowercase: {my_string.lower()}")

# Alignment and Width
# Expected Output: Left aligned within 20 chars: |Hello World        |
print(f"Left aligned within 20 chars: |{my_string:<20}|")
# Expected Output: Right aligned within 20 chars: |        Hello World|
print(f"Right aligned within 20 chars: |{my_string:>20}|")
# Expected Output: Center aligned within 20 chars: |    Hello World    |
print(f"Center aligned within 20 chars: |{my_string:^20}|")

# Character Count
count_l = my_string.count('l')
# Expected Output: Number of 'l' in 'Hello World': 3
print(f"Number of 'l' in '{my_string}': {count_l}")

# Including Special Characters
# Expected Output: Curly braces around the string: {Hello World}
print(f"Curly braces around the string: {{{my_string}}}")
# Expected Output: String in quotes: 'Hello World'
print(f"String in quotes: '{my_string}'")

# Combining with Arithmetic
length = len(my_string)
# Expected Output: Length of 'Hello World' plus 5: 16
print(f"Length of '{my_string}' plus 5: {length + 5}")



# Demonstrating various f-string formatting options in Python

# Fixed point number formatting
# Formats the number to two decimal places
num = 3.14159
print(f"Fixed point number: {num:.2f}")  # Expected Output: Fixed point number: 3.14

# Percentage formatting
# Converts the float to a percentage and formats to two decimal places
completion = 0.756
print(f"Percentage: {completion:.2%}")  # Expected Output: Percentage: 75.60%

# Scientific notation formatting
# Formats the number in scientific notation with two decimal places in the exponent
num_large = 1200.5
print(f"Scientific notation: {num_large:.2e}")  # Expected Output: Scientific notation: 1.20e+03

# Thousands separator formatting
# Formats the integer with commas as thousands separators
population = 123456789
print(f"Thousands separator: {population:,}")  # Expected Output: Thousands separator: 123,456,789

# Alignment formatting
# Demonstrates left, right, and center alignment within a field of 10 characters
name = "Alice"
print(f"Left aligned: {name:<10}")   # Expected Output: Left aligned: Alice
print(f"Right aligned: {name:>10}")  # Expected Output: Right aligned:      Alice
print(f"Center aligned: {name:^10}") # Expected Output: Center aligned:   Alice

# Padding with characters
# Pads the number with zeros on the left, making it at least two digits long
day = 5
print(f"Padded number: {day:0>2}")  # Expected Output: Padded number: 05

# Binary, octal, and hexadecimal format
# Formats the integer into binary, octal, and hexadecimal representations
num = 255
print(f"Binary format: {num:b}")         # Expected Output: Binary format: 11111111
print(f"Octal format: {num:o}")          # Expected Output: Octal format: 377
print(f"Hexadecimal format: {num:x}")    # Expected Output: Hexadecimal format: ff

# Date formatting
# Formats a datetime object into a human-readable date and time string
from datetime import datetime
now = datetime.now()
print(f"Formatted date and time: {now:%Y-%m-%d %H:%M}")  # Expected Output: Formatted date and time: 2024-05-21 15:45
