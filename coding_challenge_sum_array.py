def sum_list(numbers):
    """Given a list of numbers, return the total sum of all numbers.
    If the list is empty, return 0."""
    sum = 0
    for x in numbers:
        sum += x
    return sum



# Test 1: List with positive numbers
result1 = sum_list([1, 2, 3])
print(result1)  # Output: 6

# Test 2: List with positive and negative numbers
result2 = sum_list([10, -5, 5])
print(result2)  # Output: 10

# Test 3: Empty list
result3 = sum_list([])
print(result3)  # Output: 0

# Test 4: List with one number
result4 = sum_list([100])
print(result4)  # Output: 100

# Test 5: List with all zeros
result5 = sum_list([0, 0, 0])
print(result5)  # Output: 0