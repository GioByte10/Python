import random

toCap = input("Input a string to randomly capitalize \n")

cap = ""

for i in range(len(toCap)):
    if random.randint(0, 1) > 0:
        cap += toCap[i].capitalize()
    else:
        cap += toCap[i]

print(cap)
