total_score = 100   # Global variable: accessible anywhere

def calculate_level_score():
    bonus_points = 50   # Local variable: only exists inside this function

    # Reading the global variable is allowed automatically
    current_total = total_score + bonus_points
    print(f"Inside function: Total with bonus is {current_total}")
    print(f"Inside function: Bonus points variable is {bonus_points}")

# Run the function
calculate_level_score()

print(f"\nOutside function: Global score is still {total_score}")

# This line will crash if uncommented because bonus_points does not exist here
# print(bonus_points)  # NameError: name 'bonus_points' is not defined