def second_largest(numbers):
    """Given a list of integers, return the second largest number in the list.
    You may assume the list has at least two different numbers."""

    lar_num = sec_lar_num = float('-inf')

    for num in numbers:
        if num > lar_num:
            sec_lar_num = lar_num
            lar_num = num
        elif num > sec_lar_num and num != lar_num:
            sec_lar_num = num

    return sec_lar_num

# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Normal case
result1 = second_largest([5, 1, 9, 3, 7])
print(f"[5, 1, 9, 3, 7] → {result1}")  # Should print: 7

# Test 2: Only two numbers
result2 = second_largest([2, 4])
print(f"[2, 4] → {result2}")  # Should print: 2

# Test 3: With duplicates
result3 = second_largest([10, 10, 5, 8])
print(f"[10, 10, 5, 8] → {result3}")  # Should print: 8

# Test 4: Decreasing order
result4 = second_largest([100, 99, 50, 1])
print(f"[100, 99, 50, 1] → {result4}")  # Should print: 99

# Test 5: Negative numbers
result5 = second_largest([-5, -1, -3])
print(f"[-5, -1, -3] → {result5}")  # Should print: -3

