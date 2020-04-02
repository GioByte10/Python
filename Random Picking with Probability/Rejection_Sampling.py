import random

probabilities = [0] * 100
maxValue = 100

for num in range(100):
    probabilities[num] = num + 1


def acceptReject():
    while True:
        selectedNum = random.randint(0, len(probabilities) - 1)
        selected = probabilities[selectedNum]
        rand = random.randint(1, maxValue)

        if rand < selected:
            return selected


for num in range(100):
    print(acceptReject())
