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
        self.__rows = 10
        self.__cols = 10
        self.__player_count = 2
        self.__spray = 15
        self.__shots_per_ship = False
        self.__players = []
        self.__random_ship_combination = True
        self.__ships = []

    def setup(self):
        """We need to set up the game, in case you want to change some
        settings.
        :return: None
        """
        while self.__rows < 1 or self.__cols < 1 or self.__rows * self.__cols < 24:
            self.adjust_value()

        if self.__random_ship_combination:
            self.ship_combination_creator()
        else:
            pass
        board = Board(self.__rows, self.__cols)

    def change_rows(self, x):
        """This lets you change the number of rows.
        :param x: int
        :return: None
        """
        self.__rows = x

    def change_cols(self, y):
        """This lets you change the number of columns.
        :param y: int
        :return: None
        """
        self.__cols = y

    def change_player_count(self, player_count):
        """This lets you change the player count of the game.
        :return: None
        """
        self.__player_count = player_count

    def change_spray(self, spray):
        """This lets you change the spray value of the shots.
        :return: None
        """
        self.__spray = spray

    def adjust_value(self):
        """In case the board is too small, this function is called.
        :return: None
        """
        pass

    def ship_combination_creator(self):
        """This function gives you a random combination of ships.
        :return: None
        """
        # We reset the ships in case there are any rests from previous
        # games
        self.clear_ships()
        # A fleet can take between 10% and 25% of the board. We don't
        # want decimal numbers, only integers.
        field_count = self.__rows * self.__cols
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
                self.add_ship(4)
                self.add_ship(3)
                break
            elif fleet_size < 6:
                self.add_ship(fleet_size)
                break

            # If the fleet has a size of 6, there are 2 combinations.
            elif fleet_size == 6:
                ship_count = rng.randint(1, 2)
                if len(self.__ships) == 0 or ship_count == 2:
                    self.add_ship(3)
                    self.add_ship(3)
                else:
                    self.add_ship(6)
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
                self.add_ship(ship)
                # and reduce the fleet size.
                fleet_size -= ship

    def add_ship(self, size):
        """This function adds a ship to the fleet configuration.
        :param size: int
        :return: None
        """
        self.__ships.append(size)

    def remove_ship(self, size):
        """This function removes a ship from the fleet configuration if
        there is a ship of that size.
        :param size: int
        :return: None
        """
        if size in self.__ships:
            self.__ships.remove(size)

    def clear_ships(self):
        """Clears the fleet configuration.
        :return: None
        """
        self.__ships.clear()

    def get_fleet(self):
        """Give the fleet configuration to the players.
        :return: list
        """
        return self.__ships


class Player:

    def __init__(self, name):
        self.name = name


class Board:

    def __init__(self, rows, cols):
        self.__board = []
        # The board is a 2D-Array. Every element of the board is a field
        # which has the according x and y values.
        for i in range(rows):
            self.__board.append([])
            for j in range(cols):
                self.__board[i].append(Field(i, j))


class Field:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__value = "empty"


class Ship:

    def __init__(self, size, position, facing, name=""):
        self.__size = size
        self.__position = []
        self.__name = name
        # Dependent of where the ship is facing, we can calculate the
        # other spaces it takes.
        x = position[0]
        y = position[1]
        for i in range(size):
            if facing == "north":
                self.__position.append((x, y - i))
            elif facing == "south":
                self.__position.append((x, y + i))
            elif facing == "west":
                self.__position.append((x - i, y))
            elif facing == "east":
                self.__position.append((x - i, y))


if __name__ == "__main__":
    game = Game()
    game.setup()
