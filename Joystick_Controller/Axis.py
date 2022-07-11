import pygame
from tkinter import *
import time

root = Tk()
root.geometry('1920x720')
c = Canvas(root, height=720, width=1920, bg="white")

c.pack()

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CONTROL')

pygame.display.update()

gameExit = False

lead_x = 0
lead_y = 0

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

    if event.type == pygame.JOYAXISMOTION:
        lead_x += int(joysticks[-1].get_axis(0) * 4.5)
        lead_y += int(joysticks[-1].get_axis(1) * 4.5)

    c.create_polygon(lead_x, lead_y, lead_x + 6, lead_y + 10.5, lead_x + 18, lead_y + 10.5, lead_x + 24, lead_y, lead_x + 18, lead_y - 10.5, lead_x + 6, lead_y - 10.5,
                     fill="white", outline="black")

    root.update_idletasks()
    root.update()

    # print("X: " + str(lead_x) + "  Y: " + str(lead_y))
