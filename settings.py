class Settings:
    """Game Menu Settings"""
    def __init__(self):
        self.title = "Sudoku Solver"
        self.screen_width = 350
        self.screen_height = 350
        self.x_position = 0
        self.y_position = 0
        self.geometry = f'{self.screen_width}x{self.screen_height}+{self.x_position}+{self.y_position}'
