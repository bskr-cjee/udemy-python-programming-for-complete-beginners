def sum_digits(text):
    """Given a string made up of digits, return the sum of all the digits.
    For example, "1234" → 1 + 2 + 3 + 4 = 10
    If the string is empty, return 0."""
    sum = 0
    for x in text:
        sum += int(x)
    return sum


# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Typical number string
result1 = sum_digits("12345")
print(f'"12345" → {result1}')  # Should print: 15

# Test 2: Single digit
result2 = sum_digits("5")
print(f'"5" → {result2}')  # Should print: 5

# Test 3: All zeros
result3 = sum_digits("000")
print(f'"000" → {result3}')  # Should print: 0

# Test 4: Empty string
result4 = sum_digits("")
print(f'"" → {result4}')  # Should print: 0

# Test 5: Larger digits
result5 = sum_digits("908172")
print(f'"908172" → {result5}')  # Should print: 27
