import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.limit = 0
        self.magnitude = math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def mult(self, times):
        self.x *= times
        self.y *= times

    def setLimit(self, limit):
        self.limit = limit
        if self.magnitude > limit:
            divisor = self.magnitude / limit
            self.magnitude /= divisor
            self.x /= divisor
            self.y /= divisor


    def setMag(self, mag):
        if self.limit == 0:
            divisor = self.magnitude / mag
            self.magnitude /= divisor
            self.x /= divisor
            self.y /= divisor

        elif mag > self.limit:
            self.magnitude = mag
            self.setLimit(self.limit)

        else:
            divisor = self.magnitude / mag
            self.magnitude /= divisor
            self.x /= divisor
            self.y /= divisor

    def heading(self):
        return math.atan(self.y / self.x)


    @staticmethod
    def sSub(vector1, vector2):
        v = Vector(vector1.x - vector2.x, vector1.y - vector2.y)
        return v