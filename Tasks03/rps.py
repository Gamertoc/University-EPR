"""This program lets you play rock-paper-scissors against a machine. Since I wanna do some good
work, I will program different methods of playing first, then let them play against each other
and then let the best one play against you lul."""

__author__ = "7146127, Theobald"

import random as dice


def play_random():
    """This function just randomly decides what it wants to play and doesn't take anything into
    account."""

    rps = dice.randint(1, 3)
    if rps == 1:
        return "Rock"
    elif rps == 2:
        return "Paper"
    else:
        return "Scissors"


def play_human(last_game_pick, last_game_result):
    """Humans tend to keep a winning strategy, but tend to switch when they lose. Source:
    Experience and Google (https://arxiv.org/pdf/1404.5199v1.pdf). It is also called the
    "win-stay, lose-shift" strategy. That's exactly what this one will do. For this one the
    program will be written in a way that it gets its last pick and the result of that. If it
    was successful, it will stick with the decision, else it will change.
    :param last_game_pick: String
    :param last_game_result: String
    :return: String
    """

    # For the first game there is no strategy, so it just plays random
    if last_game_pick == "None":
        return play_random()

    # If we won the last game we will stick with the decision.
    if last_game_result == "win":
        return last_game_pick
    # In any other case, we will switch. For that we use the random class to determine our
    # strategy as long as it's different from the last one.
    while True:
        rps = play_random()
        if rps != last_game_pick:
            return rps


def play_antihuman(last_game_pick, last_game_result):
    """This strategy is a strategy devised from the human behavior mentioned above. An article
    on the website arstechnica (https://arstechnica.com/science/2014/05/win-at-rock-paper
    -scissors-by-knowing-thy-opponent/) describes is this way: If you lose, switch to the thing
    that beats the thing your opponent just played. If you win, don't keep playing the same
    thing, but instead switch to the thing that would beat the thing that you just played.
    """

    # For the first game there is no strategy, so it just plays random
    if last_game_pick == "None":
        return play_random()

    # If we won the last game, we will play whatever would beat that what we just played.
    if last_game_result == "win":
        if last_game_pick == "Rock":
            return "Paper"
        elif last_game_pick == "Paper":
            return "Scissors"
        else:
            return "Rock"

    # If we lost, we will play whatever beats the thing our opponent just played.
    if last_game_pick == "Rock":
        return "Scissors"
    elif last_game_pick == "Paper":
        return "Rock"
    else:
        return "Paper"


def check_win(pick_one, pick_two):
    """This function checks which of the picks won. A draw counts as loss for both, since nobody
    gets points in a draw.
    """
    # We just check which thing won
    if pick_one == "Rock":
        if pick_two == "Paper":
            return "Second won"
        elif pick_two == "Scissors":
            return "First won"
    elif pick_one == "Paper":
        if pick_two == "Scissors":
            return "Second won"
        elif pick_two == "Rock":
            return "First won"
    elif pick_one == "Scissors":
        if pick_two == "Rock":
            return "Second won"
        elif pick_two == "Paper":
            return "First won"
    return "Draw"


def find_best_machine(revisions):
    """We wanna find out what the best algorithm is. For this we let every algorithm play
    against every other.
    :param revisions: int
    """
    # The first one mentioned is the one that counts, the second one is the enemy
    random_human = 0
    random_antihuman = 0
    human_random = 0
    human_antihuman = 0
    antihuman_random = 0
    antihuman_human = 0

    # Let's start with the game random vs human
    human_last_pick = "None"
    human_last_result = "None"
    i = 0
    # Draws don't count to the counter
    while i < revisions:
        human = play_human(human_last_pick, human_last_result)
        random = play_random()
        result = check_win(random, human)
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
        human_last_pick = human

    if human_random > random_human:
        print("Human won vs random in", revisions, "rounds with", human_random, "-", random_human)
    else:
        print("Random won vs human in", revisions, "rounds with", random_human, "-", human_random)

    # Now it's the same for the other two games. Starting with random vs antihuman
    antihuman_last_pick = "None"
    antihuman_last_result = "None"
    i = 0
    # Draws don't count to the counter
    while i < revisions:
        antihuman = play_antihuman(antihuman_last_pick, antihuman_last_result)
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
    i = 0
    # Draws don't count to the counter
    while i < revisions:
        human = play_human(human_last_pick, human_last_result)
        antihuman = play_antihuman(antihuman_last_pick, antihuman_last_result)
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

    if human_antihuman > antihuman_human:
        print("Human won vs antihuman in", revisions, "rounds with", human_antihuman, "-",
              antihuman_human)
    else:
        print("Antihuman won vs human in", revisions, "rounds with", antihuman_human, "-",
              human_antihuman)

    # Now we add all the games together and get a total for games won each
    antihuman_won_games = antihuman_human + antihuman_random
    human_won_games = human_antihuman + human_random
    random_won_games = random_human + random_antihuman
    print("Human won a total of", human_won_games, "games.")
    print("Antihuman won a total of", antihuman_won_games, "games.")
    print("Random won a total of", random_won_games, "games.")
    print("Antihuman won with", antihuman_won_games, "out of", 2 * revisions, "games.")
    # Antihuman proved to be the winning strategy, since it was literally designed to win
    # against average humans. Therefore it will always be the winner in this contests.


def main():
    if input("Do you want to let the bots play against each other? (Y/n) ") == "Y":
        find_best_machine(1000000)
    antihuman_last_pick = "None"
    antihuman_last_result = "None"
    user_count = 0
    antihuman_count = 0
    while True:
        user = input("Do you want to throw Rock, Paper or Scissors? ")
        antihuman = play_antihuman(antihuman_last_pick, antihuman_last_result)
        if user == "q":
            print("You played", user_count, "-", antihuman_count)
            exit()
        elif not user == "Scissors" and not user == "Rock" and not user == "Paper":
            continue
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


if __name__ == '__main__':
    main()
