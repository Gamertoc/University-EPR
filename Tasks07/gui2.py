from tkinter import *
from dialog import Dialog, messagebox
import tkinter as tk

from Spray import Game

active = '#c92d02'
default_color = '#4787d6'


class CreateGameDialog(Dialog):
    def initialize(self, frame):
        self.grid_size = 5

        Label(frame, text="Grid Size:").grid(row=0)

        self.e1 = Scale(frame, from_=self.grid_size, to=25, orient=HORIZONTAL)
        self.e1.grid(row=0, column=1)

        return self.e1

    def validate(self):
        try:
            self.values.clear()
            self.values.append(int(self.e1.get()))
        except ValueError:
            messagebox.showwarning(
                "Bad input",
                "Illegal values, please try again")
            return False

        return True

    def apply(self):
        self.grid_size = self.values[0]


class PlaceShipsDialog(Dialog):
    def initialize(self, frame, grid_size=10, min_players=2):
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
        print(ship)
        return True

    def buttonbox(self):
        if(self.box is not None):
            self.box.destroy()

        self.box = Frame(self)

        ok_btn = Button(self.box, text="Next Player", width=10,
                        command=self.next_cmd, default=ACTIVE)
        ok_btn.pack(side=LEFT, padx=5, pady=5)

        finish_btn = Button(self.box, text="Ready",
                            state=DISABLED, width=10, default=ACTIVE)
        if self.num_players >= self.min_players - 1:
            finish_btn.config(state="normal")
        finish_btn.pack(side=LEFT, padx=5, pady=5)

        cancel_btn = Button(self.box, text="Cancel",
                            width=10, command=self.cancel)
        cancel_btn.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Escape>", self.cancel)

        self.box.pack()

    def next_cmd(self):
        self.num_players += 1
        self.e1.delete(0, END)
        self.buttonbox()
        self.e1.focus_set()
        self.e2.reset()

    def validate(self):
        return True

    def apply(self):
        pass


class PlayerGrid:
    def __init__(self, parent, column=0, row=0,
                 text='', color='blue', width=10, height=10):
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
        frame = Frame(self.parent, padx=10, pady=10, bg=self.color)
        frame.grid(row=self.row, column=self.column, sticky='nsew')
        grid = Frame(frame)
        grid.grid(sticky='nsew', column=self.column, columnspan=2)
        label = Label(self.parent, text=self.text)
        label.grid(row=self.row + 1, column=self.column)

        for x in range(self.width):
            Grid.columnconfigure(frame, x, weight=1)
            for y in range(self.height):
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
        button = self.grid[coord]
        button['bg'] = active
        button['activebackground'] = active

    def remove_selection(self, coord):
        button = self.grid[coord]
        button['bg'] = default_color
        button['activebackground'] = '#38dcf5'


class ShipSelectGrid(PlayerGrid):
    def __init__(self, parent, on_ship=None, **kwargs):
        PlayerGrid.__init__(self, parent, **kwargs)
        self.on_ship = on_ship
        self._selection_buttons = []
        self._selection = None
        self.ships = []
        self._ship_blocks = []
        self.reset()

    def click(self, button, coord):
        if coord in self._ship_blocks:
            return

        if self._selection is None:
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
        if self._selection is None:
            return

        mx, my = coord
        sx, sy = self._selection

        def sign(a): return (a > 0) - (a < 0)
        diffx = abs(mx - sx)
        signx = sign(mx - sx)
        diffy = abs(my - sy)
        signy = sign(my - sy)

        for coord in self._selection_buttons:
            self.remove_selection(coord)

        self._selection_buttons.clear()
        self.add_selection(self._selection)
        self._selection_buttons.append(self._selection)

        if diffx > 0 and diffy > 0:
            return

        if diffx > 0:
            currentx = sx + signx
            while currentx != mx + signx:
                coord = (currentx, sy)
                if coord in self._ship_blocks:
                    break
                self.add_selection(coord)
                self._selection_buttons.append(coord)
                currentx += signx
        elif diffy > 0:
            currenty = sy + signy
            while currenty != my + signy:
                coord = (sx, currenty)
                if coord in self._ship_blocks:
                    break
                self.add_selection(coord)
                self._selection_buttons.append(coord)
                currenty += signy

    def reset(self):
        for coord in self.grid.keys():
            self.remove_selection(coord)
        self._selection_buttons.clear()
        self._selection = None
        self.ships.clear()
        self._ship_blocks.clear()


