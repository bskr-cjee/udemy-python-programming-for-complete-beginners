def is_vowel(letter):
    """Given a single character, return True if it is a lowercase vowel: 'a', 'e', 'i', 'o', or 'u'.
    Return False if it is not a vowel. The check should be case-sensitive."""

    my_list = ["a", "e", "i", "o", "u"]
    if letter.lower() in my_list:
        return True
    else:
        return False


# Test Cases:
# -----------------------------------

# Test 1: Lowercase vowel
result1 = is_vowel("a")
print(f'"a" → {result1}')  # Should print: True

# Test 2: Another lowercase vowel
result2 = is_vowel("e")
print(f'"e" → {result2}')  # Should print: True

# Test 3: Not a vowel
result3 = is_vowel("b")
print(f'"b" → {result3}')  # Should print: False

# Test 4: Uppercase vowel
result4 = is_vowel("A")
print(f'"A" → {result4}')  # Should print: True

# Test 5: Last vowel
result5 = is_vowel("u")
print(f'"u" → {result5}')  # Should print: True
