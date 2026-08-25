def is_ascending(numbers):
    """Given a list of numbers, return True if the numbers are in strict ascending order.
    Each number must be less than the one after it.
    If the list is empty or has one number, return True."""

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            return False
    # If we made it through the loop, the list is ascending
    return True


# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Regular ascending list
result1 = is_ascending([1, 2, 3, 4, 5])
print(f"[1, 2, 3, 4, 5] → {result1}")  # Should print: True

# Test 2: Duplicate value breaks strict order
result2 = is_ascending([2, 2, 3])
print(f"[2, 2, 3] → {result2}")  # Should print: False

# Test 3: Descending list
result3 = is_ascending([10, 9, 8])
print(f"[10, 9, 8] → {result3}")  # Should print: False

# Test 4: Single element list
result4 = is_ascending([5])
print(f"[5] → {result4}")  # Should print: True

# Test 5: Empty list
result5 = is_ascending([])
print(f"[] → {result5}")  # Should print: True

