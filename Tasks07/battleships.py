"""A game of battleships. This is the main file."""

__author__ = "7146127, Theobald"
__credits__ = "Water"
__email__ = "s7223152@cs.uni-frankfurt.de"

import random as rng


class Game:

    def __init__(self):
        """We need some things in every game. These are essentially the
        settings.
        :return: None"""
        self.rows = 10
        self.cols = 10
        self.player_count = 2
        self.spray = 15
        self.shots_per_ship = False
        self.players = []
        self.random_ship_combination = False
        self.ships = []

    def setup(self):
        """We need to set up the game, in case you want to change some
        settings.
        :return: None
        """
        b = Board()
        while self.rows < 1 or self.cols < 1 or self.rows * self.cols < 24:
            self.adjust_value()
        b.create_board(self.rows, self.cols)

    def change_rows(self, x):
        """This lets you change the number of rows.
        :param x: int
        :return: None
        """
        self.rows = x

    def change_cols(self, y):
        """This lets you change the number of columns.
        :param y: int
        :return: None
        """
        self.cols = y

    def change_player_count(self, player_count):
        """This lets you change the player count of the game.
        :return: None
        """
        self.player_count = player_count

    def change_spray(self, spray):
        """This lets you change the spray value of the shots.
        :return: None
        """
        self.spray = spray

    def adjust_value(self):
        """In case the board is too small, this function is called.
        :return: None
        """
        pass

    def random_ship_combination(self):
        """This function gives you a random combination of ships.
        :return: None
        """
        # We reset the ships in case there are any rests from previous
        # games
        # A fleet can take between 10% and 25% of the board. We don't
        # want decimal numbers, only integers.
        field_count = self.rows * self.cols
        fleet_max = (field_count / 4) // 1
        fleet_min = field_count / 10
        if not fleet_min == fleet_min // 1:
            fleet_min = fleet_min // 1 + 1

        # Now we take a random value between the min and the max to
        # determine the size of our fleet. It must be at least 6 since
        # we need at least 2 ships that are at least 3 spaces long.
        while True:
            fleet_size = rng.randint(fleet_min, fleet_max)
            if fleet_size >= 6:
                break

        # Now we get to the algorithm (more on that in the
        # documentation
        while True:

            # If the remaining fleet is smaller than 8 (except for 6),
            # we can determine the other ships and escape afterwards
            if fleet_size == 7:
                self.ships.append(4)
                self.ships.append(3)
                break
            elif fleet_size < 6:
                self.ships.append(fleet_size)
                break

            # If the fleet has a size of 6, there are 2 combinations.
            elif fleet_size == 6:
                ship_count = rng.randint(1, 2)
                if len(self.ships) == 0 or ship_count == 2:
                    self.ships.append(3)
                    self.ships.append(3)
                else:
                    self.ships.append(6)
                break

            # If the fleet is bigger, we use a simple algorithm
            else:

                # First, we need to check for the largest ship that we
                # can have while having another ship after that.
                largest_possible = 6
                while True:
                    if fleet_size - largest_possible < 3:
                        largest_possible -= 1
                    else:
                        break

                # Now we generate a ship,
                ship = rng.randint(3, largest_possible)
                # add it to the other ones
                self.ships.append(ship)
                # and reduce the fleet size.
                fleet_size -= ship

        print(self.ships)


class Player:

    def __init__(self, name):
        self.name = name


class Board:

    def __init__(self):
        self.board = []

    def create_board(self, rows, cols):
        """In this function the board is created. The standard size is
        10x10, but this can be changed.
        :param cols: int
        :param rows: int
        :return: None
        """

        # The board is a 2D-Array. Every element of the board is a field
        # which has the according x and y values.
        for i in range(rows):
            self.board.append([])
            for j in range(cols):
                self.board[i].append(Field(i, j))


class Field:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = "empty"


if __name__ == "__main__":
    game = Game()
    game.setup()
