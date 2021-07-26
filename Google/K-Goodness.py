def getOperations(string, n, k):
    score = 0

    for i in range(n // 2):
        if string[i] == string[n - i - 1]:
            score += 1

    return abs(k - score)


import sys

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    inputs = [int(x) for x in sys.stdin.readline().split()]

    string = sys.stdin.readline()

    n = inputs[0]
    k = inputs[1]

    print("Case #" + str(i) + ": " + str(getOperations(string, n, k)))
