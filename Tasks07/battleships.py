"""A game of battleships. This is the main file."""

__author__ = "7146127, Theobald"
__credits__ = "Water"
__email__ = "s7223152@cs.uni-frankfurt.de"

import random as rng

"""
This is to collect my thoughts on how the game will run and will be removed once the 
documentation is in place.

Menu: 
    Start game
    Settings
    Close

Settings:
    Player count
        1 - 4
    Field size
        5 - 25
    Spray
        active/inactive
        value
    Shots based on remaining ships
        active/inactive
    Fleet configuration
        clear
        Algorithm
        manual
            increase/decrease number
            calculate if it is in range

Start game:
    Set player names
    Placing ships
        Manually
        Algorithm
    --> Play
        Shot
            Number
            Spray
            --> Hit or miss
    
    Win/lose
    Revenge
"""


class Game:
    """This class contains the main game as well as its mechanics."""

    def __init__(self):
        """We need some things in every game. These are essentially the
        settings.
        :return: None
        """
        self.__players = []
        self.__player_count = 2
        self.__field_size = 10
        self.__spray = True
        self.__spray_value = 15
        self.__shots_per_ship = False
        self.__shots = 1
        self.__random_ship_combination = True
        self.__fleet_config = []

    def start_game(self):
        """Starting the game with some essentials.
        :return: None
        """
        for i in range(self.player_count):
            name = "Player " + str(i + 1)
            self.players.append(Player(self.field_size, name))

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

    @players.deleter
    def players(self):
        """Clears the players.
        :return: None
        """
        self.__players = []

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
    def spray_value(self):
        """Get the spray value.
        :return: int
        """
        return self.__spray_value

    @spray_value.setter
    def spray_value(self, value):
        """Change the value of the spray.
        :param value: int
        :return: None
        """
        self.__spray_value = value

    @property
    def spray(self):
        """Get whether spray is enabled or not.
        :return: bool
        """
        return self.__spray

    @spray.setter
    def spray(self, value):
        """Enable/disable spray.
        :value: bool
        :return: None
        """
        self.__spray = value

    @property
    def shots_per_ship(self):
        """Get whether the shots are ship based or not.
        :return: bool
        """
        return self.__shots_per_ship

    @shots_per_ship.setter
    def shots_per_ship(self, value):
        """Enable/disable the shots per ship.
        :param value: bool
        :return: None
        """
        self.__shots_per_ship = value

    @property
    def shots(self):
        """Get the number of shots you have.
        :return: int
        """
        return self.__shots

    @shots.setter
    def shots(self, value):
        """Change the standard number of shots you have per round.
        :param value: int
        :return: None
        """
        self.__shots = value

    def ship_combination_creator(self):
        """This function gives you a random combination of ships.
        :return: None
        """
        # We reset the ships in case there are any rests from previous
        # games
        self.clear_fleet_config()

        # A fleet can take between 10% and 25% of the board. We don't
        # want decimal numbers, only integers.
        field_count = self.field_size ** 2
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

    def clear_fleet_config(self):
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

    def fleet_percentage(self):
        """Returns the percentage of the board that is covered by the
        fleet.
        :return: int"""
        # First we need the current value of the fleet
        fleet_value = 0
        for i in range(len(self.fleet_config)):
            fleet_value += self.fleet_config[i]

        # Then we calculate the percentage and round it to one digit
        # after the decimal point.
        fleet_percent = round(fleet_value / self.field_size ** 2, 1)

        # If the value is between 10% and 25%, we can say that it is ok,
        # else it needs to be adjusted.
        fleet_percent_within_range = False
        if 10 <= fleet_percent <= 25:
            fleet_percent_within_range = True
        return fleet_percent, fleet_percent_within_range


class Player:
    """Everything about the player goes here."""

    def __init__(self, board_size, name=None):
        self.__name = name
        self.__board = Board(board_size)

    @property
    def name(self):
        """Get the player's name.
        :return: String
        """
        return self.__name

    @name.setter
    def name(self, value):
        """Set this player's name.
        :param value: String
        :return: None
        """
        self.name = value

    @property
    def board(self):
        """Get the board of the player.
        :return: Board
        """
        return self.__board

    @board.setter
    def board(self, size):
        """Creates this player's board.
        :param size: int
        :return: None
        """
        self.board = Board(size)


class Board:
    """This is the board."""

    def __init__(self, size):
        self.__board = []
        # The board is a 2D-Array. Every element of the board is a field
        # which has the according x and y values.
        for i in range(size):
            self.__board.append([])
            for j in range(size):
                self.__board[i].append(Field(i, j))

    @property
    def board(self):
        """Get the board.
        :return: list
        """
        return self.__board


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


#     @property
#     def position(self):
#         """Gives the position.
#         :return: list
#         """
#         return self.__position
#
#     def hit(self, shot):
#         """If the ship is hit.
#         :param shot: tuple
#         :return: None
#         """
#         if shot in self.position:
#             self.position.remove(shot)


if __name__ == "__main__":
    game = Game()
    game.start_game()
