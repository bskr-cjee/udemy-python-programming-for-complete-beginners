my_int = 5

# The if-elif-else structure is used for decision-making in Python.

# 1. The `if` block:
#    - This is the starting point of the decision-making structure.
#    - You can only have ONE `if` block in an if-elif-else structure.
#    - It checks a condition (in this case, if `my_int == 5`).
#    - If the condition is True, the code inside the `if` block executes.
if my_int == 5:
    print('my_int equals 5')  # This will not run because my_int is 4.

# 2. The `elif` block:
#    - Stands for "else if".
#    - You can have MULTIPLE `elif` blocks to check additional conditions.
#    - Each `elif` block is checked in order, only if the previous `if` or `elif` conditions are False.
#    - If the condition in the `elif` block is True, the code inside it runs, and no further blocks are checked.
elif my_int < 4:
    print('my_int is less than 4')  # This will run because my_int is 4.

# 3. The `else` block:
#    - The `else` block is optional and can be used at most ONCE.
#    - It executes only if NONE of the `if` or `elif` conditions are True.
#    - The `else` block does not check a condition—it runs as a default case.
else:
    print('my_int is greater than 5')  # This will not run because an elif condition was True.
