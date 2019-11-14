"""Replacing the while-loop with a for-loop"""

__author__ = "7146127, Theobald"


def increment(loops, step, x_start = 7):
    """

    :param loops: int
    :param step: int or float
    :param x_start: int or float
    :return: None
    """
    x = x_start
    prev_numbers = ""
    for i in range(loops):
        if x == int(x):
            x = int(x)
        prev_numbers += " " + str(x)
        x += step
        print("Now, x is ", x)
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
    if input("Do you want a different start value than 7? (Y/n) ") == "Y":
        # If you want, we have to make sure that the value is valid
        while True:
            x_start = input("Please enter the new starting value (int or float): ")
            try:
                x_start = float(x_start)
                break
            except ValueError:
                continue
        increment(loops, step, x_start)
    else:
        increment(loops, step)

if __name__ == '__main__':
    main()
