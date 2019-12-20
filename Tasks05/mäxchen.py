# -*- coding: utf-8 -*-
"""This is the main module and entry point of the game "Mäxchen"."""

# noinspection SpellCheckingInspection
__author__ = "7146127, Theobald, 6956404, Stadler"
__email__ = "s7223152@cs.uni-frankfurt.de, s0706782@rz.uni-frankfurt.de"

import random as dice
import time
import ui_help


# TO DO:
# Testing the bot
#   -> bots seem to run nicely

# Unicode still doesnt work :( -> Commented
# The Deletion with Flush() still doesnt work in the shell. But we can say "Don't use shell"


def roll_dices(order_numbers):
    """Create a random valid number."""

    first_digit = dice.randint(1, 6)
    second_digit = dice.randint(1, 6)

    if order_numbers:
        return max(first_digit, second_digit) * 10 + min(first_digit, second_digit)
    else:
        return first_digit * 10 + second_digit


def new_better_than_old(new_number, old_number, settings_all):
    """Value two numbers.
    The standard number order is:
    42 > 21 > 66 > 55 > ... > 11 > others
    (others in the normal ">" order)
    
    """

    # Stretching the numbers so we can easily compare them.
    if new_number == settings_all["Hamburger"]:
        new_number *= 1000
    elif new_number == settings_all["Mäxchen"]:
        new_number *= 100
    elif new_number % 10 == new_number // 10:
        new_number *= 10

    if old_number == settings_all["Hamburger"]:
        old_number *= 1000
    elif old_number == settings_all["Mäxchen"]:
        old_number *= 100
    elif old_number % 10 == old_number // 10:
        old_number *= 10

    return new_number > old_number


def points_worth(number, settings_all):
    """Calculate the points to subtract from the players account.
    :param number: int
    :param settings_all: dictionary
    :return: int
    """
    if number == settings_all["Hamburger"]:
        return settings_all["point_loss_hamburger"]
    elif number == settings_all["Mäxchen"]:
        return settings_all["point_loss_mäxchen"]
    else:
        return settings_all["point_loss_normal"]


