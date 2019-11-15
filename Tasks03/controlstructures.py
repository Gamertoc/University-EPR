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
        print("Now, current is ", current)
        print("All previous numbers: ", prev_numbers)


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

    # Same for the loop value
    while True:
        loops = input("Please enter the number of repetitions (int): ")
        try:
            loops = int(loops)
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
