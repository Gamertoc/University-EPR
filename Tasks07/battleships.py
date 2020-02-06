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
        self.__random_ship_combination = True
        self.__fleet_config = []

    def start_game(self):
        """Starting the game with some essentials.
        :return: None
        """
        self.ship_combination_creator()
        for i in range(self.player_count):
            name = "Player " + str(i + 1)
            self.players.append(Player(self.field_size, name))
        # for i in self.fleet_config:
        #     for j in self.players:
        #         j.add_ship(i)

        self.players[0].position_ship(self.fleet_config[0], 9, 5, "north")

    def check_ship_placement(self):
        """This function checks whether all ships are placed or not.
        :return: bool
        """
        for i in self.players:
            for j in i.fleet:
                if not j.position:
                    return False
        return True

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
        self.__fleet = []

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

    @property
    def fleet(self):
        """Get the player's fleet.
        :return: list
        """
        return self.__fleet

    def add_ship(self, size):
        """Add a ship to this player's fleet.
        :param size: int
        :return: None
        """
        self.fleet.append(Ship(size))

    def position_ship(self, size, x, y, facing):
        """Position the ships you have.
        :param size: int
        :param x: int
        :param y: int
        :param facing: str
        :return: bool
        """
        position = []
        ship = None

        # First, we need to know what ship we are positioning
        for i in self.fleet:
            if size == i.size and i.position == []:
                ship = i
                break

        if ship is not None:
            try:
                # Now we can calculate the full position of this ship
                for i in range(size):
                    if facing == "north":
                        position.append(self.board.board[x][y - i])
                    elif facing == "south":
                        position.append(self.board.board[x][y + i])
                    elif facing == "west":
                        position.append(self.board.board[x - i][y])
                    elif facing == "east":
                        position.append(self.board.board[x + i][y])
            except IndexError:
                return False

            # We have to check whether the ships is next to any other ship.
            # We need to check for any connection, horizontally, vertically
            # or diagonally
            for i in position:
                for j in range(-1, 2):  # horizontal check
                    for k in range(-1, 2):  # vertical check
                        x = i.x + j
                        y = i.y + k
                        try:
                            test_field = self.board.board[x][y]
                        except IndexError:
                            continue
                        if test_field in self.board.board[x] and test_field not in position:
                            if not test_field.value == 0:
                                return False
                        else:
                            continue

            # Now we can finally place the ship and mark the fields
            for i in position:
                i.value = 1
            ship.set_position(position)
            return True


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

    # WATER: 0
    # SHIP: 1
    # MISS: 2
    # HIT: 3

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__value = 0

    @property
    def x(self):
        """Get the x value.
        :return: int
        """
        return self.__x

    @property
    def y(self):
        """Get the x value.
        :return: int
        """
        return self.__y

    @property
    def value(self):
        """Returns the current value of this field.
        :return: int
        """
        return self.__value

    @value.setter
    def value(self, value):
        """Sets the current value of the field.
        :param value: int
        :return: None
        """
        self.__value = value


class Ship:
    """A ship of a player's fleet."""

    def __init__(self, size):
        self.__size = size
        self.__position = []
        if size == 3:
            name = "Destroyer"
        elif size == 4:
            name = "Cruiser"
        elif size == 5:
            name = "Battleship"
        else:
            name = "Carrier"
        self.__name = name

    @property
    def size(self):
        """Get the size of the ship.
        :return: int
        """
        return self.__size

    @property
    def position(self):
        """Get the position of this ship.
        :return: list
        """
        return self.__position

    def set_position(self, position):
        """Set the position of the ship.
        :param position: list
        :return: None
        """
        for i in range(len(position)):
            self.__position.append(i)


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
