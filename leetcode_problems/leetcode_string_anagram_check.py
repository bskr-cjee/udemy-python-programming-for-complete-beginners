def is_anagram(string1, string2):
    """This method checks if two strings are anagrams.
    Two strings are anagrams if they contain the same characters with the same frequencies, in any order.
    Do NOT use sorting methods or built-in sorted()."""

    my_list = list(string2)

    for char in string1:
        if char in my_list:
            my_list.remove(char)
        else:
            return False
    return True

# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Anagrams with same letters
result1 = is_anagram("listen", "silent")
print(f'"listen", "silent" → {result1}')  # Should print: True

# Test 2: Completely different strings
result2 = is_anagram("hello", "world")
print(f'"hello", "world" → {result2}')  # Should print: False

# Test 3: Anagrams with repeated letters
result3 = is_anagram("anagram", "nagaram")
print(f'"anagram", "nagaram" → {result3}')  # Should print: True

# Test 4: Same letters but not same frequency
result4 = is_anagram("aacc", "ccac")
print(f'"aacc", "ccac" → {result4}')  # Should print: False

# Test 5: Different lengths
result5 = is_anagram("rat", "car")
print(f'"rat", "car" → {result5}')  # Should print: False

