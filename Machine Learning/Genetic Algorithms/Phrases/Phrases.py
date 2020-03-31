from DNA import DNA
from Population import Population

mutation = 0.01

print("Welcome to Natural Selected Phrases        Mutation Rate = " + str(mutation * 100) + "%")
members = int(input("Enter a population: "))
target = input("Enter a target: ")

population = Population(members, target, mutation)
dna = DNA(population)

dna.generateDNA()


while not population.endb:

    population.generateFitness()
    population.generateMatingPool()
    population.nextGeneration()



