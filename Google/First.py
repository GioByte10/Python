ph = input()

word = 0

for c in ph:
    if c == ' ':
        word += 1

print("\nThere are " + str(word + 1) + " words")
