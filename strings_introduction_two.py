my_string = 'Hello World!'


# Task 1: Print the character at index 8 (9th position in the string)
task_1 = my_string[8]
print(task_1)  # Output: r

# Task 2: Print the last character in the string using negative indexing
task_2 = my_string[-1]
print(task_2)  # Output: !

# Task 3: Print the second-to-last character in the string using negative indexing
task_3 = my_string[-2]
print(task_3)  # Output: d

# Task 4: Print the characters from index 3 to 7 (inclusive of index 3, exclusive of index 8)
task_4 = my_string[3:8]
print(task_4)  # Output: lo Wo

# Task 5: Print the first 8 characters of the string (from the beginning to the 8th index, not including the 8th index)
task_5 = my_string[:8]
print(task_5)  # Output: Hello Wo

# Task 6: Print characters from index 3 to the end of the string
task_6 = my_string[3:]
print(task_6)  # Output: lo World!

# Task 7: Print characters from index -9 to -4, counting from the end
task_7 = my_string[-9:-4]
print(task_7)  # Output: lo Wo

# Task 8: Print the entire string except for the last 4 characters
task_8 = my_string[:-4]
print(task_8)  # Output: Hello Wo

# Task 9: Print the last 9 characters from the string
task_9 = my_string[-9:]
print(task_9)  # Output: lo World!

# Task 10: Print characters from index 3 to the 4th-to-last index (exclusive)
task_10 = my_string[3:-4]
print(task_10)  # Output: lo Wo
