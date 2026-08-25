def remove_vowels(text):
    """Given a string, return a new string with all lowercase vowels removed.
    Only remove: 'a', 'e', 'i', 'o', 'u'. Leave all other characters unchanged."""

    vowels = "aeiou"
    result = ""

    for char in text:
        if char not in vowels:
            result += char

    return result

# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Word with vowels
result1 = remove_vowels("hello")
print(f'"hello" → {result1}')  # Should print: "hll"

# Test 2: Sentence with vowels
result2 = remove_vowels("apple pie")
print(f'"apple pie" → {result2}')  # Should print: "ppl p"

# Test 3: All uppercase letters
result3 = remove_vowels("HELLO")
print(f'"HELLO" → {result3}')  # Should print: "HELLO"

# Test 4: All vowels
result4 = remove_vowels("aeiou")
print(f'"aeiou" → {result4}')  # Should print: ""

# Test 5: Empty string
result5 = remove_vowels("")
print(f'"" → {result5}')  # Should print: ""

