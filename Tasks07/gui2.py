from tkinter import *
import tkinter as tk

active = '#c92d02'
default_color = '#4787d6'

def main(height, width):
    root = Tk()

    # menubar with dropdown menu for game, options, help
    menubar = Menu(root)

    gamemenu = Menu(menubar, tearoff = 0)
    gamemenu.add_command(label="New Game", command = nothereyet)
    gamemenu.add_command(label = "Settings", command = nothereyet)
    gamemenu.add_separator()
    gamemenu.add_command(label = "Exit", command = root.quit)
    menubar.add_cascade(label = "Game", menu = gamemenu)

    optionmenu = Menu(menubar, tearoff=0)
    optionmenu.add_command(label = "Scattershot", command = nothereyet)
    optionmenu.add_command(label = "All Ships Attack", command = nothereyet)
    menubar.add_cascade(label = "Options", menu = optionmenu)

    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label = "Help Index", command = nothereyet)
    helpmenu.add_command(label = "About...", command = nothereyet)
    menubar.add_cascade(label = "Help", menu = helpmenu)

    root.config(menu = menubar)

    # menu settings frame, display options without dropdown menu
    settings_frame = Frame(root, pady=20)
    settings_frame.title = 'Settings'
    settings_frame.grid(row=2, column=0, columnspan=5, sticky=N+S+E+W)
    intro_label = Label(settings_frame, pady=10, padx=20, font=20,
            text='Intro : A game of battleships. Whoever sinks all enemy ships, wins.\
                \n Start the game through the menu.')
    intro_label.grid(row=0, column=0, columnspan=5)


    # help button
    help_button = Button(settings_frame, text='Help', command=show_help)
    help_button.grid(row=2, column=4)

    # game options
    options_label = Label(settings_frame, text='Options')
    options_label.grid(row=2, column=0)
    # radio button for scatter shot
    var1 = IntVar()
    option1 = Checkbutton(settings_frame, text='scattershot', variable=var1)
    option1.grid(row=3, column=0)
    # radio button for all ships shoot
    var2 = IntVar()
    option2 = Checkbutton(settings_frame, text='all ships attack', variable=var2)
    option2.grid(row=4, column=0)

    # scale for gamefieldsize
    gfs = Scale(settings_frame, from_=5, to=25, orient=HORIZONTAL)
    gfs.grid(row=3, column=1)
    btn_1 = Button(settings_frame, text='Confirm fieldsize',
                   command=lambda: print(gfs.get()))
    btn_1.grid(row=2, column=1)

    # scale for numberofplayers
    nop = Scale(settings_frame, from_=2, to=4, orient=HORIZONTAL)
    nop.grid(row=3, column=2)
    btn_1 = Button(settings_frame, text='Confirm number of players',
                   command=lambda: print(nop.get()))
    btn_1.grid(row=2, column=2)

    # current player ships
    player_frame = Frame(root, padx=10, pady=10)
    player_frame.grid(row=0, column=0, sticky=N+S+E+W)
    player_grid = Frame(player_frame)
    player_grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)

    for x in range(width):
        Grid.columnconfigure(player_frame, x, weight=1)

        for y in range(height):
            Grid.rowconfigure(player_frame, y, weight=1)
            btn = Button(player_frame, bg=default_color,
                         activebackground='#38dcf5')
            btn.grid(column=x, row=y, sticky=N+S+E+W)
            btn['command'] = lambda x=btn: click(x)

    # enemy field, shoot here
    enemy_frame = Frame(root, padx=10, pady=10)
    enemy_frame.grid(row=0, column=2, sticky=N+S+E+W)
    enemy_grid = Frame(enemy_frame)
    enemy_grid.grid(sticky=N+S+E+W, column=2, row=7, columnspan=2)

    for x in range(width):
        Grid.columnconfigure(enemy_frame, x, weight=1)

        for y in range(height):
            Grid.rowconfigure(enemy_frame, y, weight=1)
            btn = Button(enemy_frame, bg=default_color,
                         activebackground='#38dcf5')
            btn.grid(column=x, row=y, sticky=N+S+E+W)
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
    """opens the help window"""
    help_message = """Click buttons. Help yourself.
    """
    messagebox.showinfo('Help', help_message)


def var_states():
   print(var1.get(), var2.get())


def nothereyet():
    pass

main(10, 10)
