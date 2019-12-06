"""This is the main module and entry point of the game "Mäxchen"."""

__author__ = "7146127, Theobald, 6956404, Stadler"
__email__ = "s7223152@cs.uni-frankfurt.de, s0706782@rz.uni-frankfurt.de"

import random as dice
import sys
import time
import ui_help


# TO DO:
# expansion 1
# expansion 3
# expansion 5
# expansion 7
# etc...
# Add unicode emoji (!!!!!! Idle crashes!!!!!!!!) DONT!


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
    elif new_number % 11 == new_number // 10:
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

    # This is the index of the player, who does the next move.
    # It is the list index, not the number.
    turn_index = 0

    while not game_over:

        print("It is " + players[turn_index][0] + "'s turn.")


        # Cheaters have a 50% chance of their cheated number.
        if players[turn_index][2] == "HTTB" and dice.randint(0, 1) == 1:
            tossed_number = settings_all["Hamburger"]
        elif players[turn_index][2] == "MM" and dice.randint(0, 1) == 1:
            tossed_number = settings_all["Mäxchen"]
        else:
            # A new number gets tossed.
            order_numbers = settings_all["numbers_in_order"]
            tossed_number = roll_dices(order_numbers)

        # This construction shows you your number for 5 seconds.
        # sys.stdout.write("Press enter to show your number")
        # 
        # !!!!! Does not work with the python shell !!!!!
        # 
        input("Press enter to show your number")
        for i in range(6):
            sys.stdout.write("\rYou tossed a " + str(tossed_number) + " which will vanish in " +
                             str(5 - i))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.flush()
        sys.stdout.write("\r")

        print("The number from the last turn was", last_tossed_number)

        typed_number = 0

        # This makes sure that a valid number is entered.
        while True:
            typed_number = ui_help.input_valid_number("Please enter the number you tossed. (It's "
                                                      "allowed to lie) ", \
                                                      settings_all[numbers_in_order])

            if not new_better_than_old(typed_number, last_tossed_number, settings_all):
                print("Of course the number has to be bigger than the old one.")
                print("Read the rules and try again.")
            else:
                break

        next_turn_index = (turn_index + 1) % player_count

        believe = ui_help.input_yes_no(players[next_turn_index][0] + \
                                       " now decides. Do you believe that he tossed that? Write "
                                       "\"yes\" or \"no\": ")

        # When not believing, check the numbers.
        if believe == "no":
            print("These were the dices:")
            ui_help.visual_dice(tossed_number // 10, tossed_number % 10)
            print("Tossed number:", tossed_number, "Typed number:", typed_number)
            if new_better_than_old(typed_number, tossed_number, settings_all):
                if players[turn_index][2] != "GK":
                    print("Oops, you were caught red-handed.")
                    print("Try to lie better next time ;-)")
                    players[turn_index][1] -= points_worth(tossed_number, settings_all)
                    ui_help.print_points(players[turn_index])
                else:
                    print("Due to an internal crash, the accout of " + players[turn_index][0] \
                          + "was locked. He/She loses no points this round.")
            elif typed_number == tossed_number:
                if players[next_turn_index][2] != "GK":
                    print("No lie, no points for", players[next_turn_index][0])
                    players[next_turn_index][1] -= points_worth(typed_number, settings_all)
                    ui_help.print_points(players[next_turn_index])
                else:
                    print("ERROR, cannot remove points from such a nice player.")
                    ui_help.print_points(players[next_turn_index])
            else:
                print("It was a trap and you ran into it, " + players[next_turn_index][0]  + "!")
                if players[next_turn_index][2] != "GK":
                    players[next_turn_index][1] -= points_worth(typed_number, settings_all)
                    ui_help.print_points(players[next_turn_index])
                else:
                    print("But no problem. Shit happens.")
            #Reset the number for the next turn
            typed_number = 0

        # Checking if any player has less than 1 point
        for i in players:
            if i[1] <= 0:
                print(i[0], "has", i[1], "and is therefore out of the game! Better luck next "
                                         "time.")
                players.remove(i)

        # Check for win
        if len(players) == 1:
            return players[0]

        # After that we refresh the player count
        player_count = len(players)

        # Calculates the new player turn index.
        turn_index = (turn_index + 1) % player_count
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
    player_count = ui_help.input_number("How many players want to play? ")

    # Check whether the player count is valid. Is has to be 2 or larger (for now)
    if player_count <= 0:
        print("Ok, you do not have to...")
        return
    elif player_count == 1:
        print("Stop the jokes...")
    else:
        print("Welcome to the game!")

    # The player list contains 3-element-lists: [<name>, <points>, <cheat>].
    players = []

    # Each player can enter his name
    for i in range(player_count):
        name = input("\nPlayer " + str(i + 1) + ": Please enter your name:\n")
        cheat = ""

        if name[:14] == "HamToTheBurger":
            cheat = "HTTB"
            name = name[14:]
        elif name[:7] == "MegaMax":
            cheat = "MM"
            name = name[7:]
        elif name[:7] == "GodKing":
            cheat = "GK"
            name = name[7:]
        
        players.append([name, 10, cheat])

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
    
    settings_all = {
        "Mäxchen": 21,
        "Hamburger": 42,
        "numbers_in_order" : True  # If True, only use 1st digit > 2nd digit numbers.
    }
    if ui_help.input_yes_no("Do you even want to change the settings? Type \"yes\" or \"no\": ") \
            == "no":
        return settings_all
    else:
        print("OK, let's dive right into it!\n")
        if ui_help.input_yes_no(
                "Do you want to allow tossing normal values where the first digit is smaller "
                "than the second? Type \"yes\" or \"no\": ") \
                == "yes":
            settings_all["numbers_in_order"] = False

        if ui_help.input_yes_no(
                "Do you want to reverse the definitions of \"Mäxchen\" and \"Hamburger\"? "
                "Type \"yes\" or \"no\": ") \
                == "yes":
            settings_all["Mäxchen"] = 42
            settings_all["Hamburger"] = 21


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
    winner = initialize(setting)
    print(winner, "won the game. Congratulations!")


# Starts the game, if run as main.
if __name__ == "__main__":
    main()
