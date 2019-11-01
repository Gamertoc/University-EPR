__author__ = "Oliver Theobald, 7146127"

# This program adds all odd integers between 2 and 20 and prints that value at every iteration
# of the loop
odd = 0
for i in range(2, 21):
    if i % 2 == 1:
        odd += i
    print(odd)
