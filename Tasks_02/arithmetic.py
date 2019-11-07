__author__ = "7146127, Theobald"

# This program takes a natural number as input and returns the arithmetic mean for 1 to the
# natural number
n = input("Please enter an integer larger than 0: ")

# This construction is used to check if the given input has the correct format (integer) and an
# acceptable value (>0)
while True:
    while not n.isdigit():
        n = input("Please don't enter any strings or stuff like that, only integers > 0: ")
    n = int(n)
    if n <= 0:
        n = input("Please enter a value above 0: ")
    else:
        break

# now we calculate the arithmetic mean by adding all numbers from 1 to n together and dividing
# this by n
mean = 0
for i in range(1, n+1):
    mean += i
mean /= n

# Now we calculate the median. If n is an even number, then the median is the value between the
# both middle values. Since we get all integers from 1 to n, we can just take the mean value,
# round it down once and round it up once, add those together and divide those by 2.
if len(range(1, n+1)) % 2 == 0:
    median = ((mean//1) + (mean//1) + 1) / 2
else:  # If n is odd the median is the number with the same value as the mean
    median = int(mean//1)
# Essentially, the median has the same value as the arithmetic mean

# And at the end both values get printed
print("The arithmetic mean is", mean)
print("The median is", median)
