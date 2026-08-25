def convert_temperature(temp, unit):
    """This function converts a given temperature from Celsius to Fahrenheit or vice versa.

    Parameters:
      temp (float): The temperature value to convert.
      unit (str): 'C' for Celsius or 'F' for Fahrenheit.
    Returns:
      float: The converted temperature if the unit is valid.
      None: If an invalid unit is provided.

    Formula to Convert Celsius to Fahrenheit: F = (C * 9/5) + 32
    Formula to Convert Fahrenheit to Celsius: C = (F - 32) * 5/9

    Example usage:
      convert_temperature(20, 'C')  # Expected output: 68.0
      convert_temperature(68, 'F')  # Expected output: 20.0
    """

    if unit == "C":
        fah = (temp * 9 / 5) + 32
        return fah
    elif unit == "F":
        cel = (temp - 32) * 5 / 9
        return cel
    else:
        return None


# TEST CASES:
# -----------------------------------

# Test 1: Convert 25°C to Fahrenheit
result1 = convert_temperature(25, "C")
if result1 is not None:
    print(f"25°C is {result1}°F")   # Should print 77.0°F

# Test 2: Convert 98.6°F to Celsius
result2 = convert_temperature(98.6, "F")
if result2 is not None:
    print(f"98.6°F is {result2}°C")     # Should print 37.0°C

# Test 3: Convert 0°C to Fahrenheit
result3 = convert_temperature(0, "C")
if result3 is not None:
    print(f"0°C is {result3}°F")  # Should print 32.0°F

# Test 4: Convert 212°F to Celsius
result4 = convert_temperature(212, "F")
if result4 is not None:
    print(f"212°F is {result4}°C")  # Should print 100.0°C

# Test 5: Convert using invalid unit
result5 = convert_temperature(100, "K")
if result5 is None:
    print("Invalid unit provided.")  # Should print this

# Test 6: Convert -40°C to Fahrenheit
result6 = convert_temperature(-40, "C")
if result6 is not None:
    print(f"-40°C is {result6}°F")  # Should print -40.0°F

# Test 7: Convert -40°F to Celsius
result7 = convert_temperature(-40, "F")
if result7 is not None:
    print(f"-40°F is {result7}°C")  # Should print -40.0°C

