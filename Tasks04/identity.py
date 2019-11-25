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


def double_name(gender):
    """Generating a double name of the given type.
     :param gender: String
     :return: String
     """
    # gender sets whether the generated double name is male, female or
    # a family name
    if gender == "male":
        return double_name_male()
    elif gender == "female":
        return double_name_female()
    elif gender == "family":
        return double_name_last()


def double_name_male():
    """Generating a double male name.
    :return: String
    """
    while True:
        # We generate two random male names
        first_name = male_name()
        second_name = male_name()

        # The names are not allowed to be the same, therefore we need to
        # make sure that they aren't.
        if first_name == second_name:
            continue

        # If they are different, we connect them with a -
        else:
            new_name = first_name + "-" + second_name
            return new_name


def double_name_female():
    """Generating a double female name.
    :return: String
    """
    while True:
        # We generate two random female names
        first_name = female_name()
        second_name = female_name()

        # The names are not allowed to be the same, therefore we need to
        # make sure that they aren't.
        if first_name == second_name:
            continue

        # If they are different, we connect them with a -
        else:
            new_name = first_name + "-" + second_name
            return new_name


def double_name_last():
    """Generating a double last name.
    :return: String
    """
    while True:
        # We generate two random last names
        first_name = last_name()
        second_name = last_name()

        # The names are not allowed to be the same, therefore we need to
        # make sure that they aren't.
        if first_name == second_name:
            continue

        # If they are different, we connect them with a -
        else:
            new_name = first_name + "-" + second_name
            return new_name


def main():
    """Running the program if run as main"""
    pass


if __name__ == '__main__':
    main()