def play(players, settings_all):
    """To play the base game.
    :param players: list
    :param settings_all: dictionary
    :return: String
    """
    game_over = False
    last_tossed_number = 0
    player_count = len(players)

    finished_players = []

    # This is the index of the player, who does the next move.
    # It is the list index, not the number.
    turn_index = 0

    while not game_over:

        print("\nIt is " + players[turn_index][0] + "'s turn.")

        # Cheaters have a 50% chance of their cheated number.
        if players[turn_index][2] == "HTTB" and dice.randint(0, 1) == 1:
            tossed_number = settings_all["Hamburger"]
        elif players[turn_index][2] == "MM" and dice.randint(0, 1) == 1:
            tossed_number = settings_all["Mäxchen"]
        else:
            # A new number gets tossed.
            order_numbers = settings_all["order_digits"]
            tossed_number = roll_dices(order_numbers)

        # A bot doesn't need to let his number appear on screen
        if players[turn_index][4]:
            print(players[turn_index][0], "is a bot and therefore doesn't need his number to "
                                          "appear on screen.")
        else:
            # This construction shows you your number for 5 seconds after pressing enter.
            input("Press enter to show your number")
            for i in range(6):
                print(
                    "\rYou tossed a ", str(tossed_number), " which will vanish in ", str(5 - i),
                    flush=True, sep="", end="")
                time.sleep(1)

        print("\rThe number from the last turn was", last_tossed_number, "   ")

        # If the player is a bot, it'll generate a number based on the given strategy.
        if players[turn_index][4]:
            while True:
                typed_number = bot_lie(settings_all, tossed_number, last_tossed_number)
                if new_better_than_old(typed_number, last_tossed_number, settings_all):
                    break
            print(players[turn_index][0], "typed", typed_number)
        else:
            # This makes sure that a valid number is entered.
            while True:
                typed_number = ui_help.input_valid_number(
                    "Please enter the number you tossed (It's "
                    "allowed to lie). ",
                    settings_all["order_digits"])

                if not new_better_than_old(typed_number, last_tossed_number, settings_all):
                    print(
                        "Of course the number has to be bigger than the old one.\nRead the rules "
                        "and try again.")
                else:
                    break

        next_turn_index = (player_count + turn_index + settings_all["play_order"]) % player_count

        if players[next_turn_index][4]:
            believe = bot_believe(settings_all, typed_number)
            if believe == "yes":
                print(players[next_turn_index][0], "believes that.")
            else:
                print(players[next_turn_index][0], "does not believe that.")
        else:
            believe = ui_help.input_yes_no(players[next_turn_index][0] +
                                           " now decides. Do you believe that he tossed that? Write "
                                           "\"yes\" or \"no\": ")

        # When not believing, check the numbers.
        if believe == "no":
            print("\nThese were the dices:")
            ui_help.visual_dice(tossed_number // 10, tossed_number % 10)
            print("Tossed number:", tossed_number, "Typed number:", typed_number, "\n")
            if new_better_than_old(typed_number, tossed_number, settings_all):
                if players[turn_index][2] != "GK":
                    print("Oops, you were caught red-handed.")
                    print("Try to lie better next time", u"\U0001F609")
                    players[turn_index][1] -= points_worth(tossed_number, settings_all)
                    ui_help.print_points(players[turn_index])
                else:
                    print("Due to an internal crash, the profile of " + players[turn_index][0]
                          + " was locked. He/She loses no points this round.")
            elif typed_number == tossed_number:
                if players[next_turn_index][2] != "GK":
                    print("No lie, no points for", players[next_turn_index][0])
                    players[next_turn_index][1] -= points_worth(typed_number, settings_all)
                    ui_help.print_points(players[next_turn_index])
                else:
                    print("ERROR, cannot remove points from such a nice player.")
                    ui_help.print_points(players[next_turn_index])
            else:
                print("It was a trap and you ran into it, " + players[next_turn_index][0] + "!")
                if players[next_turn_index][2] != "GK":
                    players[next_turn_index][1] -= points_worth(typed_number, settings_all)
                    ui_help.print_points(players[next_turn_index])
                else:
                    print("But no problem. Shit happens.")

            # Reversing the play order when those options are activated and the specific number
            # is hit
            if (settings_all["reverse_mäxchen"] and tossed_number == settings_all["Mäxchen"]) or \
                    (settings_all["reverse_hamburger"] and tossed_number == settings_all[
                        "Hamburger"]):
                settings_all["play_order"] *= -1
                print("Turn order got reversed. Be prepared!")

            # Reset the number for the next turn
            typed_number = 0
            for i in players:
                i[3].append(i[1])

        # Checking if any player has less than 1 point
        for i in players:
            if i[1] <= 0:
                print("\n" + i[0], "has", i[1], "points and is therefore out of the game! "
                                                "Better luck next time.")
                finished_players.append(i)
                players.remove(i)

        # Check for win
        if len(players) == 1:
            finished_players.append(players[0])
            return finished_players

        # After that we refresh the player count
        player_count = len(players)

        # Calculates the new player turn index.
        turn_index = (player_count + turn_index + settings_all["play_order"]) % player_count
        last_tossed_number = typed_number

        # Restarting the game at 0 when the maximum value is reached.
        if typed_number == settings_all["Hamburger"]:
            print("Maximum value reached. Restarting the game...")
            last_tossed_number = 0
            continue


def initialize(settings_all):
    """This function will initialize the game, starting with the chosen
     number of players.
     """
    player_count = ui_help.input_number("How many players want to play?\n")

    # Check whether the player count is valid. Is has to be 2 or larger (for now)
    if player_count <= 0:
        print("Ok, you do not have to...")
        return
    elif player_count == 1:
        print("Stop the jokes...")
        exit()
    print("Welcome to the game!")
    print("Please enter your names. It is your responsibility to pick unique names.")

    # The player list contains 4-element-lists: [<name>, <points>, <cheat>, <points_table>].
    players = []

    # Each player can enter his name
    for i in range(player_count):
        name = input("\nPlayer " + str(i + 1) + ": Please enter your name:\n")
        cheat = ""
        bot = False

        # By entering specific phrases in front of the name, one can activate cheat codes
        if name[:14] == "HamToTheBurger":
            cheat = "HTTB"
            name = name[14:]
        elif name[:7] == "MegaMax":
            cheat = "MM"
            name = name[7:]
        elif name[:7] == "GodKing":
            cheat = "GK"
            name = name[7:]

        # By entering a specific phrase at the end of the name, one can make a player be
        # controlled by a bot.
        if name[-4:] == "#207":
            bot = True
            name = name[:-4]

        players.append([name, settings_all["points_to_start"], cheat, [], bot])

    dice.shuffle(players)
    print("\nThe play order is:")
    for i in players:
        print(i[0])
    
    return play(players, settings_all)


def bot_lie(settings_all, tossed_number, last_tossed_number):
    """This function decides which number the bot enters and therefore if he lies or not. The
    bot has 3 strategies to choose from: Safe, aggressive and normal. The bot settings can be
    set by changing the settings.
    :param settings_all: dictionary
    :param tossed_number: int
    :param last_tossed_number: int
    :return: int
    """
    strategy = dice.randint(1, 100)

    # If the bot is set to safe, it will choose that strat with 80%, 15% will be normal and 5%
    # will be aggressive.
    # If it is set to normal, it will be 75% normal, 15% safe and 10% aggressive.
    # If it is set to aggressive, it will be 80% aggressive and 20% normal.
    if (settings_all["bot_lie"] == "safe" and strategy <= 80) or \
            (settings_all["bot_lie"] == "normal" and strategy <= 15) or \
            (settings_all["bot_lie"] == "aggressive" and strategy <= 5):
        return safe_tell(settings_all, tossed_number, last_tossed_number)

    elif (settings_all["bot_lie"] == "safe" and 80 < strategy <= 95) or \
            (settings_all["bot_lie"] == "normal" and 15 < strategy <= 90) or \
            (settings_all["bot_lie"] == "aggressive" and strategy <= 10):
        return normal_tell(settings_all, last_tossed_number)

    else:
        return aggressive_tell(settings_all, tossed_number, last_tossed_number)


def safe_tell(settings_all, tossed_number, last_tossed_number):
    """Generating a number based on the safe strat. This means that that 90% of the time the
    number will be equal or lower to the tossed number.
    :param settings_all: dictionary
    :param tossed_number: int
    :param last_tossed_number: int
    :return: int
    """
    strat = str(time.time()).split(".")[-1]
    digit = dice.randint(1, len(strat))
    strat = int(strat[-digit])
    if not strat == 0:
        safe = True
    else:
        safe = False
    while True:
        new_number = roll_dices(settings_all["order_digits"])
        if new_better_than_old(new_number, last_tossed_number, settings_all):
            if (safe and not new_better_than_old(new_number, tossed_number, settings_all)) or \
                (not safe and (new_better_than_old(new_number, tossed_number, settings_all)
                               or new_number == tossed_number)):
                return new_number


def normal_tell(settings_all, last_tossed_number):
    """Generating a number based on the normal strat. This means that a random valid number is
    used by the bot.
    :param settings_all: dictionary
    :param last_tossed_number: int
    :return: int
    """
    # The only point of this construction is to make sure that the number can be used in game,
    # e.g. it is a number a human could have entered.
    while True:
        new_number = roll_dices(settings_all["order_digits"])
        if new_better_than_old(new_number, last_tossed_number, settings_all):
            return new_number


def aggressive_tell(settings_all, tossed_number, last_tossed_number):
    """Generating a number based on the aggressive strat. This means that 90% of the time the
    number is larger than the tossed one.
    :param settings_all: dictionary
    :param tossed_number: int
    :param last_tossed_number: int
    :return: int
    """
    strat = str(time.time()).split(".")[-1]
    digit = dice.randint(1, len(strat))
    strat = int(strat[-digit])
    if not strat == 0:
        aggressive = True
        if tossed_number == settings_all["Hamburger"]:
            return tossed_number
    else:
        aggressive = False
    while True:
        new_number = roll_dices(settings_all["order_digits"])
        if new_better_than_old(new_number, last_tossed_number, settings_all):
            if (aggressive and new_better_than_old(new_number, tossed_number, settings_all)) or \
                    (not aggressive and (
                            new_better_than_old(new_number, tossed_number, settings_all)
                            or new_number == tossed_number)):
                return new_number


def bot_believe(settings_all, typed_number):
    """This function generates a value whether the bot believes you or not.
    :param settings_all: dictionary
    :param typed_number: int
    :return: str
    """
    strategy = dice.randint(1, 100)
    # A naive bot will be 90% naive and 10% normal.
    # A normal bot will be 80% normal, 10% naive and 10% suspicious.
    # A suspicious bot will be 85% suspicious, 10% normal and 5% naive.

    if (settings_all["bot_believe"] == "naive" and strategy <= 90) or \
            (settings_all["bot_believe"] == "normal" and strategy <= 10):
        believe = naive_believer(settings_all, typed_number)

    elif (settings_all["bot_believe"] == "naive" and 90 < strategy) or \
            (settings_all["bot_believe"] == "normal" and 10 <= strategy < 90) or \
            (settings_all["bot_believe"] == "suspicious" and strategy <= 10):
        believe = normal_believer(settings_all, typed_number)

    else:
        believe = suspicious_believer(settings_all, typed_number)
    if believe:
        return "yes"
    else:
        return "no"


def naive_believer(settings_all, typed_number):
    """This function simulates a naive bot. Naive means that he will only get suspicious on very
    high numbers. If the number is below a certain point, he won't get suspicious at all
    :param settings_all: dictionary
    :param typed_number: int
    :return: bool"""
    while True:
        pivot = dice.randint(11, 66)
        # This construction makes sure that our turning point isn't a doubles or a Hamburger or
        # a Mäxchen
        if pivot not in (settings_all["Hamburger"], settings_all["Mäxchen"]) \
                and not pivot % 11 == pivot // 11:
            break

    believable = 0
    # If the number is below or equal to the turning point, the bot will just believe it.
    if new_better_than_old(pivot, typed_number, settings_all):
        return True

    # If the number isn't a Hamburger, the bot will use some statistics
    elif not typed_number == settings_all["Hamburger"]:
        for i in range(10000):
            number = roll_dices(settings_all["order_digits"])
            if number <= pivot or new_better_than_old(number, typed_number, settings_all) or \
                    number == typed_number:
                believable += 1
    else:
        # For a hamburger, we need another construction
        for i in range(10000):
            if roll_dices(settings_all["order_digits"]) == settings_all["Hamburger"]:
                believable += 1

    # The score is calculated by dividing the believable counter by 10,000, adding the
    # countervalue multiplied with the score itself, and stretching this by 10,000 to get better
    # usability
    score = (believable / 10000)
    score = (score + (1 - score) * score + (1 - score) * (1 - score) * score) * 10000
    if score >= dice.randint(1, 10000):
        return True
    else:
        return False


def normal_believer(settings_all, typed_number):
    """The normal believer uses statistics to tell whether he believes you or not. For that he
    generates a bunch of numbers """
    believable = 0
    # The normal method only works for non-Hamburger numbers because there are no numbers that
    # are better than a hamburger.
    if not typed_number == settings_all["Hamburger"]:
        for i in range(10000):
            number = roll_dices(settings_all["order_digits"])
            if new_better_than_old(number, typed_number, settings_all) or number == typed_number:
                believable += 1

    else:
        # For a hamburger we use this construction
        for i in range(10000):
            if roll_dices(settings_all["order_digits"]) == settings_all["Hamburger"]:
                believable += 1

    score = believable
    if dice.randint(1, 10000) <= score:
        return True
    else:
        return False


def suspicious_believer(settings_all, typed_number):
    """The normal believer uses statistics to tell whether he believes you or not. For that he
    generates a bunch of numbers """
    believable = 0
    # The normal method only works for non-Hamburger numbers because there are no numbers that
    # are better than a hamburger.
    if not typed_number == settings_all["Hamburger"]:
        for i in range(10000):
            if new_better_than_old(roll_dices(settings_all["order_digits"]), typed_number,
                                   settings_all):
                believable += 1

    else:
        # For a hamburger we use this construction
        for i in range(10000):
            if roll_dices(settings_all["order_digits"]) == settings_all["Hamburger"]:
                believable += 1

    score = believable / 10000
    score = (score / 3) * 10000
    if dice.randint(1, 10000) >= score:
        return True
    else:
        return False


def settings():
    """Adjusting the settings of the game.
    :return: dictionary
    """

    # This dictionary stores all the settings
    settings_all = {
        "Mäxchen": 21,
        "Hamburger": 42,
        "order_digits": True,  # If True, the larger digit will be the 1st digit every time
        "play_order": 1,
        "points_to_start": 10,
        "point_loss_normal": 1,
        "point_loss_mäxchen": 2,
        "point_loss_hamburger": 3,
        "reverse_mäxchen": True,
        "reverse_hamburger": True,
        "bot_lie": "aggressive",
        "bot_believe": "normal",
    }

    # This dictionary references each setting by a number
    reference = {
        1: "Mäxchen",
        2: "Hamburger",
        3: "order_digits",
        4: "play_order",
        5: "points_to_start",
        6: "point_loss_normal",
        7: "point_loss_mäxchen",
        8: "point_loss_hamburger",
        9: "reverse_mäxchen",
        10: "reverse_hamburger",
        11: "bot_lie",
        12: "bot_believe"
    }

    # This dictionary stores the explanation of each setting.
    help_game = {
        -1: "What do you need help with?\n0: What do I even do here?\n1 to 12: What that "
            "setting does.\nlist: List all settings.\nq to go back to the settings.",
        0: "To change a setting, simply type a number from 1 to 12 to change the according "
           "setting.\nType help to get an explanation of which number belongs to which "
           "setting.\nTo go directly to the game, type q.",
        1: "This is the value of Mäxchen. Standard: 21",
        2: "This is the value of the Hamburger. Standard: 42",
        3: "This sets whether the numbers of the dices are ordered or not (meaning that the "
           "larger digit will always be the first one). Standard: True",
        4: "This is the order of playing. 1 means normal, -1 means reversed. Standard: 1",
        5: "This is the number of points each player gets at the start. Standard: 10",
        6: "This is the number of points you lose on normal numbers. Standard: 1",
        7: "This is the number of points you lose on a Mäxchen. Standard: 2",
        8: "This is the number of points you lose on a Hamburger. Standard: 3",
        9: "This sets whether the playing order is reversed when a Mäxchen is revealed. "
           "Standard: True",
        10: "This sets whether the playing order is reversed when a Hamburger is revealed. "
            "Standard: True",
        11: "This sets the favorite strat of the bot regarding what it tells you what it rolled. "
            "There is a \"safe\" a \"normal\" and an \"aggressive\" strategy. Standard: "
            "aggressive",
        12: "This sets the favorite strat of the bot regarding whether he believes you what you "
            "rolled. There is a a \"naive\" a \"normal\" and a \"suspicious\" strategy. "
            "Standard: normal",
    }
    print(help_game[0])

    # Remove if not working!!!!!!!
    print("\033[91m{}\033[00m".format("\nPlease remember that you can seriously fuck up the "
                                      "settings to the point of making the game unplayable.\n"
                                      "This is entirely your responsibility and we recommend "
                                      "that you think about the impact on the game before "
                                      "changing any setting." + u"\U0001f621"))

    # The user can decide whether he wants to change some game settings or not.
    while True:
        choice = input("\nWhat do you want to do? ")
        if choice == "q":
            break

        # If you ask for help, you will receive help
        elif choice == "help":
            print(help_game[-1])
            while True:
                choice = input("\nNow what do you need help with? ")
                if choice == "q":
                    print("Going back to the settings.")
                    break
                elif choice == "list":
                    for i in help_game:
                        if not i <= 0:
                            print(i, ": ", help_game[i], sep="")
                else:
                    try:
                        choice = int(choice)
                        if choice in help_game:
                            print(help_game[choice])
                        else:
                            print("The setting you asked help for doesn't exist. Please choose "
                                  "something else.")
                    except ValueError:
                        print(help_game[-1])

        # If you don't need help, you can just start changing settings.
        else:
            try:
                choice = int(choice)
                if choice not in reference:
                    print("We don't have such a setting. Please choose something that we cover.")
                    continue
                else:
                    setting = settings_all[reference[choice]]
                    print(help_game[choice], "\nThe current value is", setting)

                    # Now that you see the setting, you can decide whether you still wanna
                    # change it.
                    if input("Type y if you want to change this. ") == "y":

                        # If the setting is a boolean, we just flip the value.
                        if type(setting) is bool:
                            settings_all[reference[choice]] = not settings_all[reference[choice]]
                            print("The new value is", settings_all[reference[choice]])

                        # If the setting is a number, we need to get a new number as input.
                        elif type(setting) is int:
                            while True:
                                try:
                                    settings_all[reference[choice]] = int(input("Please enter "
                                                                                "the new value of "
                                                                                "this setting. "))
                                    print("The new value is", settings_all[reference[choice]])
                                    break
                                except ValueError:
                                    print("That's not a number. Try again.")

                        # If the setting is a string (only on setting 11), we have to take that
                        # into account
                        elif type(setting) is str:
                            while True:
                                settings_all[reference[choice]] = input("Please enter the new "
                                                                        "value of this setting. ")
                                if (settings_all[reference[choice]] in ("aggressive", "normal",
                                                                        "safe") and settings_all[
                                        reference[choice]] == "bot_lie") or (
                                        settings_all[reference[choice]] in ("suspicious", "normal",
                                                                            "naive") and
                                        settings_all[
                                            reference[choice]] == "bot_believe"):
                                    print("The new value is", settings_all[reference[choice]])
                                    break
                                else:
                                    print("This is not a valid setting.")

                    else:
                        print("Aborting change...")

            except ValueError:
                print("Please enter something valid.")
                continue
    return settings_all


def main():
    """The main entry point of the game."""
    setting = settings()
    player_stats = initialize(setting)

    print(player_stats[-1][0], "won the game. Congratulations!")

    print("\nHere are the player statistics of all rounds:\n")
    ui_help.print_tables(player_stats)

    # The console shall not close directly to display the tables.
    input("Press enter to exit the game...")
    exit()


# Starts the game, if run as main.
if __name__ == "__main__":
    main()
