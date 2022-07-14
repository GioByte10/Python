# https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering


def swap(values, item1, item2):
    temp = values[item1]
    values[item1] = values[item2]
    values[item2] = temp


def nextLexOrder(values):

    largestI = -1
    for i in range(len(values) - 1):
        if values[i] < values[i + 1]:
            largestI = i

    largestJ = -1
    for j in range(len(values)):
        if values[largestI] < values[j]:
            largestJ = j

    swap(values, largestI, largestJ)
    toReverse = []

    for i in range(len(values) - largestI - 1):
        item = values[i + largestI + 1]
        toReverse.append(item)

    for item in toReverse:
        values.remove(item)

    toReverse.reverse()

    for item in toReverse:
        values.append(item)

    return values
