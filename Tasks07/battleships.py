"""A game of battleships. This is the main file."""

__author__ = "7146127, Theobald"
__credits__ = "Water"
__email__ = "s7223152@cs.uni-frankfurt.de"

import array


class Game:

    def main(self):
        b = Board()
        b.create_board()


class Board:

    def create_board(self, cols=5, rows=10):
        """In this function the board is created. The standard size is
        10x10, but this can be changed.
        :param cols: int
        :param rows: int
        :return: None
        """

        # The board is a 2D-Array.

        # Every element of the board is a field which has the according
        # x and y values.
        board = []
        for i in range(rows):
            board.append([])
            for j in range(cols):
                board[i].append(Field(i, j))


class Field:

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    game = Game()
    game.main()
