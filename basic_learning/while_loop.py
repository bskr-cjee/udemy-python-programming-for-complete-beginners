# example01
secret_word = "Python"
user_input = ""

# Keep asking until the user types the correct secret word
while user_input != secret_word:
    user_input = input("Enter the secret keyword to exit: ")
print("Access Granted!")

# example02
print("\nExample 02")
count = 1   # Initialize a counter variable
while count <= 5:   # The loop runs as long as count is less than or equal to 5
    print(count, end = " ")
    count += 1  # Increment the counter to eventually end the loop

# example03
print("\nExample 03")
num = 5
while not num < 1:
    print( num, end = " " )
    num -= 1

# example04: Break & Continue
number = 0

while number < 10:
    number += 1
    # SKIP: If the number is 5, skip the rest of this loop iteration
    if number == 5:
        continue
    # STOP: If the number is 8, exit the entire loop immediately
    if number == 8:
        break
    print(f"Processing number: {number}")

print("Loop finished!")