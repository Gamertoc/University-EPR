"""The functions get two integers and do different things with them.

The first function returns the average of the two numbers,
the second function

"""

__author__ = "7146127, Theobald"


def average(x, y):
    """Returning the average of two integers and printing the average and the
    type of the average.

    """
    d = (int(x) + int(y)) / 2
    if (x + y) % 2 == 0:
        d = int(d)
    print(d, type(d))
    return d


def firstLastDigit(d):
    """Printing the first and last digit of the average and returning its
    length.

    """
    if d < 0:
        d = str(d)
        print(d[1], d[-1], sep="")
    else:
        d = str(d)
        print(d[0], d[-1], sep="")
    return len(d)


def backwards(d):
    """

    :param d:
    :return:
    """
    d = str(d)
    d_backwards = ""
    for i in range(len(d)):
        d_backwards += d[-i - 1]
    return d_backwards


def main():
    """

    """
    x = int(input("Please enter the first integer: "))
    y = int(input("Please enter the second integer: "))
    d = average(x, y)
    firstLastDigit(d)
    print(backwards(d))


if __name__ == '__main__':
    main()
