class Spot:

    def __init__(self, row, col, height, width):
        self.x = col
        self.y = row
        self.height = height
        self.width = width
        self.g = 0
        self.h = 0
        self.f = 0
        self.square = None

        # print(str(self.x) + " " + str(self.y) + "   " + str(self.height) + " " + str(self.width))

    def show(self, c, color):
        # print("x: " + str(self.x * self.width) + " to " + str(self.x * self.width + self.width) + "  y: " + str(
        # self.y * self.height) + " to " + str(self.y * self.height + self.height))

        self.square = c.create_rectangle(self.x * self.width, self.y * self.height, self.x * self.width + self.width,
                                         self.y * self.height + self.height, fill=color)

    def print(self, c):
        c.create_text(self.x * self.width + self.width / 2, self.y * self.height + self.height / 2,
                      text=str(self.x) + ", " + str(self.y))
