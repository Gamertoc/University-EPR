"""This is the main module and entry point of the game "Mäxchen"."""
# -*- coding: utf-8 -*-
# noinspection SpellCheckingInspection
__author__ = "7146127, Theobald, 6956404, Stadler"
__email__ = "s7223152@cs.uni-frankfurt.de, s0706782@rz.uni-frankfurt.de"

import random as dice
import time
import ui_help


# TO DO:
# Allow numbers where the first dice can be smaller than the second
# Document cheats
# Add a bot

# Settings that need updates:
# 1: Not implemented
# 2: Not implemented
# 3: Not implemented
# 5: Not implemented
# 6: Not implemented
# 7: Not implemented
# 8: Not implemented


def roll_dices(order_numbers):
    """Create a random valid number."""

    number_1 = dice.randint(1, 6)
    number_2 = dice.randint(1, 6)

    if order_numbers:
        return max(number_1, number_2) * 10 + min(number_1, number_2)
    else:
        return number_1 * 10 + number_2


def new_better_than_old(new_number, old_number, settings_all):
    """Value two numbers.

    The number order is:
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
    """Calculate the points to subtract from the players account."""
    
    if number == settings_all["Hamburger"]:
        return 3
    elif number == settings_all["Mäxchen"]:
        return 2
    else:
        return 1


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
            order_numbers = settings_all["numbers_in_order"]
            tossed_number = roll_dices(order_numbers)

        # This construction shows you your number for 5 seconds after pressing enter.
        input("Press enter to show your number")
        for i in range(6):
            print("\rYou tossed a " + str(tossed_number) + " which will vanish in " + str(5 - i),
                  flush=True, sep="", end="")
            time.sleep(1)

        print("\rThe number from the last turn was", last_tossed_number, "   ")

        typed_number = 0

        # This makes sure that a valid number is entered.
        while True:
            typed_number = ui_help.input_valid_number("Please enter the number you tossed (It's "
                                                      "allowed to lie). ",
                                                      settings_all["numbers_in_order"])

            if not new_better_than_old(typed_number, last_tossed_number, settings_all):
                print("Of course the number has to be bigger than the old one.\nRead the rules "
                      "and try again.")
            else:
                break

        next_turn_index = (player_count + turn_index + settings_all["play_order"]) % player_count

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
            if (settings_all["reverse_mäxchen"] and tossed_number == 21) or (settings_all[
                                                                                 "reverse_hamburger"] and tossed_number == 42):
                settings_all["play_order"] *= -1

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
        if typed_number == 42:
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
        return
    print("Welcome to the game!")
    print("Please enter your names. It is your responsibility to pick unique names.\n")

    # The player list contains 4-element-lists: [<name>, <points>, <cheat>, <points_table>].
    players = []

    # Each player can enter his name
    for i in range(player_count):
        name = input("\nPlayer " + str(i + 1) + ": Please enter your name:\n")
        cheat = ""

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
        
        players.append([name, 10, cheat, []])

    # Now we choose whether we let humans play against each other or let
    # a bot play against a human.
    if player_count == 1:
        # The function for the bot belongs here
        pass
    else:
        return play(players, settings_all)


def settings():
    """Adjusting the settings of the game.
    :return: dictionary
    """

    # This dictionary stores all the settings
    settings_all = {
        "Mäxchen": 21,
        "Hamburger": 42,
        "numbers_in_order": True,  # If True, only use 1st digit >= 2nd digit numbers.
        "play_order": 1,
        "points_to_start": 10,
        "point_loss_normal": 1,
        "point_loss_mäxchen": 2,
        "point_loss_hamburger": 3,
        "reverse_mäxchen": True,
        "reverse_hamburger": True,
    }

    # This dictionary references each setting by a number
    reference = {
        1: "Mäxchen",
        2: "Hamburger",
        3: "numbers_in_order",
        4: "play_order",
        5: "points_to_start",
        6: "point_loss_normal",
        7: "point_loss_mäxchen",
        8: "point_loss_hamburger",
        9: "reverse_mäxchen",
        10: "reverse_hamburger",
    }

    # This dictionary stores the explanation of each setting.
    help_game = {
        -1: "What do you need help with?\n0: What do I even do here?\n1 to 10: What that "
            "setting does.\nlist: List all settings.\nq to go back to the settings.",
        0: "To change a setting, simply type a number from 1 to 10 to change the according "
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
    }
    print(help_game[0])

    print("\033[91m{}\033[00m".format("Please remember that you can seriously fuck up the "
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

            except ValueError:
                print("Please enter something valid.")
                continue
    return settings_all


def main():
    """The main entry point of the game."""
    
    #             TEST
    #         Remove later
    # for i in range(10):
    #    n1 = roll_dices() #old
    #    n2 = roll_dices() #new
    #    print(n2, "better than", n1, "is", new_better_than_old(n2, n1))
    setting = settings()
    player_stats = initialize(setting)
    
    print(player_stats[-1][0], "won the game. Congratulations!")

    print("\nHere are the player statistics of all rounds:\n")
    ui_help.print_tables(player_stats)
    exit()


# Starts the game, if run as main.
if __name__ == "__main__":
    main()
