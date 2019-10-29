__author__ = "Oliver Theobald, 7146127"

# This program accepts an integer and determines wether it is dividable by 3, 5 and 7
n = int(input("Please enter an integer: "))

if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
    print("The number", n, "is dividable by 3, 5 and 7.")
elif n % 2 == 1:
    print("The number", n, "is odd.")
else:
    print("The number", n, "is even.")
