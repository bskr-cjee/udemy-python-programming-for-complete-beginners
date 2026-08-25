def remove_adjacent_duplicates(text):
    """Given a string, remove all adjacent duplicate characters in pairs.
    Use a stack-based approach to remove duplicates in one pass.
    Return the final reduced string after all adjacent pairs are removed."""
    stack = []

    for ch in text:
        # Check if the stack is not empty AND the top of the stack is the same the current character
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)   # Join the characters into a final result string and return.


# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Simple duplicate
result1 = remove_adjacent_duplicates("abbaca")
print(f'"abbaca" → {result1}')  # Should print: "ca"

# Test 2: More duplicates to remove
result2 = remove_adjacent_duplicates("azxxzy")
print(f'"azxxzy" → {result2}')  # Should print: "ay"

# Test 3: Multiple collapse rounds
result3 = remove_adjacent_duplicates("aabcca")
print(f'"aabcca" → {result3}')  # Should print: "ba"

# Test 4: Collapses to empty
result4 = remove_adjacent_duplicates("abcddcba")
print(f'"abcddcba" → {result4}')  # Should print: ""

# Test 5: Empty string
result5 = remove_adjacent_duplicates("")
print(f'"" → {result5}')  # Should print: ""
