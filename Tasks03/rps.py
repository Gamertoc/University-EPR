"""This program lets you play rock-paper-scissors against a machine.
Since I wanna do some good work, I will program different methods of
playing first, then let them play against each other and then let the
best one play against you lul.
"""

__author__ = "7146127, Theobald"

import random as dice


def play_random():
    """This function just randomly decides what it wants to play and
    doesn't take anything into account.
    """
    throwable = playable()
    return throwable[dice.randint(1, len(throwable))-1]


def play_human(last_game_pick, last_game_result):
    """Humans tend to keep a winning strategy, but tend to switch when
    they lose.
    Source: Experience and https://arxiv.org/pdf/1404.5199v1.pdf.
    It is also called the "win-stay, lose-shift" strategy. That's
    exactly what this one will do. For this one the program will be
    written in a way that it gets its last pick and the result of that.
    If it was successful, it will stick with the decision, else it will
    change.
    :param last_game_pick: String
    :param last_game_result: String
    :return: String
    """

    # For the first game there is no strategy, so it just plays random
    if last_game_pick == "None":
        play_random()

    # If we won the last game we will stick with the decision.
    if last_game_result == "win":
        return last_game_pick
    # In any other case, we will switch. For that we use the random
    # class to determine our strategy as long as it's different from the
    # last one.
    while True:
        rps = play_random()
        if rps != last_game_pick:
            return rps


def play_antihuman(last_game_pick, last_game_enemy, last_game_result):
    """This strategy is a strategy devised from the human behavior
    mentioned above. An article on the website arstechnica
    (https://arstechnica.com/science/2014/05/win-at-rock-paper-scissors
    -by-knowing-thy-opponent/) describes is this way: If you lose,
    switch to the thing that beats the thing your opponent just played.
    If you win, don't keep playing the same thing, but instead switch to
    the thing that would beat the thing that you just played.
    :param last_game_pick: String
    :param last_game_enemy: String
    :param last_game_result: String
    :return: String
    """

    # For the first game there is no strategy, so it just plays random
    if last_game_pick == "None":
        return play_random()
    # If we won the last game, we will play whatever would beat that
    # what we just played.
    win_lose = system()
    if last_game_result == "win":
        while True:
            rps = play_random()
            if (rps, last_game_pick) in win_lose:
                return rps

    # If we lost, we will play whatever beats the thing our opponent
    # just played.
    else:
        while True:
            rps = play_random()
            if (rps, last_game_enemy) in win_lose:
                return rps


def playable():
    """Stores the playable objects"""
    throwable = ["Rock", "Paper", "Scissors"]
    return throwable


def system():
    """Stores the system of the game"""
    win_lose = {("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")}
    return win_lose


def check_win(pick_one, pick_two):
    """This function checks which of the picks won. A draw counts as
    loss for both, since nobody gets points in a draw.
    :param pick_one: String
    :param pick_two: String
    :return: String
    """
    # We just check which thing won and return it accordingly
    win_lose = system()
    if pick_one == pick_two:
        return "Draw"
    elif (pick_one, pick_two) in win_lose:
        return "First won"
    elif (pick_two, pick_one) in win_lose:
        return "Second won"


