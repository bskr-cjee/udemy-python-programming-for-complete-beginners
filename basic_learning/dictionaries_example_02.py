data = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Step 1: Count occurrences using a dictionary
frequencies = {}
for item in data:
    if item in frequencies:
        frequencies[item] += 1
    else:
        frequencies[item] = 1

print(f'The dictionary looks like:{frequencies}')

# Step 2: Track the item with the highest count > 1
most_duplicate = None
max_count = 1  # Must be greater than 1 to be considered a duplicate

for item, count in frequencies.items():
    if count > max_count:
        max_count = count
        most_duplicate = item

print(f"Most duplicated item: {most_duplicate} (Appeared {max_count} times)")
# Output: Most duplicated item: apple (Appeared 3 times)