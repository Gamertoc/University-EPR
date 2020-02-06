"""A game of battleships. This is the main file."""

__author__ = "7146127, Theobald"
__credits__ = "Water"
__email__ = "s7223152@cs.uni-frankfurt.de"

import random as rng

"""
This is to collect my thoughts on how the game will run and will be removed once the 
documentation is in place.



"""
class Game:
    """This class contains the main game as well as its mechanics."""

    def __init__(self):
        """We need some things in every game. These are essentially the
        settings.
        :return: None"""
        self.__field_size = 10
        self.__player_count = 2
        self.__spray = 15
        self.__shots_per_ship = False
        self.__players = []
        self.__random_ship_combination = True
        self.__fleet_config = []

    def setup(self):
        """We need to set up the game, in case you want to change some
        settings.
        :return: None
        """
        while self.__field_size:
            self.adjust_value()

        if self.__random_ship_combination:
            self.ship_combination_creator()
        else:
            pass
        for i in self.players:

    @property
    def players(self):
        """Gives the list of players.
        :return: list
        """
        return self.__players

    @players.setter
    def players(self, name):
        """Adds a new player to the game.
        :param name: str
        :return: None
        """
        self.__players.append(Player(name))

    @property
    def field_size(self):
        """Get number of rows.
        :return: int
        """
        return self.__field_size

    @field_size.setter
    def field_size(self, value):
        """Set the number of rows.
        :param value: int
        :return: None
        """
        self.__field_size = value

    @property
    def player_count(self):
        """Get the number of players.
        :return: None
        """
        return self.__player_count

    @player_count.setter
    def player_count(self, value):
        """Set the number of players.
        :param value: int
        :return: None
        """
        self.__player_count = value

    @property
    def spray(self):
        """Get the spray value.
        :return: int
        """
        return self.__spray

    @spray.setter
    def spray(self, value):
        """Change the value of the spray.
        :param value: int
        :return: None
        """
        self.__spray = value

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
                if len(self.__fleet_config) == 0 or ship_count == 2:
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
        self.__fleet_config.append(size)

    def remove_ship(self, size):
        """This function removes a ship from the fleet configuration if
        there is a ship of that size.
        :param size: int
        :return: None
        """
        if size in self.__fleet_config:
            self.__fleet_config.remove(size)

    def clear_ships(self):
        """Clears the fleet configuration.
        :return: None
        """
        self.__fleet_config.clear()

    @property
    def fleet_config(self):
        """Gives the fleet config.
        :return: list
        """
        return self.__fleet_config


class Player:
    """Everything about the player goes here."""

    def __init__(self, name):
        self.name = name
        self.__board = None

    def board(self, rows, cols):
        """Creates this player's board.
        :param rows: int
        :param cols: int
        :return: None
        """
        self.__board = Board(rows, cols)


class Board:
    """This is the board."""

    def __init__(self, rows, cols):
        self.__board = []
        # The board is a 2D-Array. Every element of the board is a field
        # which has the according x and y values.
        for i in range(rows):
            self.__board.append([])
            for j in range(cols):
                self.__board[i].append(Field(i, j))


class Field:
    """This is a single field."""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__value = "empty"


class Ship:
    """A battleship."""

    def __init__(self, size, position, facing, name=None):
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

    @property
    def position(self):
        """Gives the position.
        :return: list
        """
        return self.__position

    def hit(self, shot):
        """If the ship is hit.
        :param shot: tuple
        :return: None
        """
        if shot in self.position:
            self.position.remove(shot)


if __name__ == "__main__":
    game = Game()
    game.setup()
