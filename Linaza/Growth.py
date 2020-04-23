plant = input("Plant #: ")
final = int(input("Final growth:"))

for num in range(6):
    growth = pow(final + 1, (num + 1) * 0.1666) - 1
    print("Day " + str(num + 1) + ":  " + str(growth))
