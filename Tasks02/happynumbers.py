__author__ = "7146127, Theobald"

# This program checks whether an integer is happy or not. For this it squares every digit of the
# given integer and adds them to one vale. Rinse and repeat until a) the 1 is reached - the
# number is happy - or b) it ends in a periodic cycle of 4, 16, 37, 58, 89, 145, 42, 20,
# 4... - the number is unhappy.

n = input("Please enter a natural number: ")
save = n  # We save the original number so we can use it in the output

# We use this conception to check whether the input is really a number and to check if it is
# above 0
while True:
    while not n.isdigit():
        n = input("Please don't enter any strings or stuff like that, only natural numbers: ")
    n = int(n)
    if n <= 0:
        n = input("Please enter a value above 0: ")
    else:
        n = str(n)
        break


count = 0  # This counts our iterations
while True:
    count += 1  # We increase the count by one for every iteration
    square = 0  # Something to temporarily store the value of the squared digits

    # Since n is a string, we can work by just going through every character of n, square and
    # add those
    for i in range(len(n)):
        square += eval(n[i]) ** 2

    # If the squared value reaches 1, the number is happy and we can stop the program
    if square == 1:
        print(save, "is a happy number.")
        exit()

    # If the number reaches anything in the set below, it will be stuck there forever (since you
    # always repeat that cycle), and we can say that the number is unhappy
    elif square in {4, 16, 37, 58, 89, 145, 42, 20}:
        print(save, "is an unhappy number.")
        exit()

    # Another option is when we are exceeding 100 iterations without reaching any of the above,
    # then the program terminates to avoid running in eternity
    elif count >= 100:
        print("Stopped after 100 iterations.")
        exit()

    # We set the squared number as our new n and make it a string since that's what we are
    # working with
    n = str(square)
