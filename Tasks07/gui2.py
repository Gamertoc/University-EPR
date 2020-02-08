"""The Battleship GUI. This is now the main file :)"""

__author__ = "7146127, Theobald, 7040759, Schott"
__credits__ = "Water"
__email__ = "s7223152@cs.uni-frankfurt.de, s7296105@cs.uni-frankfurt.de"

from tkinter import *
from dialog import Dialog, messagebox
import tkinter as tk

from Spray import Game

active = '#c92d02'
default_color = '#4787d6'


class CreateGameDialog(Dialog):
    def initialize(self, frame):
        """Initializes main dialog frame."""
        self.grid_size = 5

        Label(frame, text="Grid Size:").grid(row=0)

        self.e1 = Scale(frame, from_=self.grid_size, to=25, orient=HORIZONTAL)
        self.e1.grid(row=0, column=1)

        return self.e1

    def validate(self):
        """Checks if input is int."""
        try:
            self.values.clear()
            self.values.append(int(self.e1.get()))
        except ValueError:
            messagebox.showwarning(
                "Bad input",
                "Illegal values, please try again.")
            return False

        return True

    def apply(self):
        """Sets grid_size to valid value."""
        self.grid_size = self.values[0]


class PlaceShipsDialog(Dialog):
    def initialize(self, frame, game=None, grid_size=10, min_players=2):
        """Dialog for ship placement."""
        self.game = game
        self.num_players = 0
        self.min_players = 2
        self.result = ""

        Label(frame, text="Enter Name:").grid(row=0)
        self.e1 = Entry(frame)
        self.e1.grid(row=0, column=1, pady=10)

        ships_frame = Frame(frame)
        ships_frame.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.e2 = ShipSelectGrid(ships_frame, row=2, text="Place Ships",
                                 width=grid_size, height=grid_size,
                                 on_ship=self.on_ship)

        return self

    def on_ship(self, ship):
        """Adds ship to game from GUI."""
        # TODO: add ship to game
        print(ship)
        return True

    def buttonbox(self):
        """Dinamicly updates buttons, depending on numbers of players added"""
        if(self.box is not None):
            self.box.destroy()

        self.box = Frame(self)

        ok_btn = Button(self.box, text="Next Player", width=10,
                        command=self.next_cmd, default=ACTIVE)
        ok_btn.pack(side=LEFT, padx=5, pady=5)

        finish_btn = Button(self.box, text="Ready",
                            state=DISABLED, width=10, default=ACTIVE)
        # ensures a minimum of 2 players
        if self.num_players >= self.min_players - 1:
            finish_btn.config(state="normal")
        finish_btn.pack(side=LEFT, padx=5, pady=5)

        cancel_btn = Button(self.box, text="Cancel",
                            width=10, command=self.cancel)
        cancel_btn.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Escape>", self.cancel)

        self.box.pack()

    def next_cmd(self):
        """Clearing inputs for next player."""
        self.num_players += 1
        self.e1.delete(0, END)
        self.buttonbox()
        self.e1.focus_set()
        self.e2.reset()

    def validate(self):
        """Validates."""
        return True

    def apply(self):
        """Currently not needed"""
        pass


class PlayerGrid:
    def __init__(self, parent, column=0, row=0,
                 text='', color='blue', width=10, height=10):
        """Sets gameboard."""
        self.parent = parent
        self.width = width
        self.height = height

        self.color = color
        self.text = text
        self.row = row
        self.column = column
        self.grid = {}
        self.frame = self.draw_grid()

    def draw_grid(self):
        """Draws game field."""
        frame = Frame(self.parent, padx=10, pady=10, bg=self.color)
        frame.grid(row=self.row, column=self.column, sticky='nsew')
        grid = Frame(frame)
        grid.grid(sticky='nsew', column=self.column, columnspan=2)
        label = Label(self.parent, text=self.text)
        label.grid(row=self.row + 1, column=self.column)

        for x in range(self.width):
        # creates the buttons in range = width
            Grid.columnconfigure(frame, x, weight=1)
            for y in range(self.height):
                # fills up in y direction
                Grid.rowconfigure(frame, y, weight=1)
                btn = Button(frame, bg=default_color,
                             activebackground='#38dcf5')
                btn.grid(column=x, row=y, sticky='nsew')
                coord = (x, y)
                btn['command'] = lambda b=btn, c=coord: self.click(b, c)
                btn.bind("<Enter>", lambda _, b=btn,
                         c=coord: self.on_hover(b, c))
                self.grid[(x, y)] = btn
        return frame

    def click(self, button, coord):
        pass

    def on_hover(self, button, coord):
        pass

    def add_selection(self, coord):
        """Activates the selected button."""
        button = self.grid[coord]
        button['bg'] = active
        button['activebackground'] = active

    def remove_selection(self, coord):
        """Deactivates the selected button."""
        button = self.grid[coord]
        button['bg'] = default_color
        button['activebackground'] = '#38dcf5'


