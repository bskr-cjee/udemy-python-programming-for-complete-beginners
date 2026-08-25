def replace_spaces(text):
    """Given a string, return a new string with all spaces replaced by hyphens.
    Do not use the .replace() method. Loop through the string manually."""

    result = ""

    for char in text:
        if char == " ":
            result += "-"
        else:
            result += char

    return result

# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Normal sentence
result1 = replace_spaces("hello world")
print(f'"hello world" → {result1}')  # Should print: "hello-world"

# Test 2: Multiple single characters
result2 = replace_spaces("a b c")
print(f'"a b c" → {result2}')  # Should print: "a-b-c"

# Test 3: No spaces
result3 = replace_spaces("no_spaces_here")
print(f'"no_spaces_here" → {result3}')  # Should print: "no_spaces_here"

# Test 4: Leading and trailing spaces
result4 = replace_spaces("  leading and trailing ")
print(f'"  leading and trailing " → {result4}')
# Should print: "--leading-and-trailing-"

# Test 5: Empty string
result5 = replace_spaces("")
print(f'"" → {result5}')  # Should print: ""

