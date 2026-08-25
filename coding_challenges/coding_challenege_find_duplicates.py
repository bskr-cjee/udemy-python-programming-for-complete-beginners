def find_duplicates(numbers):
    """Given a list of numbers, return a new list that contains all numbers that appear more than once.
    Each duplicate should appear only once in the result.
    If there are no duplicates, return an empty list."""

    my_set = set()
    duplicates = set()

    for num in numbers:
        if num in my_set:
            duplicates.add(num)
        else:
            my_set.add(num)

    return list(duplicates)

# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Two duplicates
result1 = find_duplicates([1, 2, 2, 3, 4, 4])
print(f"[1, 2, 2, 3, 4, 4] → {result1}")  # Should print: [2, 4]

# Test 2: One number repeated many times
result2 = find_duplicates([5, 5, 5, 5])
print(f"[5, 5, 5, 5] → {result2}")  # Should print: [5]

# Test 3: No duplicates
result3 = find_duplicates([1, 2, 3])
print(f"[1, 2, 3] → {result3}")  # Should print: []

# Test 4: Multiple duplicates
result4 = find_duplicates([7, 8, 9, 7, 8])
print(f"[7, 8, 9, 7, 8] → {result4}")  # Should print: [7, 8]

# Test 5: Empty list
result5 = find_duplicates([])
print(f"[] → {result5}")  # Should print: []

