from Vector import Vector
import math
import random


class Vehicle:

    maxSpeed = 2
    maxForce = 0.05
    r = 6
    c = None

    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(0, -2)
        self.acceleration = Vector(0, 0)
        r = Vehicle.r
        self.points = [[x, y - r * 2], [x - r, y + r * 2], [x + r, y + r * 2], [x, y - r * 2]]
        self.vehicle = Vehicle.c.create_oval(x - 5, y - 5, x + 5, y + 5, fill="gray")
        self.x = x
        self.y = y

        self.dna = [0, 0]
        self.dna[0] = 5
        self.dna[1] = -0.01
        self.foodLine = Vehicle.c.create_line(300, 10, 300 + self.dna[0] * 50, 10, fill="green")
        self.poisonLine = Vehicle.c.create_line(300, 20, 300 + self.dna[1] * 50, 20, fill="red")

        print("Food steer: " + str(self.dna[0]) + "     Poison steer: " + str(self.dna[1]))


    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)

        self.velocity.setLimit(Vehicle.maxSpeed)

        self.acceleration.mult(0)


    def eat(self, listV, list):
        x = self.position.x
        y = self.position.y

        distance = 3000
        closestIndex = -1

        for index in range(len(listV)):
            d = math.dist([x, y], [listV[index].x, listV[index].y])
            if d < distance:
                distance = d
                closestIndex = index

        if distance < 5:
            Vehicle.c.delete(list[closestIndex])
            list.remove(list[closestIndex])
            listV.remove(listV[closestIndex])

        elif closestIndex > -1:
            return self.seek(listV[closestIndex])

        return Vector(0, 0)


    def applyForce(self, force):
        self.acceleration.add(force)


    def behaviors(self, goodV, badV, good, bad):
        steerG = self.eat(goodV, good)
        steerB = self.eat(badV, bad)

        steerG.mult(self.dna[0])
        steerB.mult(self.dna[1])

        self.applyForce(steerG)
        self.applyForce(steerB)


    def seek(self, target):
        desired = Vector.sSub(target, self.position)
        desired.setMag(Vehicle.maxSpeed)

        steer = Vector.sSub(desired, self.velocity)
        steer.setLimit(self.maxForce)

        return steer

        # self.applyForce(steer)


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
