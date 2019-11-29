"""This program generates random identities consisting of a name and an
address.
"""

__author__ = "7146127, Theobald, 6956404, Stadler"
__email__ = "s7223152@cs.uni-frankfurt.de, s0706782@rz.uni-frankfurt.de"

import random as dice
import names


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
    doctor = dice.randint(1, 1000)  # Different for men and women
    # Gender distribution is 50/50 (with only 2 genders),
    # 10% have a double first name,
    # 15 % have a double last name and
    # 1% are doctors.
    name = ""
    prefix = ""

    if gender <= 50 and double_first <= 10:
        name = double_name("male")
        if name.split("-")[0] in names.man and name.split("-")[1] in names.man:
            prefix = "Herr "
    elif gender <= 50:
        name = male_name()
        if name in names.woman:
            prefix = "Herr "
    elif gender > 50 and double_first <= 10:
        name = double_name("female")
        if name.split("-")[0] in names.man and name.split("-")[1] in names.man:
            prefix = "Frau "
    elif gender > 50:
        name = female_name()
        if name in names.man:
            prefix = "Frau "

    # Now we add a last name or even a double last name
    if 40 <= double_last < 55:
        name += " " + double_name("family")
    else:
        name += " " + last_name()

    # Last but not least we check if the person is a doctor
    if (gender <= 50 and doctor <= 11):
        name = "Dr. " + name
    elif (gender > 50 and doctor <= 9):
        name = "Dr. " + name

    # We use the prefix to get a clear identifier in case the name can
    # be used for both genders
#    if gender <= 50 and name.split()[-2] in names.woman:
#        prefix = "Herr "
#    elif gender > 50 and name.split()[-2] in names.man:
#       prefix = "Frau "
    # If the prefix isn't empty, we add it to the name
    if prefix:
        name = prefix + name
    return name


def test_name(name):
    """Testing a name for its attributes.
    :param name: String
    :return: list
    """
    # We save the results in a list
    result = []
    # To work with the name, we remove the address and then
    # split it by its blanks
    name = name.split(",")[0]
    name = name.split()
    # First, we check whether the fictional person is a doctor or not
    doctor = 0
    if "Dr." in name:
        doctor = 1

    result = [doctor]
    # Next we look at whether the person has a double first name
    if "-" in name[-2]:
        result.append(1)
    else:
        result.append(0)

    # Next we check if the person hat a double last name.
    if "-" in name[-1]:
        result.append(1)
    else:
        result.append(0)

    # Next we check whether the person is male or female.
    first_name = name[-2]
    if result[1] == 1:
        first_name = (first_name.split("-"))[-2]
    if (first_name in names.woman and "Herr" not in name) or "Frau" in name:
        result.append("female")
    elif (first_name in names.man and "Frau" not in name) or "Herr" in name:
        result.append("male")
    return result