class GUI:
    def __init__(self):
        root = Tk()
        self.root = root
        self.game = Game()

        root.title('Battleships')
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        self._create_menu()
        self._create_intro()

        self.player_grid = PlayerGrid(self.root,
                                      column=0,
                                      row=0,
                                      text="",
                                      color="blue")

    def loop(self):
        tk.mainloop()

    def _create_menu(self):
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
        optionmenu.add_command(label='All Ships Attack', command=nothereyet)
        menubar.add_cascade(label='Options', menu=optionmenu)

        # Help dropdown menu
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help Index', command=nothereyet)
        helpmenu.add_command(label='About...', command=nothereyet)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.root.config(menu=menubar)

    def _create_intro(self):
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
        dialog = CreateGameDialog(self.root, "New Game")
        players_dialog = PlaceShipsDialog(
            self.root, title="Add Player", grid_size=dialog.grid_size)


def main():
    g = GUI()
    g.loop()
    # menu settings frame, display options in extra window
    # settings_frame = Frame(root, pady=20)
    # settings_frame.title = 'Settings'
    # settings_frame.grid(row=2, column=0, columnspan=5, sticky='nsew')

    # intro

    # # game options
    # options_label = Label(settings_frame, text='Options')
    # options_label.grid(row=2, column=0)

    # # radio button for scatter shot
    # var1 = IntVar()
    # option1 = Checkbutton(settings_frame, text='scattershot', variable=var1)
    # option1.grid(row=3, column=0)

    # # radio button for all ships shoot
    # var2 = IntVar()
    # option2 = Checkbutton(settings_frame, text='all ships attack', variable=var2)
    # option2.grid(row=4, column=0)

    # # scale for gamefieldsize
    # gfs = Scale(settings_frame, from_=5, to=25, orient=HORIZONTAL)
    # gfs.grid(row=3, column=1)
    # btn_1 = Button(settings_frame, text='Confirm fieldsize',
    #                command=lambda: print(gfs.get()))
    # btn_1.grid(row=2, column=1)

    # # scale for numberofplayers
    # nop = Scale(settings_frame, from_=2, to=4, orient=HORIZONTAL)
    # nop.grid(row=3, column=2)
    # btn_1 = Button(settings_frame, text='Confirm number of players',
    #                command=lambda: print(nop.get()))
    # btn_1.grid(row=2, column=2)

    # # name entry
    # e_player = Entry(root)
    # e_player.grid(row=3, column=0)
    # # ready next player
    # ready_button = Button(root, text='enter player name')
    # ready_button.grid(row=3, column=1)

    # current player ships
    # player_frame = Frame(root, padx=10, pady=10, bg='blue')
    # player_frame.grid(row=0, column=0, sticky='nsew')
    # player_grid = Frame(player_frame)
    # player_grid.grid(sticky='nsew', column=0, columnspan=2)
    # player_label = Label(root, text='Current Player')
    # player_label.grid(row=1, column=0)

    # for x in range(width):
    #     Grid.columnconfigure(player_frame, x, weight=1)

    #     for y in range(height):
    #         Grid.rowconfigure(player_frame, y, weight=1)
    #         btn = Button(player_frame, bg=default_color,
    #                      activebackground='#38dcf5')
    #         btn.grid(column=x, row=y, sticky='nsew')
    #         btn['command'] = lambda x=btn: click(x)

    # # next turn / player
    # turn_button = Button(root, text='switch field', command=switchfield)
    # turn_button.grid(row=0, column=2)

    # # enemy field, shoot here
    # enemy_frame = Frame(root, padx=10, pady=10, bg='red')
    # enemy_frame.grid(row=0, column=3, sticky='nsew')
    # enemy_grid = Frame(enemy_frame)
    # enemy_grid.grid(sticky='nsew', column=3, columnspan=2)
    # enemy_label = Label(root, text='Enemy Player')
    # enemy_label.grid(row=1, column=3)

    # for x in range(width):
    #     Grid.columnconfigure(enemy_frame, x, weight=1)

    #     for y in range(height):
    #         Grid.rowconfigure(enemy_frame, y, weight=1)
    #         btn = Button(enemy_frame, bg=default_color,
    #                      activebackground='#38dcf5')
    #         btn.grid(column=x, row=y, sticky='nsew')
    #         btn['command'] = lambda x=btn: click(x)


def show_help():
    pass


def open_settings():
    pass


def var_states():
    print(var1.get(), var2.get())


def switchfield():
    pass


def nothereyet():
    pass


if __name__ == "__main__":
    main()
