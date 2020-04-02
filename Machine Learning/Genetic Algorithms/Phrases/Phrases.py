import time
from DNA import DNA
from Population import Population

mutation = 0.01
cases = 1
generations = 0
power = 1

print("Welcome to Natural Selected Phrases        Mutation Rate = " + str(mutation * 100) + "%")
members = int(input("Enter a population: "))
target = input("Enter a target: ")

for num in range(cases):

    population = Population(members, target, mutation, power)
    dna = DNA(population)

    dna.generateDNA()

    while not population.endb:

        population.generateFitness()
        population.generateMatingPool()
        population.nextGeneration()

    generations += population.generations

print("\n\n")
print(str(cases) + " tested")
print("It took an average of " + str(generations / cases) + " generations per case")
print("Using the phrase \"" + target + "\" which have a length of " + str(len(target)) + " and a population of " + str(members))
print("A fitness factor of n^" + str(power) + "   Mutation rate of " + str(mutation * 100))
