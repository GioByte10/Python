from Vector import Vector
import math


class Vehicle:

    maxSpeed = 1
    maxForce = 0.05
    r = 6
    c = None

    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(0, -2)
        self.acceleration = Vector(0, 0)

        self.vehicle = Vehicle.c.create_oval(x - 5, y - 5, x + 5, y + 5, fill="gray")
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
