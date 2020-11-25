# Write your code here
money = 550
water = 400
milk = 540
beans = 120
cups = 9

WATER_ESPRESSO = 250
BEANS_ESPRESSO = 16
COST_ESPRESSO = 4

WATER_LATTE = 350
MILK_LATTE = 75
BEANS_LATTE = 20
COST_LATTE = 7

WATER_CAPPUCCINO = 200
MILK_CAPPUCCINO = 100
BEANS_CAPPUCCINO = 12
COST_CAPPUCCINO = 6


def checkCups(neededWater, neededMilk, neededBeans, cups):
    minimum = water // neededWater

    if neededMilk != 0 and milk // neededMilk < minimum:
        minimum = milk // neededMilk

    elif beans // neededBeans < minimum:
        minimum = beans // neededBeans

    if minimum == cups:
        return "Yes, I can make that amount of coffee"

    elif minimum > cups:
        return "Yes, I can make that amount of coffee (and even " + str(minimum - cups) + " more than that)"

    elif minimum < cups:
        return "No, I can make only " + str(minimum) + " cups of coffee"


def display():
    print("The coffee machine has:")
    print(str(water) + " ml of water")
    print(str(milk) + " ml of milk")
    print(str(beans) + " gr of coffee beans")
    print(str(cups) + " disposable cups")
    print(str(money) + "$ of money")


def latte():
    global water, milk, beans, cups, money
    water -= WATER_LATTE
    milk -= MILK_LATTE
    beans -= BEANS_LATTE
    money += COST_LATTE
    cups -= 1


def espresso():
    global water, milk, beans, cups, money
    water -= WATER_ESPRESSO
    beans -= BEANS_ESPRESSO
    money += COST_ESPRESSO
    cups -= 1


def cappuccino():
    global water, milk, beans, cups, money
    water -= WATER_CAPPUCCINO
    milk -= MILK_CAPPUCCINO
    beans -= BEANS_CAPPUCCINO
    money += COST_CAPPUCCINO
    cups -= 1


def buy():
    print("What do you want to buy?")
    coffee = int(input("1.- Espresso\n2.- Latte\n3.- Cappuccino\n"))

    if coffee == 1:
        espresso()

    elif coffee == 2:
        latte()

    elif coffee == 3:
        cappuccino()

    display()


def fill():
    global water, milk, beans, cups

    waterToAdd = int(input("Write how many ml of water do you want to add: "))
    milkToAdd = int(input("Write how many ml of milk do you want to add: "))
    beansToAdd = int(input("Write how many grams of beans do you want to add: "))
    cupsToAdd = int(input("Write how many disposable cups of coffee do you want to add: "))

    water += waterToAdd
    milk += milkToAdd
    beans += beansToAdd
    cups += cupsToAdd

    display()


def take():
    global money
    print("I gave you " + str(money) + "$")

    money = 0

    display()


display()
option = input("Write action (buy, fill, take): ")

if option == "buy":
    buy()

elif option == "fill":
    fill()

elif option == "take":
    take()

else:
    print("Not a valid option")
