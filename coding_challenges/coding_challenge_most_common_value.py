def most_common(items):
    """Given a list of items, return the item that appears the most.
    If there's a tie, return any one of them.
    If the list is empty, return None."""

    my_dict = {}

    for item in items:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1

    most_duplicate = None
    max_count = 0

    for item, count in my_dict.items():
        if count > max_count:
            max_count = count
            most_duplicate = item

    return most_duplicate

# -----------------------------------
# Test Cases:
# -----------------------------------

# Test 1: Tie between two numbers
result1 = most_common([1, 2, 2, 3, 3])
print(f"[1, 2, 2, 3, 3] → {result1}")  # Should print: 2 or 3

# Test 2: Most common string
result2 = most_common(["a", "b", "a", "c"])
print(f'["a", "b", "a", "c"] → {result2}')  # Should print: "a"

# Test 3: One item
result3 = most_common([5])
print(f"[5] → {result3}")  # Should print: 5

# Test 4: Empty list
result4 = most_common([])
print(f"[] → {result4}")  # Should print: None

# Test 5: Large list with clear winner
result5 = most_common([1, 1, 1, 2, 3, 4])
print(f"[1, 1, 1, 2, 3, 4] → {result5}")  # Should print: 1
