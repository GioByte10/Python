import random

from DNA import DNA


class Population:

    def __init__(self, numOfMembers, target, mutation, fitnessFactor):
        self.numOfMembers = numOfMembers
        self.membersList = [""] * numOfMembers
        self.fitness = [0] * numOfMembers
        self.target = target
        self.mutation = mutation
        self.mates = 0
        self.matingPool = [0]
        self.endb = False
        self.generations = 1
        self.fitnessFactor = fitnessFactor

    def generateFitness(self):
        total = 0
        for ind in range(len(self.membersList)):
            for index in range(len(self.target)):
                if self.membersList[ind][index] == self.target[index]:
                    self.fitness[ind] += 1

            print(self.membersList[ind] + "  " + str(int((self.fitness[ind] / len(self.target)) * 100)) + "%")
            self.fitness[ind] = pow(self.fitness[ind], self.fitnessFactor)
            #  print(self.fitness[ind])
            total += self.fitness[ind]

        for ind in range(len(self.membersList)):
            self.fitness[ind] /= total

        print("\n\n\n")

    def selection(self):
        index = 0
        rand = random.random()

        while rand > 0:
            rand -= self.fitness[index]
            index += 1

        index -= 1
        return self.membersList[index]

    def nextGeneration(self):
        self.generations += 1
        for member in range(self.numOfMembers):
            parentA = self.selection()
            parentB = self.selection()
            child = self.crossover(parentA, parentB)
            child = self.mutate(child)
            self.membersList[member] = child
            if child == self.target:
                self.end(member)

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

    def end(self, member):
        members = (self.generations - 1) * self.numOfMembers
        for index in range(self.numOfMembers):
            if index <= member:
                print(self.membersList[index])
                members += 1
            else:
                break
        self.endb = True
        #print("\nIt took " + str(self.generations) + " generations to evolve, and " + str(members) + " members")

'''
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
'''

