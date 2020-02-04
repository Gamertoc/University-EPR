"""A game of battleships. This is the main file."""

__author__ = "7146127, Theobald"
__credits__ = "Water"
__email__ = "s7223152@cs.uni-frankfurt.de"


class Game:

    def __init__(self):
        """We need some things in every game."""
        self.rows = 10
        self.cols = 10

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

    def adjust_value(self):
        """In case the board is too small, this function is called.
        :return: None
        """
        pass


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
