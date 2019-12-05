"""This is the main module and entry point of the game "Mäxchen"."""

__author__ = "7146127, Theobald, 6956404, Stadler"
__email__ = "s7223152@cs.uni-frankfurt.de, s0706782@rz.uni-frankfurt.de"

import random as dice
import sys
import time
import ui_help


# TO DO:
# connecting the settings to the actual game
# expansion 1
# expansion 2
# expansion 3
# expansion 5
# expansion 6
# expansion 7
# etc...
# useful implementation of expansion 4


def roll_dices():
    """Create a random valid number."""

    number_1 = dice.randint(1, 6)
    number_2 = dice.randint(1, 6)

    ui_help.visual_dice(number_1, number_2)

    return max(number_1, number_2) * 10 + min(number_1, number_2)


def new_better_than_old(new_number, old_number):
    """Value two numbers.

    The number order is:
    42 > 21 > 66 > 55 > ... > 11 > others
    (others in the normal ">" order)
    """

    # Stretching the numbers so we can easily compare them.
    if new_number == 42:
        new_number *= 100
    elif new_number == 21:
        new_number *= 100
    elif new_number / 11 == new_number // 11:
        new_number *= 10

    if old_number == 42:
        old_number *= 100
    elif old_number == 21:
        old_number *= 100
    elif old_number / 11 == old_number // 11:
        old_number *= 10

    return new_number > old_number


def points_worth(number):
    """Calculate the points to subtract from the players account."""
    if number == 42:
        return 3
    elif number == 21:
        return 2
    else:
        return 1


def play(players):
    """To play the base game.
    :param players: list
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

        # A new number gets tossed
        tossed_number = roll_dices()

        # This construction shows you your number for 5 seconds
        # sys.stdout.write("Press enter to show your number")
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

        # This makes sure that a valid number is entered
        while True:
            typed_number = ui_help.input_valid_number("Please enter the number you tossed. (It's "
                                                      "allowed to lie) ")

            if not new_better_than_old(typed_number, last_tossed_number):
                print("Of course the number has to be bigger than the old one.")
                print("Read the rules and try again.")
            else:
                break

        next_turn_index = (turn_index + 1) % player_count

        believe = ui_help.input_yes_no(players[next_turn_index][0] + \
                                       " now decides. Do you believe that he tossed that? Write "
                                       "\"yes\" or \"no\": ")

        # When not believing, check the numbers
        if believe == "no":
            print("Tossed number:", tossed_number, "Typed number:", typed_number)
            if new_better_than_old(typed_number, tossed_number):
                print("Oops, you were caught red-handed.")
                print("Try to lie better next time")
                players[turn_index][1] -= points_worth(tossed_number)
                ui_help.print_points(players[turn_index])
            elif typed_number == tossed_number:
                print("No lie, no points for", players[next_turn_index][0])
                players[next_turn_index][1] -= points_worth(typed_number)
                ui_help.print_points(players[next_turn_index])
            else:
                print("It was a trap and you ran into it!")
                players[next_turn_index][1] -= points_worth(typed_number)
                ui_help.print_points(players[next_turn_index])

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


def initialize():
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

    # The player list contains 2-elements-lists: [<name>, <points>].
    players = []

    # Each player can enter his name
    for i in range(player_count):
        name = input("\nPlayer " + str(i + 1) + ": Please enter your name:\n")
        players.append([name, 10])

    # Now we choose whether we let humans play against each other or let
    # a bot play against a human.
    if player_count == 1:
        # The function for the bot belongs here
        pass
    else:
        return play(players)


def settings():
    """Adjusting the settings of the game.
    :return: list"""
    if ui_help.input_yes_no("Do you even want to change the settings? Type \"yes\" or \"no\": ") \
            == "no":
        return [0, 0, 0, 0, 0, 0]
    else:
        print("OK, let's dive right into it!\n")
        adjusted_settings = []
        if ui_help.input_yes_no(
                "Do you want to allow tossing normal values where the first digit is smaller "
                "than the second? Type \"yes\" or \"no\": ") \
                == "yes":
            adjusted_settings += [1]

        if ui_help.input_yes_no(
                "Do you want to reverse the order when a \"Mäxchen\" or a \"Hamburger\" is "
                "disclosed? Type \"yes\" or \"no\": ") \
                == "yes":
            adjusted_settings += [1]


def main():
    """The main entry point of the game."""
    #             TEST
    #         Remove later
    # for i in range(10):
    #    n1 = roll_dices() #old
    #    n2 = roll_dices() #new
    #    print(n2, "better than", n1, "is", new_better_than_old(n2, n1))
    setting = settings()
    winner = initialize()
    print(winner, "won the game. Congratulations!")


# Starts the game, if run as main.
if __name__ == "__main__":
    main()
