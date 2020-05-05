from tkinter import *

path = [55, 85, 155, 85, 105, 180, 30, 2]

root = Tk()
root.geometry("400x250+300+300")
canvas = Canvas(root, height=600, width=600, bg="white")
canvas.create_line(15, 25, 200, 25)
canvas.create_line(300, 35, 300, 200, dash=(1, 2))
canvas.create_line(path)
canvas.create_oval(30, 30, 40, 40, fill="black", outline="black")
canvas.pack(fill=BOTH, expand=1)
root.mainloop()
