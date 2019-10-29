__author__ = "Oliver Theobald, 7146127"

# This program converts grade points (0-15) in grades (1+, 1, 1-, etc.)

n = int(input("Please enter a grade in points (0-15): "))

# I use this array to simply determine the according grade
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

print("The grade ", n, " equals ", grades.get(n), ". ", sep="", end="")
if n >= 5:
    print("The user passed the test.")
else:
    print("The user failed the test.")
