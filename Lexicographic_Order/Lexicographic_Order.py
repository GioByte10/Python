# https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering

values = [1, 2, 3, 4, 5, 6, 7, 8]
toReverse = []


def swap(item1, item2):
    temp = values[item1]
    values[item1] = values[item2]
    values[item2] = temp


print(str(values))


def lexOrder():
    while True:

        largestI = -1
        for i in range(len(values) - 1):
            if values[i] < values[i + 1]:
                largestI = i

        if largestI == -1:
            break

        largestJ = -1
        for j in range(len(values)):
            if values[largestI] < values[j]:
                largestJ = j

        if largestJ == -1:
            break

        # print("Largest I: " + str(largestI) + "  Largest J:" + str(largestJ))

        swap(largestI, largestJ)
        # print("Swapped Values: " + str(values))

        toReverse = []

        for i in range(len(values) - largestI - 1):
            item = values[i + largestI + 1]
            toReverse.append(item)

        for item in toReverse:
            values.remove(item)

        # print("To Reverse: " + str(toReverse))

        toReverse.reverse()

        for item in toReverse:
            values.append(item)

        print(str(values))
        # print()


lexOrder()
