# put your python code here

multiples = []
summ = 0

brange = int(input())
trange = int(input())

for i in range(brange, trange + 1, 1):
    if i % 3 == 0:
        multiples.append(i)

for n in multiples:
    summ += n

mean = summ / len(multiples)

print(mean)
