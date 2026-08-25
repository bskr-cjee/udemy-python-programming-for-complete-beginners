print( "and logical operator:" )
print( True and True )        # True
print( True and False )       # False
print( False and True )       # False
print( False and False )      # False

print( "or logical operator:" )
print( True or True )         # True
print( True or False )        # True
print( False or True )        # True
print( False or False )       # False

# Logical operator order:
# not
# and
# or

print( "Operator precedence example:" )
print( True or not False and False )
# True or (not False) and False
# True or True and False
# True or False
# Output: True

print( "Operator precedence example with parentheses:" )
print( (True or not False) and False )
# (True or not False) and False
# (True or True) and False
# True and False
# Output: False