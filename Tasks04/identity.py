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


def full_name():
    """Generating a full name (including Dr.).
    :return: String
    """
    gender = dice.randint(1, 100)  # Over 50 is male, under 50 is female
    double_first = dice.randint(1, 100)  # Over 10 no
    double_last = dice.randint(1, 100)  # Only between 40 and 55
    doctor = dice.randint(1, 100)  # Only if 100
    # Gender distribution is 50/50 (with only 2 genders),
    # 10% have a double first name,
    # 15 % have a double last name and
    # 1% are doctors.
    name = ""
    if gender <= 50 and double_first <= 10:
        name = double_name("male")
    elif gender <= 50:
        name = male_name()
    elif double_first <= 10:
        name = double_name("female")
    else:
        name = female_name()

    if 40 <= double_last <= 55:
        name += " " + double_name("family")
    else:
        name += " " + last_name()

    if doctor == 100:
        name = "Dr. " + name

    return name


def test_name(name):
    """Testing a name for its attributes.
    :param name: String
    :return: list
    """
    # We save the results in a list
    result = []
    # To work with the name, we split it by its blanks
    name = name.split()

    # First, we check whether the fictional person is a doctor or not
    doctor = 0
    if name[0] == "Dr.":
        doctor = 1

    result = [doctor]

    # Next we look at whether the person has a double first name
    if "-" in name[doctor]:
        result.append(1)
    else:
        result.append(0)

    # Next we check if the person hat a double last name.
    if "-" in name[doctor + 1]:
        result.append(1)
    else:
        result.append(0)

    # Next we check whether the person is male or female.
    first_name = name[doctor]
    if result[1] == 1:
        first_name = (first_name.split("-"))[0]
    if first_name in names.woman and first_name in names.man:
        result.append("unclear")
    elif first_name in names.woman:
        result.append("female")
    elif first_name in names.man:
        result.append("male")

    return result


def statistical_test(sample_size):
    """We can run a statistical test to test whether our implemented
    random functions get us good values or not.
    :param sample_size: int
    :return: None
    """
    # First we create our sample
    sample = []
    for i in range(sample_size):
        sample.append(full_name())

    # Then we test each name and add the numbers to the according values
    doctor = 0
    double_first = 0
    double_last = 0
    male = 0
    female = 0
    unclear = 0
    for i in sample:
        result = test_name(i)
        doctor += result[0]
        double_first += result[1]
        double_last += result[2]
        if result[3] == "male":
            male += 1
        elif result[3] == "female":
            female += 1
        elif result[3] == "unclear":
            unclear += 1

    # Now we convert the raw numbers to percentage values by dividing it
    # by the sample size, multiplying it by 10000 to shorten the value
    # to two digits and then dividing by 100
    doctor = (((doctor / sample_size) * 10000) // 1) / 100
    double_first = (((double_first / sample_size) * 10000) // 1) / 100
    double_last = (((double_last / sample_size) * 10000) // 1) / 100
    male = (((male / sample_size) * 10000) // 1) / 100
    female = (((female / sample_size) * 10000) // 1) / 100
    unclear = (((unclear / sample_size) * 10000) // 1) / 100

    print(doctor, "% are doctors.", sep="")
    print(double_first, "% have a double first name.", sep="")
    print(double_last, "% have a double last name.", sep="")
    print(male, "% are male.", sep="")
    print(female, "% are female.", sep="")
    print(unclear, "% have an unclear gender due to some names being suitable for both "
                   "genders.", sep="")


def main():
    """Running the program if run as main"""
    statistical_test(1000)
    double = 0


if __name__ == '__main__':
    main()
