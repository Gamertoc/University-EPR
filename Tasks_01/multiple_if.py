__author__ = "7146127, Theobald"

# This program accepts an integer and determines whether it is dividable by 3, 5 and 7
# We assume that the value is an integer
n = int(input("Please enter an integer: "))

if n % 3 == 0 and n % 5 == 0 and n % 7 == 0: # Check if it's dividable
    print("The number", n, "is dividable by 3, 5 and 7.")
elif n % 2 == 1: # Check if the number is odd
    print("The number", n, "is odd.")
else: # Since the number isn't odd, it must be even
    print("The number", n, "is even.")

# Time for test cases:
# 187 : The number 187 is odd.
# 420 : The number 420 is dividable by 3, 5 and 7.
# 69 : The number 69 is odd.
# 42 : The number 42 is even.
# -420 : The number -420 is dividable by 3, 5 and 7.
# -13374206942 : The number -13374206942 is even.
# With these we covered all 3 possible solutions (dividable, even and odd) as well as negative
# and large numbers.
