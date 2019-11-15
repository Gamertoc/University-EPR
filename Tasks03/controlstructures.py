"""Replacing the while-loop with a for-loop"""

__author__ = "7146127, Theobald"


def increment(loops, step, start):
    """This program lets you define a starting point, the number of repetitions and the step
    length. From there it runs through the loop and prints every current and all previous numbers.
    :param loops: int
    :param step: int or float
    :param start: int or float
    :return: None
    """
    current = start
    prev_numbers = ""

    # Running the given amount of loops
    for i in range(loops):

        # If current (being a float) is an integer, we use it as an integer (increases readability)
        if current == int(current):
            current = int(current)

        # Here we create the string of all previous numbers and increase current.
        prev_numbers += " " + str(current)
        current += step

        # Printing them is the last step.
        print("Now, current is", current)
        print("All previous numbers:", prev_numbers, sep="")


def main():
    """Running the program at start."""

    # We need to make sure that we get valid input values
    while True:
        step = input("Please enter the step value (can be int or float): ")
        try:
            step = float(step)
            break
        except ValueError:
            continue

    # Same for the loop value, where we also have to make sure that it is above 0
    while True:
        loops = input("Please enter the number of repetitions (int): ")
        try:
            loops = int(loops)
            if loops <= 0:
                continue
            break
        except ValueError:
            continue

    # You can decide if you want to set a new start value (standard is 7)
    start = 7
    if input("Do you want a different start value than 7? (Y/n) ") == "Y":
        # If you want, we have to make sure that the value is valid
        while True:
            start = input("Please enter the new starting value (int or float): ")
            try:
                start = float(start)
                break
            except ValueError:
                continue
        increment(loops, step, start)
    else:
        increment(loops, step, 7)


if __name__ == '__main__':
    main()

# It's time for test cases again:
# 5, 3, n :
# Now, current is 12.0
# All previous numbers: 7
# Now, current is 17.0
# All previous numbers: 7 12
# Now, current is 22.0
# All previous numbers: 7 12 17

# -2, 8, Y, 10 :
# Now, current is 8.0
# All previous numbers: 10
# Now, current is 6.0
# All previous numbers: 10 8
# Now, current is 4.0
# All previous numbers: 10 8 6
# Now, current is 2.0
# All previous numbers: 10 8 6 4
# Now, current is 0.0
# All previous numbers: 10 8 6 4 2
# Now, current is -2.0
# All previous numbers: 10 8 6 4 2 0
# Now, current is -4.0
# All previous numbers: 10 8 6 4 2 0 -2
# Now, current is -6.0
# All previous numbers: 10 8 6 4 2 0 -2 -4

# Lol : Please enter the step value (can be int or float):

# 2.25, 10, Y, -5 :
# Now, current is -2.75
# All previous numbers: -5
# Now, current is -0.5
# All previous numbers: -5 -2.75
# Now, current is 1.75
# All previous numbers: -5 -2.75 -0.5
# Now, current is 4.0
# All previous numbers: -5 -2.75 -0.5 1.75
# Now, current is 6.25
# All previous numbers: -5 -2.75 -0.5 1.75 4
# Now, current is 8.5
# All previous numbers: -5 -2.75 -0.5 1.75 4 6.25
# Now, current is 10.75
# All previous numbers: -5 -2.75 -0.5 1.75 4 6.25 8.5
# Now, current is 13.0
# All previous numbers: -5 -2.75 -0.5 1.75 4 6.25 8.5 10.75
# Now, current is 15.25
# All previous numbers: -5 -2.75 -0.5 1.75 4 6.25 8.5 10.75 13
# Now, current is 17.5
# All previous numbers: -5 -2.75 -0.5 1.75 4 6.25 8.5 10.75 13 15.25
