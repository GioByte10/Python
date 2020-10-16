import random

probabilities = [0] * 3
probabilities[0] = 1
probabilities[1] = 3
probabilities[2] = 6
maxValue = 6

i = 0
j = 0
k = 0


def acceptReject():
    while True:
        selectedNum = random.randint(0, len(probabilities) - 1)
        selected = probabilities[selectedNum]
        rand = random.random() * maxValue

        if rand < selected:
            return selected


for num in range(10000):
    n = acceptReject()
    if n == 1:
        i += 1

    elif n == 3:
        j += 1

    elif n == 6:
        k += 1

print("A: " + str(i) + " B: " + str(j) + " C: " + str(k))
