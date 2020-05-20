from tkinter import*
from Vehicle import Vehicle
from Vector import Vector
import time


root = Tk()
c = Canvas(root, height=600, width=600, bg="white")
Vehicle.c = c

mouseCircle = c.create_oval(190, 190, 210, 210, fill="gray")
x = 200
y = 200

mouse = Vector(200, 200)


def createCanvas():
    root.geometry('600x600')
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

vehicle = Vehicle(300, 300, c)

while True:

    vehicle.seek(mouse)
    vehicle.update()
    vehicle.display()

    root.bind('<Motion>', motion)
    root.update_idletasks()
    root.update()

    time.sleep(0.005)

