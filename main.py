from menu_screen import Menu
import tkinter as tk
from settings import Settings


# Creates tk screen
class Main:
    """Starting function for the solver"""

    def __init__(self):
        self.settings = Settings()

    def begin_solver(self):
        root = tk.Tk()
        root.geometry(self.settings.geometry)
        root.title(self.settings.title)
        Menu(root)
        root.mainloop()


# Runs the main function
if __name__ == '__main__':
    sudoku = Main()
    sudoku.begin_solver()
