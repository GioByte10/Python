from Vector import Vector
import math
import random


class Vehicle:
    maxSpeed = 2
    maxForce = 0.05
    width = 0
    height = 0
    c = None
    mutationRate = 0.4

    def __init__(self, x, y, dna, health):
        self.position = Vector(x, y)
        self.velocity = Vector(0, -2)
        self.acceleration = Vector(0, 0)
        self.vehicle = Vehicle.c.create_oval(x - 5, y - 5, x + 5, y + 5, fill="gray")
        self.x = x
        self.y = y

        self.health = health

        if dna is not None:
            self.dna = [0, 0, 0, 0]

            self.dna[0] = dna[0]
            print(random.random())
            if random.random() < Vehicle.mutationRate:
                self.dna[0] += random.uniform(-0.5, 0.5)

            self.dna[1] = dna[1]
            if random.random() < Vehicle.mutationRate:
                self.dna[1] += random.uniform(-0.5, 0.5)

            self.dna[2] = dna[2]
            if random.random() < Vehicle.mutationRate:
                self.dna[2] += random.uniform(-10, 10)

            self.dna[3] = dna[3]
            if random.random() < Vehicle.mutationRate:
                self.dna[3] += random.uniform(-10, 10)

        else:
            self.dna = [0, 0, 0, 0]
            # Food Steer
            self.dna[0] = random.randint(-2, 2)
            # Poison Steer
            self.dna[1] = random.randint(-2, 2)
            # Food Perception
            self.dna[2] = random.randint(1, 100)
            # Poison Perception
            self.dna[3] = random.randint(1, 100)

        self.foodLine = Vehicle.c.create_line(x, y, x + self.dna[0] * 10, y, fill="green", width=3)
        self.poisonLine = Vehicle.c.create_line(x, y, x + self.dna[1] * 10, y, fill="red", width=2)

        self.foodPerception = Vehicle.c.create_oval(x - self.dna[2], y - self.dna[2], x + self.dna[2], y + self.dna[2],
                                                    fill="", outline="green")
        self.poisonPerception = Vehicle.c.create_oval(x - self.dna[3], y - self.dna[3], x + self.dna[3],
                                                      y + self.dna[3],
                                                      fill="", outline="red")

        # self.txtSpeed = Vehicle.c.create_text(x, y - 20, text="0", fill="white")
        self.txtFoodSteer = Vehicle.c.create_text(x, y - 40, text=str(self.dna[0]), fill="green", font=1)
        self.txtPoisonSteer = Vehicle.c.create_text(x, y - 20, text=str(self.dna[1]), fill="red", font=1)

        # print("Food steer: " + str(self.dna[0]) + "     Poison steer: " + str(self.dna[1]))

    def update(self):
        self.health -= 1

        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)

        self.velocity.setLimit(Vehicle.maxSpeed)

        self.acceleration.mult(0)

        red = int((1000 - self.health) * 0.255)
        green = int(self.health * 0.255)

        if red < 0:
            red = 0
        elif red > 255:
            red = 255

        if green > 255:
            green = 255
        elif green < 0:
            green = 0

        # print("red" + str(int((1000 - self.health) * 0.255)) + "  green:" + str(int(self.health * 0.255)))

        Vehicle.c.itemconfig(self.vehicle, fill=self.toRGB((red, green, 0)))

    def eat(self, listV, list, nutrition, perception):
        x = self.position.x
        y = self.position.y

        distance = 3000
        closestIndex = -1

        for index in range(len(listV)):
            d = math.dist([x, y], [listV[index].x, listV[index].y])
            if d < distance and d < perception:
                distance = d
                closestIndex = index

        if distance < 5:
            self.health += nutrition
            Vehicle.c.delete(list[closestIndex])
            list.remove(list[closestIndex])
            listV.remove(listV[closestIndex])

        elif closestIndex > -1:
            return self.seek(listV[closestIndex])

        return Vector(0, 0)

    def applyForce(self, force):
        self.acceleration.add(force)

    def behaviors(self, goodV, badV, good, bad):
        steerG = self.eat(goodV, good, 100, self.dna[2])
        steerB = self.eat(badV, bad, -200, self.dna[3])

        steerG.mult(self.dna[0])
        steerB.mult(self.dna[1])

        self.applyForce(steerG)
        self.applyForce(steerB)

    def seek(self, target):
        desired = Vector.sSub(target, self.position)
        desired.setMag(Vehicle.maxSpeed)

        steer = Vector.sSub(desired, self.velocity)
        steer.setLimit(Vehicle.maxForce)

        return steer

        # self.applyForce(steer)

    def display(self):
        x = self.position.x
        y = self.position.y

        # theta = self.velocity.heading() + math.pi / 2
        # center = (x, y)
        # self.rotate(theta, center)

        Vehicle.c.move(self.vehicle, x - self.x, y - self.y)
        self.updateIndicators()

        self.x += x - self.x
        self.y += y - self.y

    def updateIndicators(self):
        x = self.position.x
        y = self.position.y

        Vehicle.c.move(self.foodLine, x - self.x, y - self.y)
        Vehicle.c.move(self.poisonLine, x - self.x, y - self.y)

        Vehicle.c.move(self.foodPerception, x - self.x, y - self.y)
        Vehicle.c.move(self.poisonPerception, x - self.x, y - self.y)

        Vehicle.c.move(self.txtFoodSteer, x - self.x, y - self.y)
        Vehicle.c.move(self.txtPoisonSteer, x - self.x, y - self.y)

        # Vehicle.c.itemconfig(self.txtSpeed, text=str(self.velocity.magnitude))
        # Vehicle.c.move(self.txtSpeed, x - self.x, y - self.y)

    def deleteIndicators(self):
        Vehicle.c.delete(self.foodLine)
        Vehicle.c.delete(self.poisonLine)

        Vehicle.c.delete(self.foodPerception)
        Vehicle.c.delete(self.poisonPerception)

        Vehicle.c.delete(self.txtFoodSteer)
        Vehicle.c.delete(self.txtPoisonSteer)

        # Vehicle.c.delete(self.txtSpeed)

    def dead(self):
        return self.health < 0

    def boundaries(self):
        x = self.position.x
        y = self.position.y

        d = 25
        desired = None

        if self.position.x < d:
            desired = Vector(Vehicle.maxSpeed, self.velocity.y)

        elif self.position.x > Vehicle.width - d:
            desired = Vector(-Vehicle.maxSpeed, self.velocity.y)

        if self.position.y < d:
            desired = Vector(self.velocity.x, Vehicle.maxSpeed)

        elif self.position.y > Vehicle.height - d:
            desired = Vector(self.velocity.x, -Vehicle.maxSpeed)

        if desired is not None:
            desired.normalize()
            desired.mult(Vehicle.maxSpeed)
            steer = Vector.sSub(desired, self.velocity)
            steer.setLimit(Vehicle.maxForce)
            self.applyForce(steer)

    def clone(self):
        if random.random() < 0.0003 + self.health / 2000000:
            return Vehicle(self.position.x, self.position.y, self.dna, 500)

        else:
            return None


    @staticmethod
    def toRGB(rgb):
        return "#%02x%02x%02x" % rgb


'''
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
'''
