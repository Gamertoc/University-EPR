from tkinter import *
import tkinter as tk
from Spray import Game

active = '#c92d02'
default_color = '#4787d6'


def main(height, width):
    root = Tk()
    root.title('Battleships')
    # menubar for dropdown menus
    menubar = Menu(root)

    game = Game()

    # Game dropdown menu
    gamemenu = Menu(menubar, tearoff = 0)
    gamemenu.add_command(label='New Game', command=lambda: game.start_game())
    gamemenu.add_command(label='Settings', command=nothereyet)
    gamemenu.add_separator()
    gamemenu.add_command(label='Exit', command=root.quit)
    menubar.add_cascade(label='Game', menu=gamemenu)

    # Options dropdown menu
    optionmenu = Menu(menubar, tearoff=0)
    optionmenu.add_command(label='Scattershot', command=nothereyet)
    optionmenu.add_command(label='All Ships Attack', command=nothereyet)
    menubar.add_cascade(label='Options', menu=optionmenu)

    # Help dropdown menu
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label='Help Index', command=nothereyet)
    helpmenu.add_command(label='About...', command=nothereyet)
    menubar.add_cascade(label='Help', menu=helpmenu)

    root.config(menu = menubar)

    # menu settings frame, display options in extra window
    settings_frame = Frame(root, pady=20)
    settings_frame.title = 'Settings'
    settings_frame.grid(row=2, column=0, columnspan=5, sticky='nsew')
    
    # intro
    var = StringVar()
    intro = Message(settings_frame, textvariable=var, relief=RAISED, justify=LEFT)
    var.set('Intro : \nA game of battleships.\nWhoever sinks all enemy ships, wins.\
        \nStart the game through the menu.')
    intro.grid(row=0, column=0, columnspan=2)

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
    # ready_button = Button(root, text='enter player name', command=addplayer)
    # ready_button.grid(row=3, column=1)

    # current player ships
    player_frame = Frame(root, padx=10, pady=10, bg='blue')
    player_frame.grid(row=0, column=0, sticky='nsew')
    player_grid = Frame(player_frame)
    player_grid.grid(sticky='nsew', column=0, columnspan=2)
    player_label = Label(root, text='Current Player')
    player_label.grid(row=1, column=0)

    for x in range(width):
        Grid.columnconfigure(player_frame, x, weight=1)

        for y in range(height):
            Grid.rowconfigure(player_frame, y, weight=1)
            btn = Button(player_frame, bg=default_color,
                         activebackground='#38dcf5')
            btn.grid(column=x, row=y, sticky='nsew')
            btn['command'] = lambda x=btn: click(x)

    # next turn / player
    turn_button = Button(root, text='switch field', command=switchfield)
    turn_button.grid(row=0, column=2)

    # enemy field, shoot here
    enemy_frame = Frame(root, padx=10, pady=10, bg='red')
    enemy_frame.grid(row=0, column=3, sticky='nsew')
    enemy_grid = Frame(enemy_frame)
    enemy_grid.grid(sticky='nsew', column=3, columnspan=2)
    enemy_label = Label(root, text='Enemy Player')
    enemy_label.grid(row=1, column=3)

    for x in range(width):
        Grid.columnconfigure(enemy_frame, x, weight=1)

        for y in range(height):
            Grid.rowconfigure(enemy_frame, y, weight=1)
            btn = Button(enemy_frame, bg=default_color,
                         activebackground='#38dcf5')
            btn.grid(column=x, row=y, sticky='nsew')
            btn['command'] = lambda x=btn: click(x)

    mainloop()


def click(button):
    if(button['bg'] == active):
        button['bg'] = default_color
        button['activebackground'] = '#38dcf5'
    else:
        button['bg'] = active
        button['activebackground'] = active


def show_help():
    pass


def var_states():
   print(var1.get(), var2.get())


# def addplayer():
#     pass

def switchfield():
    pass


def nothereyet():
    pass


main(10, 10)