class ShipSelectGrid(PlayerGrid):
    def __init__(self, parent, on_ship=None, **kwargs):
        """Set ships on grid."""
        PlayerGrid.__init__(self, parent, **kwargs)
        self.on_ship = on_ship
        self._selection_buttons = []
        self._selection = None
        self.ships = []
        self._ship_blocks = []
        self.reset()

    def click(self, button, coord):
        """Ships can't cross each other."""
        if coord in self._ship_blocks:
        # selection doesn't work, if grid is blocked
            return

        if self._selection is None:
        # selection works, if not selected before
            self._selection = coord
        elif self._selection == coord:
            for coord in self._selection_buttons:
                self.remove_selection(coord)
            self._selection = None
        else:
            ship = list(self._selection_buttons)
            result = True

            if self.on_ship is not None:
                result = self.on_ship(ship)

            if result:
                self.ships.append(ship)
                self._ship_blocks += ship
            else:
                for coord in self._selection_buttons:
                    self.remove_selection(coord)

            self._selection_buttons.clear()
            self._selection = None

    def on_hover(self, button, coord):
        """Reads x,y values."""
        if self._selection is None:
            return

        mx, my = coord
        sx, sy = self._selection

        def sign(a):
            """Gives the sign of an integer value."""
            return (a > 0) - (a < 0)
        
        diffx = abs(mx - sx)
        signx = sign(mx - sx)
        diffy = abs(my - sy)
        signy = sign(my - sy)

        for coord in self._selection_buttons:
            # reset selection
            self.remove_selection(coord)

        self._selection_buttons.clear()
        self.add_selection(self._selection)
        self._selection_buttons.append(self._selection)

        if diffx > 0 and diffy > 0:
            # ignore diagonals
            return

        if diffx > 0:
            # on change in x direction, add to selection
            currentx = sx + signx
            while currentx != mx + signx:
                coord = (currentx, sy)
                if coord in self._ship_blocks:
                    # don't cross ships
                    break
                self.add_selection(coord)
                self._selection_buttons.append(coord)
                currentx += signx
        elif diffy > 0:
            # on change in y direction, add to selection
            currenty = sy + signy
            while currenty != my + signy:
                coord = (sx, currenty)
                if coord in self._ship_blocks:
                    # don't cross ships
                    break
                self.add_selection(coord)
                self._selection_buttons.append(coord)
                currenty += signy

    def reset(self):
        """Resets values."""
        for coord in self.grid.keys():
            # reset all blocks to no selection
            self.remove_selection(coord)
        self._selection_buttons.clear()
        self._selection = None
        self.ships.clear()
        self._ship_blocks.clear()


class GUI:
    def __init__(self):
        """Main interface."""
        root = Tk()
        self.root = root
        self.game = Game()

        root.title('Battleships')
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        self._create_menu()
        self._create_intro()

        self.player_grid_frame = None
        self.player_grid = None
        self.create_player_grid()

    def loop(self):
        """GUI Loop"""
        tk.mainloop()

    def _create_menu(self):
        """Creates all dropdown menus."""
        menubar = Menu(self.root)
        # Game dropdown menu
        gamemenu = Menu(menubar, tearoff=0)
        gamemenu.add_command(
            label='New Game', command=self.new_game)
        gamemenu.add_separator()
        gamemenu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='Game', menu=gamemenu)

        # Options dropdown menu
        optionmenu = Menu(menubar, tearoff=0)
        optionmenu.add_command(label='Scattershot', command=self.game.spray)
        optionmenu.add_command(label='All Ships Attack', command=None)
        menubar.add_cascade(label='Options', menu=optionmenu)

        # Help dropdown menu
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help Index', command=None)
        helpmenu.add_command(label='About...', command=None)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.root.config(menu=menubar)

    def _create_intro(self):
        """Displays intro."""
        var = StringVar()
        var.set("""
Intro :
A game of battleships.Whoever sinks all enemy ships, wins.
Start the game through the menu.
        """)

        intro = Message(self.root, textvariable=var,
                        relief=RAISED, justify=LEFT)
        intro.grid(row=2, column=0, sticky='nsew')

    def new_game(self):
        """Creates Dialog for new game."""
        dialog = CreateGameDialog(self.root, "New Game")
        self.create_player_grid(dialog.grid_size)
        players_dialog = PlaceShipsDialog(
            self.root, title="Add Player", game=self.game, grid_size=dialog.grid_size)

    def create_player_grid(self, grid_size=10):
        """Display player grid."""
        if self.player_grid_frame is not None:
            self.player_grid_frame.destroy()
        self.player_grid_frame = Frame(self.root)
        self.player_grid_frame.grid_columnconfigure(0, weight=1)
        self.player_grid_frame.grid_rowconfigure(0, weight=1)
        self.player_grid_frame.grid(row=0, column=0, sticky='nsew')
        self.player_grid = PlayerGrid(self.player_grid_frame,
                                      column=0,
                                      row=0,
                                      text="",
                                      color="blue",
                                      width=grid_size,
                                      height=grid_size)

def main():
    """Main funciton."""
    g = GUI()
    g.loop()


def show_help():
    """Not implemented, not asked for"""
    pass


if __name__ == "__main__":
    main()
