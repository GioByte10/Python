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
        char = random.randint(55, 123)
        if char >= 91:
            char += 6

        if char < 65:
            char -= 7

        if char == 123:
            char = 32

        if char == 124:
            char = 44

        if char == 125:
            char = 45

        if char == 126:
            char = 46

        if char == 127:
            char = 63

        if char == 128:
            char = 39

        if char == 129:
            char = 59

        return chr(char)



