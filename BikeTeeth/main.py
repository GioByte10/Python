gears = [28, 24, 21, 19, 17, 15, 13]
crankset = [48, 38, 28]

nickname = [31, 32, 33, 34, 35, 36, 37, 21, 22, 23, 24, 25, 26, 27, 11, 12, 13, 14, 15, 16, 17]
invalid = [14, 15, 16, 17, 31, 32, 33, 34]
relations = []

for crank in crankset:
    for gear in gears:
        relations.append(crank / gear)

pack = list(zip(nickname, relations))

for i in invalid:
    index = nickname.index(i)
    nickname.pop(index)
    relations.pop(index)
    pack.pop(index)

pack = sorted(pack, key=lambda x: x[1])

nickname, relations = zip(*pack)
print(nickname)

for i, name in enumerate(nickname):
    print(str(name) + "  " + str(relations[i]))



