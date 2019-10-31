__author__ = "Oliver Theobald, 7146127"

# This program converts grade points (0-15) in grades (1+, 1, 1-, etc.)
# We assume that the input is an integer within the range of 0-15
n = int(input("Please enter a grade in points (0-15): "))

# I use this array to simply determine the according grades based on how we used them in school
grades = {
    15: "1+",
    14: "1",
    13: "1-",
    12: "2+",
    11: "2",
    10: "2-",
    9: "3+",
    8: "3",
    7: "3-",
    6: "4+",
    5: "4",
    4: "4-",
    3: "5+",
    2: "5",
    1: "5-",
    0: "6"
}

# In my school you pass the test when you have at least 5 points. Since the same goes for the
# Abitur, I'm gonna use this
print(n, " points equals ", grades.get(n), ". ",  sep="", end="")
if n >= 5:
    print("The user passed the test.")
else:
    print("The user failed the test.")

# Test cases (as always Input : Output)
# 0 : 0 points equals 6. The user failed the test.
# 15 : 15 points equals 1+. The user passed the test.
# 10 : 10 points equals 2-. The user passed the test.
# 4 : 4 points equals 4-. The user failed the test.
