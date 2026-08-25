def repeat_word(word, count):
    
    """Given a word (string) and a number, return a new string that repeats the word that many times.
       There should be no spaces between the words.
       If count is 0, return an empty string."""

    str = word * count
    return str

# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Repeat "hi" 3 times
result1 = repeat_word("hi", 3)
print(f'"hi" * 3 → {result1}')  # Should print: hihihi

# Test 2: Repeat "abc" 2 times
result2 = repeat_word("abc", 2)
print(f'"abc" * 2 → {result2}')  # Should print: abcabc

# Test 3: Repeat "hello" 0 times
result3 = repeat_word("hello", 0)
print(f'"hello" * 0 → {result3}')  # Should print: (empty string)

# Test 4: Repeat "a" 5 times
result4 = repeat_word("a", 5)
print(f'"a" * 5 → {result4}')  # Should print: aaaaa

# Test 5: Repeat empty string
result5 = repeat_word("", 4)
print(f'"" * 4 → {result5}')  # Should print: (empty string)
