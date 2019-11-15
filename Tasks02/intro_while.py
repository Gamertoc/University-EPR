__author__ = "7146127, Theobald"

# This program tosses random one-digit integers until a 3 or a -9 is tossed
import random as dice  # Importing the random class lets us generate random integers within a range

# We generate the first random number and set the count to one
n = dice.randint(-9, 9)
count = 1

# We keep generating numbers and increasing the counter until we get a 3 or a -9
while n != 3 and n != -9:
    n = dice.randint(-9, 9)
    count += 1

# At the end we print the number that got tossed and how many attempts we needed for that
print(n, "got tossed after", count, "attempts.")


# The second version works the same as the first, except for the wile-loop that doesn't check
# for itself if the condition is met, rather an if-condition checks every number and - if it's a
# 3 or a -9 - leaves the while-loop with a break statement.
second = 0
while True:
    m = dice.randint(-9, 9)
    second += 1
    if m == 3 or m == -9:
        break

print(m, "got tossed after", second, "attempts.")
