print("Example 01")
coordinates = [(x, y) for x in range(2) for y in range(3)]
print(coordinates)

print("\nExample 02")   # Multiplication table up to 3 using nested while loops
i = 1
while i <= 3:                   # Outer loop
    j = 1
    while j <= 10:               # Inner loop
        print(f"{i}x{j}={i*j}", end="\t")
        j += 1
    print()                     # Line break
    i += 1

print("\nExample 03")   # Printing a right-angled triangle pattern
rows = 5
for i in range(1, rows + 1):    # Outer loop dictates number of rows
    for j in range(i):          # Inner loop dictates stars per row
        print("*", end=" ")
    print()                     # Move to the next line


print("\nExample 04")   # Printing a inverted right-angled triangle pattern
rows = 5
for i in range(rows, 0, -1):    # Outer loop counts backward from 'rows' down to 1
    for j in range(i):          # Inner loop prints stars based on current row size
        print("*", end=" ")
    print()


print("\nExample 05")   # Printing a pyramid pattern
rows = 5
for i in range(rows):
    for j in range(rows - i - 1):   # Inner loop 1: Prints leading spaces to push stars right
        print(" ", end="")
    for k in range(2 * i + 1):  # Inner loop 2: Prints the stars
        print("*", end="")
    print()


print("\nExample 06")   # Printing inverted pyramid pattern
rows = 5
for i in range(rows, 0, -1):    # Outer loop counts backward from rows down to 1
    for j in range(rows - i):   # Inner loop 1: Prints increasing spaces to push stars right
        print(" ", end="")
    for k in range(i):  # Inner loop 2: Prints decreasing stars
        print("* ", end="")
    print()  # Move to the next line


print("\nExample 07: ")     #printing fibonacci series in pyramid pattern
rows = 5
a, b = 0, 1     # Initialize the first two numbers of the Fibonacci sequence

for i in range(1, rows + 1):    # Inner loop 1: Prints decreasing spaces to center the pyramid
    # Multiply by 3 to match the wider spacing of larger numbers
    for j in range(rows - i):
        print("   ", end="")

    for k in range(i):  # Inner loop 2: Prints the Fibonacci numbers for the current row
        # Format with width 5 to keep columns perfectly aligned as numbers grow
        print(f"{a:<5}", end=" ")

        # Calculate the next Fibonacci number
        a, b = b, a + b

    print()  # Move to the next line


