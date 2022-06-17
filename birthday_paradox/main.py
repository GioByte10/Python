from random import randint
from statistics import median, stdev

n = input("nBabies: ")
ite = input("Number of Iterations: ")

if n.isdigit() and ite.isdigit():

    n = int(n)
    ite = int(ite)
    gMatchingBirthdays = 0
    matched = []
    matched_2 = 0
    l = 0

    for k in range(ite):

        matchingBirthdays = 0
        birthdays = [randint(1, 365) for i in range(n)]      # List comprehension :D
        # print(birthdays)

        for i in range(n - 1):
            for j in range(n - i - 1):
                # print('[' + str(birthdays[i]) + "]  [" + str(birthdays[i + j + 1]) + ']')
                if birthdays[i] == birthdays[i + j + 1]:
                    matchingBirthdays += 1
                    gMatchingBirthdays += 1
                l += 1

        print("There are " + str(matchingBirthdays) + " matching birthdays")
        matched.append(matchingBirthdays)

        if matchingBirthdays > 0:
            matched_2 += 1

    mean = gMatchingBirthdays / ite
    med = median(matched)

    print()

    print("Percentage of instances with babies sharing at least one birthday: " + str(matched_2 * 100 / ite) + '\n')
    print("Mean:            " + str(mean))
    print("Median:          " + str(med))

    if ite > 1:
        stde = stdev(matched)
        print("St Deviation:    " + str(stde))

    print(str(n) + " babies")
    print(str(ite) + " iterations")

else:
    print("Enter a valid number")


