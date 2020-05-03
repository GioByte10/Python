class Spot:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        print(str(self.x) + "  " + str(self.y))

    def show(self, c, width, height, row, col):
        print(str(self.x) + "  " + str(self.y) + "  " + str(row) + "  " + str(col))
        c.create_rectangle(self.x * width, self.y * height, width, height, fill="green")

