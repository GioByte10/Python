from tkinter import *

root = Tk()
c = Canvas(root, height=400, width=400, bg="white")
rows = 5
cols = 6
grid = []


def createCanvas():
    root.geometry('400x400')
    c.pack()


createCanvas()
root.mainloop()
