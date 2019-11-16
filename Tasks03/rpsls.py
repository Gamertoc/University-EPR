"""This program lets you play rock, paper, scissors, lizard, spock against a bot."""

__author__ = "7146127, Theobald"

import random as dice
from Tasks03 import rps


def playable():
    """Contains all throwable objects/symbols"""
    throwable = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    return throwable


def system():
    """Contains the game's system"""
    win_lose = {("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Lizard"), ("Lizard",
                                                                               "Spock"),
                ("Spock", "Scissors"), ("Scissors", "Lizard"), ("Lizard", "Paper"), ("Paper",
                                                                                     "Spock"),
                ("Spock", "Rock"), ("Rock", "Scissors")}


def main():
    rps.play_user()


if __name__ == '__main__':
    main()
