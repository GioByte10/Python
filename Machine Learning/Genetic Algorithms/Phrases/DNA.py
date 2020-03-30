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

    @staticmethod
    def newChar():
        char = random.randint(55, 117)
        if char >= 91:
            char += 6

        if char < 65:
            char -= 7

        if char == 123:
            char = 32

        return chr(char)



