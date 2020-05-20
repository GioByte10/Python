from Vector import Vector
import math


class Vehicle:

    maxSpeed = 3
    maxForce = 0.05
    r = 6
    c = None

    def __init__(self, x, y, c):
        self.position = Vector(x, y)
        self.velocity = Vector(0, -2)
        self.acceleration = Vector(0, 0)
        self.c = c
        r = Vehicle.r
        self.points = [[x, y - r * 2], [x - r, y + r * 2], [x + r, y + r * 2], [x, y - r * 2]]
        self.vehicle = Vehicle.c.create_oval(295, 295, 305, 305, fill="black")
        self.x = x
        self.y = y


    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)

        self.velocity.setLimit(Vehicle.maxSpeed)

        self.acceleration.mult(0)


    def applyForce(self, force):
        self.acceleration.add(force)


    def seek(self, target):
        desired = Vector.sSub(target, self.position)
        desired.setMag(Vehicle.maxSpeed)

        steer = Vector.sSub(desired, self.velocity)
        steer.setLimit(self.maxForce)

        self.applyForce(steer)


    def display(self):
        x = self.position.x
        y = self.position.y

        theta = self.velocity.heading() + math.pi / 2
        center = (x, y)

        # self.rotate(theta, center)
        Vehicle.c.move(self.vehicle, x - self.x, y - self.y)

        self.x += x - self.x
        self.y += y - self.y


    def rotate(self, theta, center):
        cos_val = math.cos(theta)
        sin_val = math.sin(theta)
        cx, cy = center
        new_points = []

        for x_old, y_old in self.points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])

        new2points = []

        for pair in new_points:
            for coordinates in pair:
                new2points.append(coordinates)

        Vehicle.c.coords(self.vehicle, new2points)
