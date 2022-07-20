from random import shuffle

tests = 1000
n = 100
s = 0

for j in range(tests):
    boxes = []
    fail = False

    for i in range(n):
        boxes.append(i)

    shuffle(boxes)

    for prisoner in range(n):
        nextBox = prisoner

        for turn in range(int(n/2)):
            nextBox = boxes[nextBox]

            if nextBox == prisoner:
                break

            if turn == int(n/2)-1:
                fail = True
                break

        if fail:
            break

    if not fail:
        s += 1


successRate = (s/tests) * 100

print(n, "prisoners; ", tests, "test cases\n")
print("Success rate: ", successRate, "%")
