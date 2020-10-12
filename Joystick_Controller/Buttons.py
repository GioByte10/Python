import pygame
from tkinter import*
import time

root = Tk()
root.geometry('500x500')
c = Canvas(root, height=500, width=500, bg="blue")

c.pack()

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CONTROL')

pygame.display.update()

gameExit = False

lead_x = 240
lead_y = 240

joysticks = []
clock = pygame.time.Clock()

for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Detected joystick '", joysticks[-1].get_name(), "'")

while not gameExit:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    if event.type == pygame.JOYBUTTONDOWN:
        print(event.button)
        if event.button == 3:
            if lead_y >= 10:
                lead_y -= 10

        if event.button == 0:
            if lead_y <= int(c.cget("height")) - 30:
                lead_y += 10

        if event.button == 2:
            if lead_x >= 10:
                lead_x -= 10

        if event.button == 1:
            if lead_x <= int(c.cget("width")) - 30:
                lead_x += 10

        time.sleep(0.05)

    c.create_rectangle(lead_x, lead_y, lead_x + 20, lead_y + 20)

    root.update_idletasks()
    root.update()

    print("X: " + str(lead_x) + "  Y: " + str(lead_y))
