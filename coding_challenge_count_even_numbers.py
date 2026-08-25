def count_evens(numbers):
    """Given a list of numbers, count how many are even (divisible by 2).
    Return the total count of even numbers. If the list is empty, return 0."""

    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Mixed even and odd numbers
result1 = count_evens([1, 2, 3, 4, 5])
print(f"[1, 2, 3, 4, 5] → {result1}")  # Should print 2

# Test 2: All even numbers
result2 = count_evens([2, 4, 6, 8])
print(f"[2, 4, 6, 8] → {result2}")  # Should print 4

# Test 3: All odd numbers
result3 = count_evens([1, 3, 5, 7])
print(f"[1, 3, 5, 7] → {result3}")  # Should print 0

# Test 4: Empty list
result4 = count_evens([])
print(f"[] → {result4}")  # Should print 0

# Test 5: List including zero and even/odd mix
result5 = count_evens([0, 11, 22, 33])
print(f"[0, 11, 22, 33] → {result5}")  # Should print 2

