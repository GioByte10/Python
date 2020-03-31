import random

from DNA import DNA


class Population:

    def __init__(self, numOfMembers, target, mutation):
        self.numOfMembers = numOfMembers
        self.membersList = [""] * numOfMembers
        self.fitness = [0] * numOfMembers
        self.target = target
        self.mutation = mutation
        self.mates = 0
        self.matingPool = [0]
        self.endb = False
        self.generations = 1

    def generateFitness(self):
        for ind in range(len(self.membersList)):
            for index in range(len(self.target)):
                if self.membersList[ind][index] == self.target[index]:
                    self.fitness[ind] += 1
            print(self.membersList[ind] + "  " + str(int((self.fitness[ind] / len(self.target)) * 100)) + "%")
        print("\n\n\n")

    def generateMatingPool(self):
        self.mates = 0
        for num in self.fitness:
            self.mates += num

        self.matingPool = [""] * self.mates
        i = 0

        for num in range(len(self.fitness)):
            for probability in range(self.fitness[num]):
                self.matingPool[i] += self.membersList[num]
                i += 1

        self.fitness = [0] * self.numOfMembers

    def nextGeneration(self):
        self.generations += 1
        self.membersList = [""] * self.numOfMembers
        for member in range(self.numOfMembers):
            numA = random.randint(0, self.mates - 1)
            numB = random.randint(0, self.mates - 1)
            parentA = self.matingPool[numA]
            parentB = self.matingPool[numB]
            child = self.crossover(parentA, parentB)
            child = self.mutate(child)
            self.membersList[member] = child
            if child == self.target:
                self.end()

    def crossover(self, parentA, parentB):
        string = ""
        midpoint = random.randint(0, len(self.target) - 1)

        for char in range(len(self.target)):
            if char < midpoint:
                string += parentA[char]
            else:
                string += parentB[char]

        return string

    def mutate(self, child):
        string = ""
        for char in child:
            if random.randint(1, 100) <= self.mutation * 100:
                string += DNA.newChar()
            else:
                string += char

        return string

    def end(self):
        members = (self.generations - 1) * self.numOfMembers
        for index in range(self.numOfMembers):
            if self.membersList[index] != "":
                print(self.membersList[index])
                members += 1
            else:
                break
        self.endb = True
        print("\nIt took " + str(self.generations) + " generations to evolve, and " + str(members) + " members")
