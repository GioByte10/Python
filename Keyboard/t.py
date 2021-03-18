import random
import time
from pynput.keyboard import Controller

keyboard = Controller()

time.sleep(3)


def type(string):



    for character in string:
        keyboard.type(character)
        delay = 0.01
        time.sleep(delay)




type("""
    # vehicle.eat(foodV, food)
    # vehicle.eat(poisonV, poison)

    # vehicle.seek(mouse)
    for vehicle in vehicles:
        vehicle.boundaries()
        vehicle.behaviors(foodV, poisonV, food, poison)
        vehicle.update()
        vehicle.display()

        newVehicle = vehicle.clone()
        if newVehicle is not None:
            vehicles.append(newVehicle)

    root.bind('<Motion>', motion)
    root.update_idletasks()
    root.update()

    for vehicle in vehicles:
        if vehicle.dead():
            Vehicle.c.delete(vehicle.vehicle)
            vehicle.deleteIndicators()

            foodV.append(Vector(vehicle.position.x, vehicle.position.y))
            food.append(
                c.create_oval(foodV[len(foodV) - 1].x - 4, foodV[len(foodV) - 1].y - 4, foodV[len(foodV) - 1].x + 4,
                              foodV[len(foodV) - 1].y + 4,
                              fill="green"))

            toRemove.append(vehicle)

    for vehicle in toRemove:
        vehicles.remove(vehicle)

    toRemove = []

    if random.random() < 0.03:
        foodV.append(Vector(random.randint(0, width), random.randint(0, height)))
        food.append(c.create_oval(foodV[len(foodV) - 1].x - 4, foodV[len(foodV) - 1].y - 4, foodV[len(foodV) - 1].x + 4,
                                  foodV[len(foodV) - 1].y + 4,
                                  fill="green"))

    if random.random() < 0.005:
        poisonV.append(Vector(random.randint(0, width), random.randint(0, height)))
        poison.append(c.create_oval(poisonV[len(poisonV) - 1].x - 4, poisonV[len(poisonV) - 1].y - 4,
                                    poisonV[len(poisonV) - 1].x + 4, poisonV[len(poisonV) - 1].y + 4,
                                    fill="red"))

    # time.sleep(0.001)

root.mainloop()

""")

