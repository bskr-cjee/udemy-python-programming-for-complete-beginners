print( "Addition:" )
print( 5 + 5 )      # 10
print( 5 + 5.0 )    # 10.0 (integer + float = float)

print( "Addition Default Data Types:" )
print( type( 5 + 5 ) )      # <class 'int'>
print( type( 5 + 5.0 ) )    # <class 'float'>

print( "Change Data Types:")
print( float(5 + 5) )       # 10.0
print( int(5 + 5.0) )       # 10

print( "Subtraction:" )
print( 5 - 5 )      # 0
print( 5 - 5.0 )    # 0.0 (integer - float = float)

print( "Multiplication:" )
print( 5 * 5 )      # 25
print( 5 * 5.0 )    # 25.0 (integer * float = float)

print( "Division:" )
print( 5 / 5 )      # 1.0 ( Division always returns float )
print( 5 // 5 )     # 1 (// always returns integer)
print( 5 / 3 )      # 1.6666666666666667
print( 5 // 3 )     # 1 ( // floors the result )

print("Modulo:")
print( 7 % 2 )      # 1 ( If either number is float this returns float )
print( 8 % 2 )      # 0 ( If either number is float this returns float )

print("Exponent:")
print( 2 ** 3)      # 8 ( If either number is float this returns float )

print("Assignment Operators:")
my_int = 8
print( my_int )     # 8
my_int += 1
print( my_int )     # 9 ( += 1.0 would assign a float )
my_int -= 1
print( my_int )     # 8  ( -= 1.0 would assign float )
my_int *= 2
print( my_int )     # 16 ( *= 2.0 would assign float )
my_int /= 2
print( my_int )     # 8.0 ( //= always assigns a float )
my_int //= 2
print( my_int )     # 4.0 ( If my_int was an integer this assigns int )
my_int %= 2
print (my_int )     # 0.0 ( If both are integers then %= assigns int )
my_int += 2         # 2.0
my_int **= 3        # (2.0)^3
print( my_int )     # 8.0 ( If both are integers then **= assigns int )