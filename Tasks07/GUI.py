"""The GUI for the game battleships."""

__author__ = "7146127, Theobald"
__credits__ = "Water"
__email__ = "s7223152@cs.uni-frankfurt.de"

import tkinter as tk


class GUI:

    def main(self):
        root = tk.Tk()
        root.title("Battleships")
        root.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.main()
