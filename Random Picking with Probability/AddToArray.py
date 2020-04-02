import random
probabilities = [0] * 100
total = 0

for num in range(100):
    probabilities[num] = num
    total += probabilities[num]

toPick = [0] * total
k = 0

for index in range(len(probabilities)):
    for num in range(probabilities[index]):
        toPick[k] = probabilities[index]
        k += 1

for num in range(100):
    print(str(toPick[random.randint(0, total - 1)]))