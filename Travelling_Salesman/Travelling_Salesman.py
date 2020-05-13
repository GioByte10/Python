from tkinter import *
from Lexicographic_Order import nextLexOrder
import math
import random
import time

root = Tk()
c = Canvas(root, height=600, width=800, bg="black")
line = c.create_line(0, 0, 0, 0, width=2 / 2, fill="white")
bestLine = c.create_line(0, 0, 0, 0, width=15 / 2, fill="purple")
actual = c.create_text(200, 20, text="", fill="white", font=1)
best = c.create_text(200, 50, text="", fill="purple", font=1)

width = int(c.cget("width"))
height = int(c.cget("height"))

numCities = 9
cities = []
order = []

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
        order.append(city)


def track():
    path = []

    for i in range(len(cities)):
        path.append(cities[order[i]][0])
        path.append(cities[order[i]][1])

    c.coords(line, path)

    path = []

    for city in bestPath:
        path.append(city[0])
        path.append(city[1])

    c.coords(bestLine, path)

    root.update_idletasks()
    root.update()


def calcDistance():
    sum = 0
    for city in range(len(cities) - 1):
        sum += math.dist(cities[order[city]], cities[order[city + 1]])

    return sum


createCanvas()
createCities()

lowestDistance = calcDistance()
print(lowestDistance)
print(order)

bestPath = cities.copy()
c.itemconfig(actual, text=str(order) + " " + str(int(lowestDistance)))
c.itemconfig(best, text=str(order) + " " + str(int(lowestDistance)))
track()
# time.sleep(5)

for i in range(math.factorial(numCities) - 1):

    order = nextLexOrder(order)

    d = calcDistance()
    if d < lowestDistance:
        lowestDistance = d
        bestPath = []
        for j in range(len(cities)):
            bestPath.append(cities[order[j]])
        c.itemconfig(best, text=str(order) + " " + str(int(lowestDistance)))

    c.itemconfig(actual, text=str(order) + " " + str(int(d)))
    track()

    root.update_idletasks()
    root.update()
    # time.sleep(3)

root.mainloop()
