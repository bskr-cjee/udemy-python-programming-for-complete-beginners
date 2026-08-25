def rotate_array(nums, k):
    """Rotates the given list to the right by k steps. The rotation is done in-place using reversal.
    This method modifies the list directly and does not return anything.
    Use the helper function reverse() in your solution."""
    n = len(nums)
    if n == 0 or k % n == 0:
        return
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)



# Helper function to reverse a section of the list from index start to end (inclusive)
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# -----------------------------------
# Test Cases:
# -----------------------------------
# Test 1
arr1 = [1, 2, 3, 4, 5, 6, 7]
rotate_array(arr1, 3)
print(f"→ {arr1}")  # Should print: [5, 6, 7, 1, 2, 3, 4]

# Test 2
arr2 = [1, 2]
rotate_array(arr2, 5)
print(f"→ {arr2}")  # Should print: [2, 1]

# Test 3
arr3 = [10, 20, 30]
rotate_array(arr3, 0)
print(f"→ {arr3}")  # Should print: [10, 20, 30]

# Test 4
arr4 = [4, 3, 2, 1]
rotate_array(arr4, 4)
print(f"→ {arr4}")  # Should print: [4, 3, 2, 1]

# Test 5
arr5 = []
rotate_array(arr5, 1)
print(f"→ {arr5}")  # Should print: []

