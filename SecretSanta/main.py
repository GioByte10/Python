from random import randint, shuffle

people = []
emails = []
messages = []

temp = list(zip(people, emails, messages))
shuffle(temp)
people, emails, messages = zip(*temp)

print(people)
print(emails)
print(messages)

for i in range(len(people)):
    print(people[i - 1] + " -> " + people[i])




