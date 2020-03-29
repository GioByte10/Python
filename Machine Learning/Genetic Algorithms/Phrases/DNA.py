import random


class DNA:

    def __init__(self, population):
        self.population = population
        self.numOfDNA = population.numOfMembers
        self.target = population.target

    def generateDNA(self):
        for index in range(self.numOfDNA):
            for num in range(len(self.target)):
                self.population.membersList[index] += self.newChar()



    def newChar(self):
        return chr(random.randint(65, 122))

