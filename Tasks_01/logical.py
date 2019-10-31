__author__ = "Oliver Theobald, 7146127"

# This program receives a sentential formula and calculates the value of it
# We assume that the input has the format BOOL connection BOOL
# with BOOL being either True or False and connection being "and" or "or"
formula = input("Please enter a sentential formula (BOOL and/or BOOL): ")

# We split the input in parts so we can analyze it
parts = formula.split()
a = parts[0]
b = parts[2]
connection = parts[1]

if a == "False" or a == "false":
    a = 0
else:
    a = 1

if b == "False" or b == "false":
    b = 0
else:
    b = 1

result = a + b

if (connection == "and" and result == 2) or (connection == "or" and result > 0):
    result = True
else:
    result = False

print(result)
