__author__ = "7146127, Theobald"

# This program adds all odd integers between 2 and 20,
odd_sum = 0
odd_all = []
for i in range(2, 21):
    if i % 2 == 1:
        odd_sum += i
        odd_all.append(i)  # puts them in a list,
        print(odd_all)  # prints the list at every iteration
print(odd_sum)  # and prints the sum at the end.
