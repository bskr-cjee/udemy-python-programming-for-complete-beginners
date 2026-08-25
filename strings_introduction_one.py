my_string = 'Hello World!'


# Index:      0  1  2  3  4  5  6  7  8  9  10 11
# Characters: H  e  l  l  o     W  o  r  l  d  !

# Negative Index: -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
# Characters:       H   e   l   l   o       W   o   r   l   d   !


# Print the entire string to see the full content
print(my_string)  # Output: Hello World!

# Print the character at index 8 (9th position in the string)
print(my_string[8])  # Output: r

# Print the last character in the string
print(my_string[-1])  # Output: !

# Print the second-to-last character in the string
print(my_string[-2])  # Output: d

# Print the characters from index 3 to 7 (inclusive of index 3,
# exclusive of index 8), which selects a substring from the
# 4th to the 8th character
print(my_string[3:8])  # Output: lo Wo

# Print the first 8 characters of the string (from the beginning
# to the 8th index, not including the 8th index)
print(my_string[:8])  # Output: Hello Wo

# Print characters from index 3 to the end of the string
print(my_string[3:])  # Output: lo World!

# Print characters from index -9 to -4, counting from the end
# This retrieves characters from the 3rd to 8th index from the left
print(my_string[-9:-4])  # Output: lo Wo

# Print the entire string except for the last 4 characters
# This ends at index -4 (exclusive)
print(my_string[:-4])  # Output: Hello Wo

# Print the last 9 characters from the string
# This starts at index -9 and goes to the end
print(my_string[-9:])  # Output: lo World!

# Print characters from index 3 to the 4th-to-last index (exclusive)
# Index 3 represents the 4th character from the start, and
# index -4 represents the 4th character from the end
print(my_string[3:-4])  # Output: lo Wo
