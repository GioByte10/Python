import random

probabilities = [0] * 100
prob = [0] * 100
total = 0

for num in range(100):
    probabilities[num] = num + 1
    total += probabilities[num]

for num in range(100):
    prob[num] = probabilities[num] / total


def pickOne():
    index = 0
    rand = random.random()

    while rand > 0:
        rand -= prob[index]
        index += 1

    index -= 1
    return probabilities[index]


for num in range(100):
    print(pickOne())
