# F = ma   a = F/m   m = F/a  1 lbs = 4.448 N

print("Welcome to the weight of the worlds")
print("You can choose the planets already recorded, create your own, or the free mode\n")
print("Instructions:\nPress z to exit from any mode\nLeave empty for values you want to find\n")


def check(string):
    if len(string) > 0:
        if string == 'z':
            return False
        else:
            return float(string)
    else:
        return -1


def evaluate(gravityA, mass, force, lbs, sForce):
    line = ""

    if gravityA == -1:
        gravityA = force / mass
        line += "a = " + str(force) + " N / " + str(mass) + " kg = " + str(gravityA) + " m/s²\n"
        line += "m = " + str(mass) + " kg\n" + sForce


    elif mass == -1:
        mass = force / gravityA
        line += "a = " + str(gravityA) + " m/s²\n"
        line += "m = " + str(force) + " N / " + str(gravityA) + " m/s² = " + str(mass) + " kg\n"
        line += sForce

    elif force == -1:
        force = mass * gravityA
        lbs = force / 4.448
        line += "a = " + " m/s²\nm = " + str(mass) + " kg\n"
        line += "F = " + str(mass) + " kg * " + str(gravityA) + " m/s² = " + str(force) + " N\n"
        line += "F = " + str(force) + " N / 4.448 N = " + str(lbs) + " lbs\n"


    print(line)


def planet(gravityA, freeMode):

    while True:

        sForce = ""

        if freeMode:
            gravityA = check(input("Acceleration (m/s²) = "))
            if not gravityA:
                return 0

        else:
            print("Acceleration (m/s²) = " + str(gravityA))

        mass = check(input("Mass (kg) = "))
        if not mass:
            return 0

        force = check(input("Force (N) = "))
        if not force:
            return 0

        lbs = check(input("Force (lbs) = "))
        if not lbs:
            return 0

        print('\n')

        if force != -1:
            lbs = force / 4.448
            sForce += "Force = " + str(force) + " N\n"
            sForce += "Force = " + str(force) + " N / 4.448 N = " + str(lbs) + " lbs\n"

        elif lbs != -1:
            force = lbs * 4.448
            sForce += "Force = " + str(lbs) + " lbs * 4.448 N = " + str(force) + " N\n"
            sForce += "Force = " + str(lbs) + " lbs\n"

        if (mass == -1 and gravityA == -1) or (mass == -1 and force == -1) or (gravityA == -1 and force == -1):
            print("There is no enough information\n")
        else:
            evaluate(gravityA, mass, force, lbs, sForce)


while True:
    print("1.- Free mode\n")
    print("2.- Create your own\n")
    print("3.- Earth\na = 9.81 m/s²\n")
    print("4.- Moon\na = 1.62 m/s²\n")
    print("5.- Venus\na = 8.87 m/s²\n")
    print("6.- Mars\na = 3.72 m/s²\n")

    option = int(input("Option #"))

    if option == 1:
        planet(0, True)
    else:
        if option == 2:
            planet(float(input("Acceleration (m/s²) = ")), False)

        elif option == 3:
            planet(9.81, False)

        elif option == 4:
            planet(1.62, False)

        elif option == 5:
            planet(8.87, False)

        elif option == 6:
            planet(3.72, False)
