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

mouseCircle = c.create_oval(190, 190, 210, 210, fill="gray")
x = 200
y = 200

mouse = Vector(200, 200)

numFood = 600
foodV = []
food = []

poisonV = []
poison = []

vehicles = []


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
        foodV.append(Vector(random.randint(0, width), random.randint(0, height)))
        food.append(c.create_oval(foodV[index].x - 4, foodV[index].y - 4, foodV[index].x + 4, foodV[index].y + 4,
                                  fill="green"))

    for index in range(1):
        poisonV.append(Vector(random.randint(0, width), random.randint(0, height)))
        poison.append(c.create_oval(poisonV[index].x - 4, poisonV[index].y - 4, poisonV[index].x + 4, poisonV[index].y +
                                    4, fill="red"))


def createVehicles():
    for index in range(5):
        vehicles.append(Vehicle(random.randint(0, width), random.randint(0, height)))


createCanvas()
createFood()
createVehicles()

while True:

    # vehicle.eat(foodV, food)
    # vehicle.eat(poisonV, poison)

    # vehicle.seek(mouse)
    for vehicle in vehicles:
        vehicle.behaviors(foodV, poisonV, food, poison)
        vehicle.update()
        vehicle.display()

    root.bind('<Motion>', motion)
    root.update_idletasks()
    root.update()

    if len(food) == 0:
        break

    time.sleep(0.001)

root.mainloop()
