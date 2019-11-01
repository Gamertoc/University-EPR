__author__ = "Oliver Theobald, 7146127"

# This program tosses random one-digit integers until a 3 or a -9 is tossed
import random as dice

n = dice.randint(-9, 9)
count = 1

while n != 3 and n != -9:
    n = dice.randint(-9, 9)
    count += 1

print(n, "got tossed after", count, "attempts.")

second = 0
while True:
    m = dice.randint(-9, 9)
    second += 1
    if m == 3 or m == -9:
        break

print(m, "got tossed after", second, "attempts.")
