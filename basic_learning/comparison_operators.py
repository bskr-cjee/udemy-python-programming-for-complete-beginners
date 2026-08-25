print("Comparing equality and inequality:")
print("5 == 5 is", 5 == 5)  # Outputs: True
print("5 == 4 is", 5 == 4)  # Outputs: False
print("5 != 4 is", 5 != 4)  # Outputs: True
print("5 != 5 is", 5 != 5)  # Outputs: False


print("\nType checking of the comparison result:")
print("Type of (5 == 5) is", type(5 == 5))  # Outputs: <class 'bool'>


print("\nComparisons between different data types:")
print("5 == 5.0 is", 5 == 5.0)  # Outputs: True, integer compared with float
print("5 == '5' is", 5 == "5")  # Outputs: False, integer compared with string
print("'5' == '5' is", "5" == "5")  # Outputs: True, string compared with string
print("'5' == '5' with different quotes is", "5" == '5')  # Outputs: True


print("\nGreater and less than comparisons:")
print("5 > 4 is", 5 > 4)   # Outputs: True
print("5 < 4 is", 5 < 4)   # Outputs: False
print("5 > 5 is", 5 > 5)   # Outputs: False
print("5 < 5 is", 5 < 5)   # Outputs: False


print("\nGreater or equal and less or equal comparisons:")
print("5 >= 5 is", 5 >= 5)  # Outputs: True
print("5 <= 5 is", 5 <= 5)  # Outputs: True
print("4 >= 5 is", 4 >= 5)  # Outputs: False
print("4 <= 5 is", 4 <= 5)  # Outputs: True


print("\nString comparisons based on lexicographical order:")
print("'cats' > 'dogs' is", "cats" > "dogs")  # Outputs: False
print("'cats' < 'dogs' is", "cats" < "dogs")  # Outputs: True
print("'bbb' > 'aaa' is", "bbb" > "aaa")    # Outputs: True
print("'BBB' > 'aaa' is", "BBB" > "aaa")    # Outputs: False, case sensitivity affects order
print("'cat2' > 'cat1' is", "cat2" > "cat1")  # Outputs: True, compares '2' and '1' as characters


# Checking comparisons with mixed data types (int and str)
# These will cause a TypeError if uncommented because they are not supported
# print(5 > "5")
# print(5 < "5")
