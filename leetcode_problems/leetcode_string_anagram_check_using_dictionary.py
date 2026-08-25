def is_anagram(string1, string2):
    """This method checks if two strings are anagrams.
    Two strings are anagrams if they contain the same characters with the same frequencies, in any order.
    Do NOT use sorting methods. Use dictionaries to count characters manually."""

    # If the strings are not of the same length, they cannot be anagrams.
    if len(string1) != len(string2):
        return False

    # Createing two dictionaries to store the character counts for string1 and string2
    dict1 = {}
    dict2 = {}

    for char in string1:
        # If the letter is new, add it to the dictionary with a starting count of 1
        if char not in dict1:
            dict1[char] = 1
        # If the letter already exist in the dictionary, increment its count by 1
        else:
            dict1[char] += 1

    for char in string2:
        if char not in dict2:
            dict2[char] = 1
        else:
            dict2[char] += 1

    print(dict1, dict2)

    # If both dictionaries are same, i.e., both the strings have the same characters with same frequencies this returns true
    return dict1 == dict2



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