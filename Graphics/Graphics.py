from tkinter import *
import time

root = Tk()
root.geometry('300x300')
c = Canvas(root, height=300, width=300, bg="blue")
print(c.cget("height"))

c.pack()


myrectangle = c.create_rectangle(100, 100, 400, 400, fill='black')

while True:
    root.update_idletasks()
    root.update()
    time.sleep(1)
    c.itemconfig(myrectangle, fill='red')
    