def statistical_test_name(sample_size):
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
    for i in sample:
        result = test_name(i)
        doctor += result[0]
        double_first += result[1]
        double_last += result[2]
        if result[3] == "male":
            male += 1
        elif result[3] == "female":
            female += 1

    # Now we convert the raw numbers to percentage values by dividing it
    # by the sample size, multiplying it by 10000 to shorten the value
    # to two digits and then dividing by 100
    doctor = (((doctor / sample_size) * 10000) // 1) / 100
    double_first = (((double_first / sample_size) * 10000) // 1) / 100
    double_last = (((double_last / sample_size) * 10000) // 1) / 100
    male = (((male / sample_size) * 10000) // 1) / 100
    female = (((female / sample_size) * 10000) // 1) / 100

    # At the end we print each probability
    print(doctor, "% are doctors.", sep="")
    print(double_first, "% have a double first name.", sep="")
    print(double_last, "% have a double last name.", sep="")
    print(male, "% are male.", sep="")
    print(female, "% are female.", sep="")


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


def generate_sorted(sample_size):
    """Generating a sorted list.
    :param sample_size: int
    :return: list
    """
    sample = []
    for i in range(sample_size):
        sample.append(identity())

    # We sort our sample. To do this we sort by the first name first.
    # When we then sort by the last name, the first sorting won't
    # be entirely destroyed
    sample = sorted(sample, key=lambda x: x.split()[0])
    sample = sorted(sample, key=lambda x: x.split()[1])
    # Then we print our sample
    for i in sample:
        print(i)

    return sample


def statistical_test(sample_size):
    """Checking the statistics of the final program.
    :param sample_size: int
    :return: None
    """
    # We create our sample by the sample size
    sample = []
    for i in range(sample_size):
        sample.append(identity())

    # Now we test if our implementations fit the requirements. Starting
    # with the names.
    doctor, double_first, double_last, male, female, unclear = (0,) * 6
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

    # And then comes the address
    haupt, schul, garten, dorf, bahnhof, wiesen, berg, kirch, wald, ring_prefix, custom, \
    straße, weg, allee, ring_suffix, platz, number_four_digits, number_three_digits, \
    number_less_digits \
        = \
        (0,) * 19
    for i in sample:
        result = test_address(i)
        # Now we add the result to the respective variables
        haupt += result[0]
        schul += result[1]
        garten += result[2]
        dorf += result[3]
        bahnhof += result[4]
        wiesen += result[5]
        berg += result[6]
        kirch += result[7]
        wald += result[8]
        ring_prefix += result[9]
        custom += result[10]
        straße += result[11]
        weg += result[12]
        allee += result[13]
        ring_suffix += result[14]
        platz += result[15]
        number_four_digits += result[16]
        number_three_digits += result[17]
        number_less_digits += result[18]

    # And now we form every result into a percentage value and print it.
    doctor = '{:.2%}'.format(doctor / sample_size)
    double_first = '{:.2%}'.format(double_first / sample_size)
    double_last = '{:.2%}'.format(double_last / sample_size)
    male = '{:.2%}'.format(male / sample_size)
    female = '{:.2%}'.format(female / sample_size)
    haupt = '{:.2%}'.format(haupt / sample_size)
    schul = '{:.2%}'.format(schul / sample_size)
    garten = '{:.2%}'.format(garten / sample_size)
    dorf = '{:.2%}'.format(dorf / sample_size)
    bahnhof = '{:.2%}'.format(bahnhof / sample_size)
    wiesen = '{:.2%}'.format(wiesen / sample_size)
    berg = '{:.2%}'.format(berg / sample_size)
    kirch = '{:.2%}'.format(kirch / sample_size)
    wald = '{:.2%}'.format(wald / sample_size)
    ring_prefix = '{:.2%}'.format(ring_prefix / sample_size)
    custom = '{:.2%}'.format(custom / sample_size)
    straße = '{:.2%}'.format(straße / sample_size)
    weg = '{:.2%}'.format(weg / sample_size)
    allee = '{:.2%}'.format(allee / sample_size)
    ring_suffix = '{:.2%}'.format(ring_suffix / sample_size)
    platz = '{:.2%}'.format(platz / sample_size)
    number_four_digits = '{:.2%}'.format(number_four_digits / sample_size)
    number_three_digits = '{:.2%}'.format(number_three_digits / sample_size)
    number_less_digits = '{:.2%}'.format(number_less_digits / sample_size)

    # Last but not least we print the results.
    print(doctor, "are doctors. The value should be around 1%.")
    print(double_first, "have a double first name. The value should be around 10%.")
    print(double_last, "have a double last name. The value should be around 15%.")
    print(male, "are male. The value should be around 50%.")
    print(female, "are female. The value should be around 50%.")
    print(haupt, "live in a 'Haupt*'. The value should be around 10%.")
    print(schul, "live in a 'Schul*'. The value should be around 8%.")
    print(garten, "live in a 'Garten*'. The value should be around 7%.")
    print(dorf, "live in a 'Dorf*'. The value should be around 7%.")
    print(bahnhof, "live in a 'Bahnhof*'. The value should be around 7%.")
    print(wiesen, "live in a 'Wiesen*'. The value should be around 7%.")
    print(berg, "live in a 'Berg*'. The value should be around 6%.")
    print(kirch, "live in a 'Kirch*'. The value should be around 4%.")
    print(wald, "live in a 'Wald*'. The value should be around 4%.")
    print(ring_prefix, "live in a 'Ring*'. The value should be around 4%.")
    print(custom, "live in something named nothing of the above. The value should be around 36%.")
    print(straße, "live in a '*straße'. The value should be around 78%.")
    print(weg, "live in a '*weg'. The value should be around 18%.")
    print(allee, "live in a '*allee'. The value should be around 2%.")
    print(ring_suffix, "live in a '*ring'. The value should be around 1%.")
    print(platz, "live in a '*platz'. The value should be around 1%.")
    print(number_four_digits, "have a four digit house number. The value should be around 1%.")
    print(number_three_digits, "have a three digit house number. The value should be around 10%.")
    print(number_less_digits, "have a one or two digit house number. The value should be around "
                              "89%.")
    return sample


def test_address(residence):
    """Testing the address on its attributes.
    :param residence: String
    :return: list
    """
    # We start by creating our result list
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Then we split our given string so we only have the address left
    residence = residence.split(", ")[1]

    # First we check for the prefix and increase the according value
    if "Haupt" in residence:
        result[0] = 1
    elif "Schul" in residence:
        result[1] = 1
    elif "Garten" in residence:
        result[2] = 1
    elif "Dorf" in residence:
        result[3] = 1
    elif "Bahnhof" in residence:
        result[4] = 1
    elif "Wiesen" in residence:
        result[5] = 1
    elif "Berg" in residence and residence[4] in ("s", "w", "a", "r", "p"):
        result[6] = 1
    elif "Kirch" in residence:
        result[7] = 1
    elif "Wald" in residence:
        result[8] = 1
    elif "Ring" == residence[0:4]:
        result[9] = 1
    else:
        result[10] = 1

    # Now we check the suffix
    if "straße" in residence or "Straße" in residence:
        result[11] = 1
    elif "Weg" in residence or "weg" in residence:
        result[12] = 1
    elif "Allee" in residence or "allee" in residence:
        result[13] = 1
    elif "platz" in residence or "platz" in residence:
        result[15] = 1
    else:
        result[14] = 1

    # And now we check the number
    number = int(residence.split()[-1])
    if number > 999:
        result[16] = 1
    elif number > 99:
        result[17] = 1
    else:
        result[18] = 1

    return result


# main function to test part 1 (implementation of basic name generation)
# def main():
#    """Running the program if run as main"""
#    print("male first names:")
#    for i in range (50):
#        print(male_name())
#    print("\nfemale first names:")
#    for i in range (50):
#        print(female_name())
#    print("\nlast names:")
#    for i in range (50):
#        print(last_name())

# main function to test part 2 (generating full names)
# def main():
#    """Running the program if run as main"""
#    for i in range(100):
#        print(full_name())

# main function to test part 3 (statistical test)
# def main():
#    """Running the program if run as main"""
#    for i in range(1000):
#        print(full_name())
#    statistical_test_name(1000)

# main function to test part 4 (full identity generation)
# def main():
#    """Running the program if run as main"""
#    for i in range(100):
#        print(identity())

# main function to test part 5 (final statistical research)
def main():
    """Running the program if run as main"""
    statistical_test(50000)
#    generate_sorted(1000)


if __name__ == '__main__':
    main()
