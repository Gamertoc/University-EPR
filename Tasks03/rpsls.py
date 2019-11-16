"""This program lets you play rock, paper, scissors, lizard, spock
against a bot. It is based on my Rock-Paper-Scissors module and uses
some of the functions.
"""

__author__ = "7146127, Theobald"


from Tasks03 import rps


def playable():
    """Contains all throwable objects/symbols"""
    throwable = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    return throwable


def system():
    """Contains the game's system"""
    win_lose = {("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Lizard"),
                ("Lizard", "Spock"), ("Spock", "Scissors"), ("Scissors", "Lizard"),
                ("Lizard", "Paper"), ("Paper", "Spock"), ("Spock", "Rock"), ("Rock", "Scissors")}
    return win_lose


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
        return rps.play_random(playable())

    # If we won the last game, we will play whatever would beat that
    # what we just played. This works by selecting a random object of
    # the list and checking whether the mentioned condition (winning
    # against our last pick) is fulfilled or not.
    win_lose = system()
    if last_game_result == "win":
        while True:
            temp = rps.play_random(playable())
            if (temp, last_game_pick) in win_lose:
                return temp

    # If we lost, we will play whatever beats the thing our opponent
    # just played. It works the same way as the one above.
    else:
        while True:
            temp = rps.play_random(playable())
            if (temp, last_game_enemy) in win_lose:
                return temp


def main():
    """Running the program when run as main."""
    antihuman_last_pick = "None"
    antihuman_last_result = "None"
    user_count = 0
    antihuman_count = 0
    antihuman_last_enemy = "None"
    while True:
        user = input("Do you want to throw Rock, Paper, Scissors, Lizard or Spock? ")
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
            result = rps.check_win(user, antihuman, system())
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


if __name__ == '__main__':
    main()
