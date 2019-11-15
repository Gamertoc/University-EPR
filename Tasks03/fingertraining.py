"""This program takes written numbers as input and converts them to integers."""

__author__ = "7146127, Theobald"


def conversion(written):
    """This function takes written numbers and converts them to their respective integers."""

    # I use a dictionary to convert the written numbers to actual numbers
    written_numeric = {
        "null": 0,
        "zero": 0,
        "eins": 1,
        "one": 1,
        "zwei": 2,
        "two": 2,
        "drei": 3,
        "three": 3,
        "vier": 4,
        "four": 4,
        "five": 5,
        "fünf": 5,
        "sechs": 6,
        "six": 6,
        "sieben": 7,
        "seven": 7,
        "acht": 8,
        "eight": 8,
        "neun": 9,
        "nine": 9,
    }

    # By splitting the string we can get each value.
    convert = written.split(",")

    # Then we can iterate through each value and add them to the string.
    numeric = ""
    for i in convert:
        # But first, let's check if they are even valid values. If they aren't, we just ignore
        # them. We convert the whole string to lowercase characters, in case some uppercase got
        # mixed in.
        if str(written_numeric.get(i.lower())) == "None":
            continue
        numeric += str(written_numeric.get(i.lower()))

    print(numeric)


def main():
    """Running the program at the start."""
    numbers = input('Please enter written numbers (lowercase, german or english, separated by '
                    'commata without blanks): ')
    conversion(numbers)


if __name__ == '__main__':
    main()

# TfTC (Time for test cases):
# neun,five,eight,seven,zero,null : 958700
# eins,AcHt,SIEbEn : 187
# neun,NOOOOOOOB1054656043,x,zero : 90
#  neun,eins, acht,seven : 917  (This occurs because you are not allowed to use whitespaces