def find_best_machine(revisions):
    """We wanna find out what the best algorithm is. For this we let
    every algorithm play against every other.
    :param revisions: int
    """
    # The first one mentioned is the one that counts, the second one is
    # the enemy
    random_human = 0
    random_antihuman = 0
    human_random = 0
    human_antihuman = 0
    antihuman_random = 0
    antihuman_human = 0

    # Let's start with the game random vs human. And since we basically
    # do the same stuff four times (three times in bot vs bot and then
    # for bot vs human again), I'll just explain it one time
    human_last_pick = "None"
    human_last_result = "None"
    i = 0
    # Draws don't count to the counter, so we use a while-loop and just
    # increase the counter when someone won.
    while i < revisions:
        # We let both algorithms play and let the function check who won
        human = play_human(human_last_pick, human_last_result)
        random = play_random()
        result = check_win(random, human)

        # Depending on who won we adjust the counter and the feedback
        # for the last result
        if result == "First won":
            human_random += 1
            human_last_result = "loss"
            i += 1
        elif result == "Second won":
            random_human += 1
            human_last_result = "loss"
            i += 1
        else:
            human_last_result = "loss"

        # Don't forget the last pick for the functions that need it
        human_last_pick = human

    # And after all that print a nice little message about the score and
    # who won.
    if human_random > random_human:
        print("Human won vs random in", revisions, "rounds with", human_random, "-", random_human)
    else:
        print("Random won vs human in", revisions, "rounds with", random_human, "-", human_random)

    # Now it's the same for the other two games. Starting with random vs
    # antihuman
    antihuman_last_pick = "None"
    antihuman_last_result = "None"
    antihuman_last_enemy = "None"
    i = 0
    # Draws don't count to the counter
    while i < revisions:
        antihuman = play_antihuman(antihuman_last_pick, antihuman_last_enemy,
                                   antihuman_last_result)
        random = play_random()
        result = check_win(random, antihuman)
        if result == "First won":
            antihuman_random += 1
            antihuman_last_result = "loss"
            i += 1
        elif result == "Second won":
            random_antihuman += 1
            antihuman_last_result = "loss"
            i += 1
        else:
            antihuman_last_result = "loss"
        antihuman_last_pick = antihuman
        antihuman_last_enemy = random

    if antihuman_random > random_antihuman:
        print("Antihuman won vs random in", revisions, "rounds with", antihuman_random, "-",
              random_antihuman)
    else:
        print("Random won vs antihuman in", revisions, "rounds with", random_antihuman, "-",
              antihuman_random)

    # Now the interesting game, human vs antihuman
    human_last_pick = "None"
    human_last_result = "None"
    antihuman_last_pick = "None"
    antihuman_last_result = "None"
    antihuman_last_enemy = "None"
    i = 0
    # Draws don't count to the counter
    while i < revisions:
        human = play_human(human_last_pick, human_last_result)
        antihuman = play_antihuman(antihuman_last_pick, antihuman_last_enemy,
                                   antihuman_last_result)
        result = check_win(human, antihuman)
        if result == "First won":
            human_antihuman += 1
            human_last_result = "win"
            antihuman_last_result = "loss"
            i += 1
        elif result == "Second won":
            antihuman_human += 1
            human_last_result = "loss"
            antihuman_last_result = "win"
            i += 1
        else:
            human_last_result = "loss"
            antihuman_last_result = "loss"
        human_last_pick = human
        antihuman_last_pick = antihuman
        antihuman_last_enemy = human

    if human_antihuman > antihuman_human:
        print("Human won vs antihuman in", revisions, "rounds with", human_antihuman, "-",
              antihuman_human)
    else:
        print("Antihuman won vs human in", revisions, "rounds with", antihuman_human, "-",
              human_antihuman)

    # Now we add all the games together and get a total for which
    # function won how many games
    antihuman_won_games = antihuman_human + antihuman_random
    human_won_games = human_antihuman + human_random
    random_won_games = random_human + random_antihuman
    print("Human won a total of", human_won_games, "games.")
    print("Antihuman won a total of", antihuman_won_games, "games.")
    print("Random won a total of", random_won_games, "games.")
    print("Antihuman won with", antihuman_won_games, "out of", 2 * revisions, "games.")
    # Antihuman proved to be the winning strategy, since it was
    # literally designed to win against average humans. Therefore it
    # will always be the winner in this contests.


def play_user():
    antihuman_last_pick = "None"
    antihuman_last_result = "None"
    user_count = 0
    antihuman_count = 0
    antihuman_last_enemy = "None"
    while True:
        user = input("Do you want to throw Rock, Paper or Scissors? ")
        antihuman = play_antihuman(antihuman_last_pick, antihuman_last_enemy,
                                   antihuman_last_result)

        # You can quit by entering q. It will show you the score you
        # achieved
        if user == "q":
            print("You played", user_count, "-", antihuman_count)
            exit()

        # If the input is neither q nor a valid game input, you just
        # have to enter something valid
        elif user not in playable():
            continue

        # Same as in the bot vs bot version: Adjusting the win counter
        # and the last_pick/last_result for the machine
        else:
            result = check_win(user, antihuman)
            if result == "First won":
                print("You won with", user, "against", antihuman)
                user_count += 1
                antihuman_last_result = "loss"
            elif result == "Second won":
                print("You lost with", user, "against", antihuman)
                antihuman_count += 1
                antihuman_last_result = "win"
            else:
                print("Draw! You both threw", user)
                antihuman_last_result = "loss"
            antihuman_last_pick = antihuman
            antihuman_last_enemy = user


def main():
    """Starting the program."""
    if input("Do you want to let the bots play against each other? (Y/n) ") == "Y":
        find_best_machine(1000000)
    play_user()


if __name__ == '__main__':
    main()
