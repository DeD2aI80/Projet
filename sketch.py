
from Population import Population


neurons = 10
layers = [5,neurons,1]

pop = Population(100, layers, mutation = 0.05)


for i in range(500):
    pop.doGeneration()
    print i, pop.fitness

