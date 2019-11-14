"""Replacing the while-loop with a for-loop"""

__author__ = "7146127, Theobald"


def increment(loops, step):
    """

    """
    x = 7
    string = ""
    for i in range(loops):
        string += " " + str(x)
        x += step
        print("Now, x is ", x)
        print("All previous numbers: ", string)


def main():
    """

    """
    step = int(input("Please enter the step value: "))
    loops = int(input("Please enter the number of loops: "))
    increment(loops, step)


if __name__ == '__main__':
    main()
