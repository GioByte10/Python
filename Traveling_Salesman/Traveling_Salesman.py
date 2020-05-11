import math
from tkinter import *
import random

root = Tk()
c = Canvas(root, height=600, width=800, bg="black")
line = c.create_line(0, 0, 0, 0, width=2 / 2, fill="white")
bestLine = c.create_line(0, 0, 0, 0, width=15 / 2, fill="purple")

width = int(c.cget("width"))
height = int(c.cget("height"))
print(width)
print(height)

numCities = 30
cities = []

bestPath = [[0, 0], [0, 0]]


def createCanvas():
    root.geometry('800x600-400-70')
    c.pack()


def createCities():
    for row in range(numCities):
        cities.append([])

    for city in range(numCities):
        cities[city] = [random.randint(5, width - 5), random.randint(5, height - 5)]
        c.create_oval(cities[city][0] - 5, cities[city][1] - 5, cities[city][0] + 5, cities[city][1] + 5, fill="white")


def track():
    path = []

    for city in cities:
        path.append(city[0])
        path.append(city[1])

    c.coords(line, path)

    path = []

    for city in bestPath:
        path.append(city[0])
        path.append(city[1])

    c.coords(bestLine, path)


def swap(city1, city2):
    temp = cities[city1]
    cities[city1] = cities[city2]
    cities[city2] = temp


def calcDistance():
    sum = 0
    for city in range(len(cities) - 1):
        sum += math.dist(cities[city], cities[city + 1])

    return sum


createCanvas()
createCities()

lowestDistance = calcDistance()

while True:

    track()
    swap(random.randint(0, numCities - 1), random.randint(0, numCities - 1))

    d = calcDistance()
    if d < lowestDistance:
        lowestDistance = d
        bestPath = cities.copy()

    root.update_idletasks()
    root.update()


root.mainloop()
