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

    if 40 <= double_last < 55:
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

    # At the end we print each probability
    print(doctor, "% are doctors.", sep="")
    print(double_first, "% have a double first name.", sep="")
    print(double_last, "% have a double last name.", sep="")
    print(male, "% are male.", sep="")
    print(female, "% are female.", sep="")
    print(unclear, "% have an unclear gender due to some names being suitable for both "
                   "genders.", sep="")


def address():
    """Generating a random street name and house number.
    :return: String
    """
    # We start with generating the street name. For this we choose
    # between the most common prefixes and our own prefixes
    prefix = dice.randint(1, 100)
    if prefix <= 10:  # 10%
        prefix = "Haupt"
    elif prefix <= 18:  # 8%
        prefix = "Schul"
    elif prefix <= 25:  # 7%
        prefix = "Garten"
    elif prefix <= 32:  # 7%
        prefix = "Dorf"
    elif prefix <= 39:  # 7%
        prefix = "Bahnhof"
    elif prefix <= 46:  # 7%
        prefix = "Wiesen"
    elif prefix <= 52:  # 6%
        prefix = "Berg"
    elif prefix <= 56:  # 4%
        prefix = "Kirch"
    elif prefix <= 60:  # 4%
        prefix = "Wald"
    elif prefix <= 64:  # 4%
        prefix = "Ring"
    else:
        prefix = dice.choice(names.prefix)

    # Now we can add the suffix
    suffix = dice.randint(1, 100)
    if suffix <= 78:
        suffix = "straße"
    elif suffix <= 96:
        suffix = "weg"
    elif suffix <= 98:
        suffix = "allee"
    elif suffix == 99:
        suffix = "ring"
    elif suffix == 100:
        suffix = "platz"

    # When we have a city name as prefix, we need to capitalize the
    # suffix since it will be two words
    if prefix[-1] == " ":
        suffix = suffix.capitalize()

    # Now we can add them together
    street = prefix + suffix

    # We need a house number as well. In Germany most numbers have
    # between one and four digits, so we will use this as base. Lower
    # numbers are more common, so we'll give it a 10% probability of
    # using 3 digits and 1% of using 4 digits
    digits = dice.randint(1, 100)
    if digits == 100:
        house_number = str(dice.randint(1000, 9999))
    elif digits >= 90:
        house_number = str(dice.randint(100, 999))
    else:
        house_number = str(dice.randint(1, 99))
    address_full = street + " " + house_number
    return address_full


def identity():
    """Generating a full identity with both name and address.
    :return: String
    """
    # We generate a name, an address, add them together and return that
    name = full_name()
    place_of_residence = address()
    new_identity = name + ", " + place_of_residence
    return new_identity


# main function to test part 1 (implementation of basic name generation)
# def main():
#    """Running the program if run as main"""
#    for i in range (50):
#       print(male_name()
#    for i in range (50):
#       print(female_name()
#    for i in range (50):
#       print(last_name())

# main function to test part 2 (generating full names)
# def main():
#    """Running the program if run as main"""
#    for i in range(100):
#        print(full_name())

# main function to test part 3 (statistical test)
# def main():
#    """Running the program if run as main"""
#    statistical_test(1000)

# main function to test part 4 (full identity generation)
def main():
    """Running the program if run as main"""
    for i in range(100):
        print(identity())


if __name__ == '__main__':
    main()
