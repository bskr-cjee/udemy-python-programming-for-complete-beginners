def count_a(text):
    """Given a string, count how many times the lowercase letter 'a' appears.
    Return the total count."""

    count = 0
    for char in text:
        if char == "a":     # Only lowercase 'a' will be counted. Use char.lower() if you want uppercase to be counted too.
            count += 1
    return count


# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Multiple a's
result1 = count_a("apple and banana")
print(f"'apple and banana' → {result1}")  # Should print 5

# Test 2: Begins with two a's
result2 = count_a("aardvark")
print(f"'aardvark' → {result2}")  # Should print 3

# Test 3: No a's
result3 = count_a("hello world")
print(f"'hello world' → {result3}")  # Should print 0

# Test 4: Empty string
result4 = count_a("")
print(f"Empty string → {result4}")  # Should print 0

# Test 5: Mixed 'a' and 'A'
result5 = count_a("aAaAaA")
print(f"'aAaAaA' → {result5}")  # Should print 3
