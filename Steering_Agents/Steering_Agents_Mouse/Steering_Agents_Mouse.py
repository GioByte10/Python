from tkinter import *
from Vehicle import Vehicle
from Vector import Vector
import time
import random

root = Tk()
c = Canvas(root, height=600, width=600, bg="white")

width = int(c.cget("width"))
height = int(c.cget("height"))

Vehicle.c = c

mouseCircle = c.create_oval(190, 190, 210, 210, fill="gray")
x = 200
y = 200

mouse = Vector(200, 200)

vehicle = Vehicle(300, 300)


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


createCanvas()

while True:

    vehicle.seek(mouse)
    vehicle.update()
    vehicle.display()

    root.bind('<Motion>', motion)
    root.update_idletasks()
    root.update()

    time.sleep(0.005)

root.mainloop()
