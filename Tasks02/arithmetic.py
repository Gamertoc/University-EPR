__author__ = "7146127, Theobald"

# This program takes a natural number as input and returns the arithmetic mean for 1 to the
# natural number

n = int(input("Please enter an integer larger than 0: "))

mean = 0
for i in range(1, n+1):
    mean += i

mean /= n
print("The arithmetic mean is", mean)

if len(range(1, n+1)) % 2 == 0:
    median = ((mean//1) + (mean//1) + 1) / 2
else:
    median = int(mean//1)

print("The median is", median)
