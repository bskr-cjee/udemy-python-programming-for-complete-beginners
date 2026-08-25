# Given a whole number, determine whether it is even or odd.
# Return the string "even" if the number is evenly divisible by 2.
# Return the string "odd" if it is not.

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


# Test 1: Positive even number
result1 = even_or_odd(4)
if result1 is not None:
    print(f"4 is {result1}")  # Should print: even

# Test 2: Positive odd number
result2 = even_or_odd(7)
if result2 is not None:
    print(f"7 is {result2}")  # Should print: odd

# Test 3: Zero
result3 = even_or_odd(0)
if result3 is not None:
    print(f"0 is {result3}")  # Should print: even

# Test 4: Negative even number
result4 = even_or_odd(-6)
if result4 is not None:
    print(f"-6 is {result4}")  # Should print: even

# Test 5: Negative odd number
result5 = even_or_odd(-3)
if result5 is not None:
    print(f"-3 is {result5}")  # Should print: odd
