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
        self.updateMagnitude()

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.updateMagnitude()

    def mult(self, times):
        self.x *= times
        self.y *= times
        self.magnitude *= times

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

    def normalize(self):
        self.x /= self.magnitude
        self.y /= self.magnitude
        self.magnitude /= self.magnitude

    def heading(self):
        return math.atan(self.y / self.x)

    def updateMagnitude(self):
        self.magnitude = math.sqrt(pow(self.x, 2) + pow(self.y, 2))


    @staticmethod
    def sSub(vector1, vector2):
        return Vector(vector1.x - vector2.x, vector1.y - vector2.y)