__author__ = "7146127, Theobald"

# This program receives a sentential formula and calculates the value of it
# We assume that the input has the format BOOL connection BOOL
# with BOOL being either True or False and connection being "and" or "or"
formula = input("Please enter a sentential formula (BOOL and/or BOOL): ")

# We split the input in parts so we can analyze it
parts = formula.split()
a = parts[0]
b = parts[2]
connection = parts[1]

# Determine whether the first statement is true or false
if a == "True":
    a = True
else:
    a = False

# Same goes for the second
if b == "True":
    b = True
else:
    b = False

# Check whether the connection is an "and" or an "or" and act accordingly
if connection == "and":
    result = a & b
else:
    result = a | b

print(result)

# Test cases incoming with the type: Input : Output
# True and True : True
# True and False : False
# False and True: False
# False and False : False
# True or True : True
# True or False : True
# False or True : True
# False or False : False
# With these all possible value combinations are covered and verified
