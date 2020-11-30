scores = input().split()

wrong = 0
correct = 0

for answer in scores:
    if answer == "C":
        correct += 1

    else:
        wrong += 1

    if wrong == 3:
        print("Game over")
        break
else:
    print("You won")

print(correct)