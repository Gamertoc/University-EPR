"""This module contains helper fuctions for the user interface."""

__author__ = "7146127, Theobald, 6956404, Stadler"
__email__ = "s7223152@cs.uni-frankfurt.de, s0706782@rz.uni-frankfurt.de"


def visual_dice(first_dice, second_dice):
    """Prints the tossed number as kind of a dice.
    :param first_dice: int
    :param second_dice: int
    :return: None
    """
    first_line = ""
    second_line = ""
    third_line = ""
    for i in first_dice, second_dice:
        if i == 1:
            first_line += "     "
            second_line += "  O  "
            third_line += "     "
        elif i == 2:
            first_line += "    O"
            second_line += "     "
            third_line += "O    "
        elif i == 3:
            first_line += "    O"
            second_line += "  O  "
            third_line += "O    "
        elif i == 4:
            first_line += "O   O"
            second_line += "     "
            third_line += "O   O"
        elif i == 5:
            first_line += "O   O"
            second_line += "  O  "
            third_line += "O   O"
        else:
            first_line += "O O O"
            second_line += "     "
            third_line += "O O O"
        first_line += "        "
        second_line += "        "
        third_line += "        "

    print(first_line, "\n", second_line, "\n", third_line, sep="")


def input_number(prompt="Please enter a number: "):
    """Read a number from the user."""

    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("You have to type a valid integer and press enter.")


def input_valid_number(prompt="Please enter a valid number: "):
    """Read a valid number from the user."""

    while True:
        number = input_number(prompt)

        # Checks, whether the number is in the valid range.
        if 11 <= number <= 66:
            return number
        else:
            print("A valid number is bigger than 10 and smaller than 67.")


def input_yes_no(prompt="Write \"yes\" or \"no\": "):
    """Read only yes or no."""

    text = input(prompt)
    while text != "yes" and text != "no":
        text = input(prompt)

    return text


def print_points(player):
    """Print the points of the given player list."""

    print(player[0], "has (now) a total of", player[1], "points.")
