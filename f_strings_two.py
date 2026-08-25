name = "Alice"  # Name of the person
age = 25  # Age of the person
height = 5.678  # Height in feet
score = 0.876  # Score as a fraction
big_number = 987654321  # A large number for formatting examples


# 1: Create a formatted sentence with name and age
sentence = f"My name is {name}, and I am {age} years old."
print(sentence)


# 2: Create a formatted string for height rounded to 2 decimal places
formatted_height = f"My height is {height:.2f} feet."
print(formatted_height)


# 3: Create a formatted string for score as a percentage with 1 decimal place
formatted_score = f"My score is {score:.1%}."
print(formatted_score)


# 4: Create a formatted string for big_number with commas
formatted_big_number = f"The big number is {big_number:,}."
print(formatted_big_number)


# 5: Create a binary representation of the big number
binary_big_number = f"Binary: {big_number:b}"
print(binary_big_number)


# 6: Create an octal representation of the big number
octal_big_number = f"Octal: {big_number:o}"
print(octal_big_number)


# 7: Create a hexadecimal representation of the big number
hexadecimal_big_number = f"Hexadecimal: {big_number:x}"
print(hexadecimal_big_number)