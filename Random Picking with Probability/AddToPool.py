import random

elements = ['A', 'B', 'C']
probabilities = [0] * len(elements)
summatory = 0

for i in range(len(elements)):
    probabilities[i] = int(input("Enter the probability for element " + elements[i] + '\n'))
    summatory += probabilities[i]

print("There are " + str(summatory) + " items in the pool")
pool = [0] * summatory
k = 0

for i in range(len(elements)):
    for j in range(probabilities[i]):
        pool[k] = elements[i]
        k += 1

for i in range(10):
    print(str(pool[random.randint(0, summatory - 1)]))