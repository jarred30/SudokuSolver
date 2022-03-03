import tkinter as tk
import tkinter.font as tkf
import solver_functions


class Menu:
    """This class creates the main menu for the python program"""
    def __init__(self, master=None):
        """Initializes the main menu with three buttons"""
        self.home = tk.Frame(master)
        self.welcome = tk.Label(self.home, text='Welcome to my Sudoku solving program!')
        self.new_game = tk.Button(self.home,
                                  text="Press to open puzzle solver",
                                  fg="blue",
                                  bg="white",
                                  width=50,
                                  height=3,
                                  command=lambda: (self.home.destroy(), self._solver())
                                  )
        self.about_button = tk.Button(self.home,
                                      text="About",
                                      fg="blue",
                                      bg="white",
                                      width=50,
                                      height=3,
                                      command=lambda: (self.home.destroy(), self._about())
                                      )
        self.close_button = tk.Button(self.home,
                                      text="Close Game",
                                      fg="blue",
                                      bg="white",
                                      width=50,
                                      height=3,
                                      command=lambda: quit()
                                      )
        self.welcome.pack()
        self.new_game.pack()
        self.about_button.pack()
        self.close_button.pack()
        self.welcome.pack()
        self.home.pack()

    @staticmethod
    def _about():
        """Displays the about screen"""
        about_frame = tk.Frame()
        about_label = tk.Label(about_frame,
                               text="This solver was created using Python.")
        about_button = tk.Button(about_frame,
                                 fg="blue",
                                 text="Go back to home.",
                                 bg="white",
                                 width=50,
                                 height=3,
                                 command=lambda: (about_frame.destroy(), Menu())
                                 )
        about_label.pack()
        about_button.pack()
        about_frame.pack()

    def _solver(self):
        """Solver screen setup"""
        self.entry = tk.Frame()
        self.entry.pack()
        self.matrix = []
        self._create_matrix()
        self._solver_entry()

    def _solver_entry(self):
        """Creates entry screen"""
        self._draw_matrix()
        solve = tk.Button(self.entry,
                          text="Solve",
                          fg="blue",
                          bg="white",
                          command=lambda: (_clear_solver(), self._solution())
                          )
        menu = tk.Button(self.entry,
                         text="Home",
                         fg="blue",
                         bg="white",
                         command=lambda: (self.entry.destroy(), Menu())
                         )
        clear = tk.Button(self.entry,
                          text="Clear",
                          fg="blue",
                          bg="white",
                          command=lambda: (self.entry.destroy(), self._solver())
                          )
        menu.grid(row=9, column=0, columnspan=3)
        solve.grid(row=9, column=3, columnspan=3)
        clear.grid(row=9, column=6, columnspan=3)

        def _clear_solver():
            """Clears the solver grid"""
            for i in range(0, len(self.matrix), 1):
                self.matrix[i].grid_remove()
            menu.grid_remove()
            solve.grid_remove()
            clear.grid_remove()

    def _draw_matrix(self):
        """Draws matrix"""
        counter = 0
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                self.matrix[counter].grid(column=i, row=j)
                counter = counter + 1

    def _create_matrix(self):
        """Creates matrix"""
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if (i in [0, 1, 2, 6, 7, 8] and j in [0, 1, 2, 6, 7, 8]) or (i in [3, 4, 5] and j in [3, 4, 5]):
                    field = tk.Entry(self.entry, width=3, justify='center', relief='raised', bg='white')
                else:
                    field = tk.Entry(self.entry, width=3, justify='center', relief='raised', bg='gray')
                self.matrix.append(field)

    def _solution(self):
        """Solution display"""
        _solution = str(solver_functions.solverMain(self.matrix))
        font = tkf.Font(size=20)
        solution_label = tk.Label(self.entry, text=_solution, font=font)
        back = tk.Button(self.entry,
                         text="Return to Entry",
                         fg="blue",
                         bg="white",
                         command=lambda: (solution_label.grid_remove(), back.grid_remove(), self._solver_entry())
                         )
        solution_label.grid(row=0, column=0)
        back.grid(row=2, column=0)
