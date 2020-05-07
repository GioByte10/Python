class Cell:
    c = None
    rows = 0
    cols = 0
    width = 0
    height = 0

    def __init__(self, row, col):
        self.x = col
        self.y = row
        self.square = None

    def show(self):
        self.square = Cell.c.create_rectangle(self.x * Cell.width, self.y * Cell.height,
                                              self.x * Cell.width + Cell.width,
                                              self.y * Cell.height + Cell.height, fill="black", outline="white")
