water = int(input("Write how much milliliters of water the machine has: "))
milk = int(input("Write how much milliliters of milk the machine has: "))
beans = int(input("Write how much grams of coffee beans the machine has: "))
cups = int(input("Write how much cups the machine has: "))
money = int(input("How much money do you have? $"))

print("\nWhat would you like to purchase? (Input number.)")
print("1. Espresso $4")
print("2. Latte ($7)")
print("3. Cappuccino ($6)")
drink = int(input("Coffee Type: "))


def success():
    print("\nRight away!")


def fail():
    print("\nUnfortunately, I cannot make that amount of coffee. Please get more resources or money.")


def espressoCheck():
    if water >= 250 and beans >= 16 and money >= 4 and cups >= 1:
        success()
    else:
        fail()


def latteCheck():
    if water >= 350 and milk >= 75 and beans >= 20 and money >= 7 and cups >= 1:
        success()
    else:
        fail()


def cappuccinoCheck():
    if water >= 200 and milk >= 100 and beans >= 12 and money >= 6 and cups >= 1:
        success()
    else:
        fail()


if drink == 1:
    espressoCheck()

if drink == 2:
    latteCheck()

if drink == 3:
    cappuccinoCheck()
