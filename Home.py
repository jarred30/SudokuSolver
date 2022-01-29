import tkinter as tk
import pygame as pg


# About module
def about():
    about_window = tk.Tk()
    about_window.geometry("600x600")
    about_label = tk.Label(about_window,
                           text="This game was designed by Jarred.")
    about_button = tk.Button(about_window,
                             fg="blue",
                             text="Go back to home.",
                             bg="white",
                             width=50,
                             height=3,
                             command=lambda: (about_window.destroy(), home())
                             )
    about_label.pack()
    about_button.pack()


# New Sudoku Game
def solver():
    def grid():
        for i in range(0, 810, 90):
            for j in range(0, 810, 90):
                pg.draw.polygon(game_window, square_color, [(i, j), (i, j + 85), (i + 85, j + 85), (i + 85, j)])

    pg.init()
    game_window = pg.display.set_mode((810, 810))
    square_color = (255, 255, 255)
    screen_color = (0, 0, 0)
    run = True
    while run:
        game_window.fill(screen_color)
        grid()
        pg.display.update()



# Home Setup
def home():
    home_window = tk.Tk()
    home_window.geometry("600x600")
    welcome = tk.Label(
        text="Welcome!\n\nThis is a python based Sudoku puzzle solver. Have fun!\n"
    )
    new_game = tk.Button(home_window,
                         text="Press to open puzzle solver",
                         fg="blue",
                         bg="white",
                         width=50,
                         height=3,
                         command=lambda: (home_window.destroy(), solver())
                         )
    about_button = tk.Button(home_window,
                             text="About",
                             fg="blue",
                             bg="white",
                             width=50,
                             height=3,
                             command=lambda: (home_window.destroy(), about())
                             )
    close_button = tk.Button(home_window,
                             text="Close Game",
                             fg="blue",
                             bg="white",
                             width=50,
                             height=3,
                             command=lambda: home_window.destroy()
                             )
    welcome.pack()
    new_game.pack()
    about_button.pack()
    close_button.pack()
    home_window.mainloop()


# Start program
home()
