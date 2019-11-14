"""Getting two integers and doing a bunch of things with them."""

__author__ = "7146127, Theobald"


def average(first_number, second_number):
    """Returning the average of two integers and printing the average and the
    type of the average.
    :param first_number: int
    :param second_number: int
    :return: int or float
    """
    avg = (int(first_number) + int(second_number)) / 2

    # If the average is an integer, we can convert it to one
    if avg // 1 == avg / 1:
        avg = int(avg)
    print(avg, type(avg))
    return avg


def first_last_digit(avg):
    """Printing the first and last digit of the average and returning its
    length.
    :param avg: int or float
    :return: int
    """

    # If the average is negative (starting with a minus), we have to skip that to get the first
    # digit
    if avg < 0:
        avg = str(avg)
        print(avg[1], avg[-1], sep="")
    else:
        avg = str(avg)
        print(avg[0], avg[-1], sep="")
    return len(avg)


def reverse(avg):
    """Reversing the average.
    :param avg: int or float
    :return: string
    """
    avg = str(avg)
    avg_reversed = ""

    # We iterate through all of the string and reverse it by attaching the [-i-1] element to
    # the new string
    for i in range(len(avg)):
        avg_reversed += avg[-i - 1]
    return avg_reversed


def main():
    """Starting the program"""
    # We need to make sure that we get valid inputs
    while True:
        first = input("Please enter the first integer: ")
        try:
            first = int(first)
        except ValueError:
            continue
        break

    # The same goes for the second integer
    while True:
        second = input("Please enter the second integer: ")
        try:
            second = int(second)
            break
        except ValueError:
            continue

    # Now we can start working with that stuff
    avg = average(first, second)
    # noinspection PyTypeChecker
    first_last_digit(avg)
    print(avg, "is reversed", reverse(avg))


if __name__ == '__main__':
    main()

# Test cases:
# 10, 5 : "7.5 <class 'float'>", "75", "7.5 is reversed 5.7"
# -1234, -765 : "-999.5 <class 'float'>", "95", "-999.5 is reversed 5.999-"
# lol : "Please enter the first integer: "
# 870965437895424892631548654526437, 26954786387265987436278564873265876432 :
# "13477828676351940767776228213878947840 <class 'int'>", "10",
# "13477828676351940767776228213878947840 is reversed 04874987831282267776704915367682877431"
