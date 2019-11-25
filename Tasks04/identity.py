"""This program generates random identities consisting of a name and an
address.
"""

__author__ = "7146127, Theobald"
__email__ = "s7223152@cs.uni-frankfurt.de"

import random as dice
from Tasks04 import names


def male_name():
    """Generating a male first name.
    :return: String
    """
    return dice.choice(names.man)


def female_name():
    """Generating a female first name.
    :return: String
    """
    return dice.choice(names.woman)


def last_name():
    """Generating a family name.
    :return: String
    """
    return dice.choice(names.lastname)


def main():
    """Running the program if run as main"""
    pass


if __name__ == '__main__':
    main()
