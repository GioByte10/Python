from tkinter import*
from Vehicle import Vehicle


root = Tk()
c = Canvas(root, height=600, width=600, bg="white")
Vehicle.c = c


def createCanvas():
    root.geometry('600x600')
    c.pack()
