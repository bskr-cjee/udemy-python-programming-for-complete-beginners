# Given two numbers (a and b), return the one that is greater.
# If both are the same, return either one.

def maximum(a, b):
    if a > b:
        return a
    else:
        return b


# Test 1: First is smaller
result1 = maximum(10, 20)
print(f"Max of 10 and 20 is {result1}")  # Should print: 20

# Test 2: First is larger
result2 = maximum(8, 4)
print(f"Max of 8 and 4 is {result2}")    # Should print: 8

# Test 3: Negative numbers
result3 = maximum(-5, -2)
print(f"Max of -5 and -2 is {result3}")  # Should print: -2

# Test 4: Both numbers are equal
result4 = maximum(7, 7)
print(f"Max of 7 and 7 is {result4}")    # Should print: 7
