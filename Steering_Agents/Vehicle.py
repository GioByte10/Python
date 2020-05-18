from Vector import Vector
import math


class Vehicle:

    maxSpeed = 4
    maxForce = 0.1
    r = 6
    c = None

    def __init__(self, x, y, c):
        self.position = Vector(x, y)
        self.velocity = Vector(0, -2)
        self.acceleration = Vector(0, 0)
        self.c = c
        self.vehicle = c.create_polygon()

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
        steer.limit(self.maxForce)

        self.applyForce(steer)

    def display(self):
        theta = self.velocity.heading() + math.pi / 2
