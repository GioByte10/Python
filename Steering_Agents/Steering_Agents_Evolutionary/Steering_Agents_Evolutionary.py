from tkinter import *
from Vehicle import Vehicle
from Vector import Vector
import time
import random

root = Tk()
c = Canvas(root, height=600, width=600, bg="black")

width = int(c.cget("width"))
height = int(c.cget("height"))

Vehicle.c = c

Vehicle.width = width
Vehicle.height = height

mouseCircle = c.create_oval(190, 190, 210, 210, fill="gray")
x = 200
y = 200

mouse = Vector(200, 200)

numFood = 30
foodV = []
food = []

poisonV = []
poison = []

numVehicles = 15
vehicles = []
toRemove = []


def createCanvas():
    root.geometry('600x600+650+45')
    c.pack()


def motion(event):
    global x
    global y

    global mouse

    mouseX, mouseY = event.x, event.y
    c.move(mouseCircle, mouseX - x, mouseY - y)

    mouse = Vector(mouseX, mouseY)

    x += mouseX - x
    y += mouseY - y


def createFood():
    for index in range(numFood):
        foodV.append(Vector(random.randint(8, width - 8), random.randint(8, height - 8)))
        food.append(c.create_oval(foodV[index].x - 4, foodV[index].y - 4, foodV[index].x + 4, foodV[index].y + 4,
                                  fill="green"))

    for index in range(numFood):
        poisonV.append(Vector(random.randint(8, width - 8), random.randint(8, height - 8)))
        poison.append(c.create_oval(poisonV[index].x - 4, poisonV[index].y - 4, poisonV[index].x + 4, poisonV[index].y +
                                    4, fill="red"))


def createVehicles():
    for index in range(numVehicles):
        vehicles.append(Vehicle(random.randint(0, width), random.randint(0, height), None, 1000))


createCanvas()
createFood()
createVehicles()

while len(vehicles) > 0:

    # vehicle.eat(foodV, food)
    # vehicle.eat(poisonV, poison)

    # vehicle.seek(mouse)
    for vehicle in vehicles:
        vehicle.boundaries()
        vehicle.behaviors(foodV, poisonV, food, poison)
        vehicle.update()
        vehicle.display()

        newVehicle = vehicle.clone()
        if newVehicle is not None:
            vehicles.append(newVehicle)

    root.bind('<Motion>', motion)
    root.update_idletasks()
    root.update()

    for vehicle in vehicles:
        if vehicle.dead():
            Vehicle.c.delete(vehicle.vehicle)
            vehicle.deleteIndicators()

            foodV.append(Vector(vehicle.position.x, vehicle.position.y))
            food.append(
                c.create_oval(foodV[len(foodV) - 1].x - 4, foodV[len(foodV) - 1].y - 4, foodV[len(foodV) - 1].x + 4,
                              foodV[len(foodV) - 1].y + 4,
                              fill="green"))

            toRemove.append(vehicle)

    for vehicle in toRemove:
        vehicles.remove(vehicle)

    toRemove = []

    if random.random() < 0.03:
        foodV.append(Vector(random.randint(0, width), random.randint(0, height)))
        food.append(c.create_oval(foodV[len(foodV) - 1].x - 4, foodV[len(foodV) - 1].y - 4, foodV[len(foodV) - 1].x + 4,
                                  foodV[len(foodV) - 1].y + 4,
                                  fill="green"))

    if random.random() < 0.005:
        poisonV.append(Vector(random.randint(0, width), random.randint(0, height)))
        poison.append(c.create_oval(poisonV[len(poisonV) - 1].x - 4, poisonV[len(poisonV) - 1].y - 4,
                                    poisonV[len(poisonV) - 1].x + 4, poisonV[len(poisonV) - 1].y + 4,
                                    fill="red"))

    # time.sleep(0.001)

root.mainloop()
