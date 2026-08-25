#-----------------Example01-----------------
print("\n-----Example01-----")
# 1. Defining the function (Setting up the machine)
def greet_user(username):
    """This text explains what the function does (Docstring)."""
    greeting = f"Hello, {username}! Welcome back."
    return greeting  # Sends the result back to the user

# 2. Calling the function (Using the machine with different inputs)
message1 = greet_user("Alice")
message2 = greet_user("Bob")

# 3. Printing the results
print(message1)
print(message2)


#-----------------Example02-----------------
print("\n-----Example02-----")
def area(length, width = 15):
    return length * width

def perimeter(length, width = 15):
    return 2 * (length + width)

print("Area of the rectangle:", area(20, 10))               # 200
print("Perimeter of the rectangle:", perimeter(20, 10))     # 60

print("Area using default width:", area(20))                # 300
print("Perimeter using default width:", perimeter(20))      # 70