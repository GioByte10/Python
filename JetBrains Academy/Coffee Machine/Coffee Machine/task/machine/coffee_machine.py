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


def checkResources(neededWater, neededMilk, neededBeans):

    missing = "Sorry not enough "

    if water < neededWater:
        missing += "water"

    if neededMilk != 0 and milk < neededMilk:
        if len(missing) > 17:
            missing += ", nor "

        missing += "milk"

    if beans < neededBeans:
        if len(missing) > 17:
            missing += ", nor "

        missing += "coffee beans"

    if cups == 0:
        if len(missing) > 17:
            missing += ", nor "

        missing += "cups"

    if len(missing) > 17:
        print(missing + '\n')
        return False

    print("I have enough resources, making you a coffee")
    return True


def display():
    print("The coffee machine has:")
    print(str(water) + " ml of water")
    print(str(milk) + " ml of milk")
    print(str(beans) + " gr of coffee beans")
    print(str(cups) + " disposable cups")
    print(str(money) + "$ of money\n")


def latte():
    if checkResources(WATER_LATTE, MILK_LATTE, BEANS_LATTE):

        global water, milk, beans, cups, money

        water -= WATER_LATTE
        milk -= MILK_LATTE
        beans -= BEANS_LATTE
        money += COST_LATTE
        cups -= 1


def espresso():
    if checkResources(WATER_ESPRESSO, 0, BEANS_ESPRESSO):

        global water, milk, beans, cups, money

        water -= WATER_ESPRESSO
        beans -= BEANS_ESPRESSO
        money += COST_ESPRESSO
        cups -= 1


def cappuccino():
    if checkResources(WATER_CAPPUCCINO, MILK_CAPPUCCINO, BEANS_CAPPUCCINO):

        global water, milk, beans, cups, money

        water -= WATER_CAPPUCCINO
        milk -= MILK_CAPPUCCINO
        beans -= BEANS_CAPPUCCINO
        money += COST_CAPPUCCINO
        cups -= 1


def buy():
    print("What do you want to buy?")
    coffee = input("1.- Espresso\n2.- Latte\n3.- Cappuccino\n\"back\" to main menu\n")

    if coffee != "back":

        coffee = int(coffee)

        if coffee == 1:
            espresso()

        elif coffee == 2:
            latte()

        elif coffee == 3:
            cappuccino()

    print()


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

    print()


def take():
    global money
    print("I gave you " + str(money) + "$\n")

    money = 0


while True:

    option = input("Write action (buy, fill, take, remaining, exit): ")

    if option == "buy":
        buy()

    elif option == "fill":
        fill()

    elif option == "take":
        take()

    elif option == "remaining":
        display()

    elif option == "exit":
        break

    else:
        print("Not a valid option\n")
