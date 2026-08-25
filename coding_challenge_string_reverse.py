def reverse_string(text):
    """Given a string, return a new string with the characters in reverse order.
    If the input is empty, return an empty string."""

    rev_str = ""
    for i in range(len(text) - 1, -1, -1):      # (start, stop, step)
        rev_str += text[i]

    return rev_str

# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Normal word
result1 = reverse_string("hello")
print(f'"hello" → {result1}')  # Should print: "olleh"

# Test 2: Another word
result2 = reverse_string("apple")
print(f'"apple" → {result2}')  # Should print: "elppa"

# Test 3: Empty string
result3 = reverse_string("")
print(f'"" → {result3}')  # Should print: ""

# Test 4: One character
result4 = reverse_string("a")
print(f'"a" → {result4}')  # Should print: "a"

# Test 5: Numbers as string
result5 = reverse_string("12345")
print(f'"12345" → {result5}')  # Should print: "54321"

