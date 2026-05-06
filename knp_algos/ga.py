import random
from .evaluate import evaluate

def genetic_algorithm(values, weights, capacity, pop_size=20, generations=50, mutation_rate=0.1):
    n = len(values)
    
    population = [[random.randint(0, 1) for _ in range(n)] for _ in range(pop_size)]
    
    for _ in range(generations):
        fitness = [evaluate(ind, values, weights, capacity) for ind in population]
        
        new_population = []
        for _ in range(pop_size):
            i, j = random.sample(range(pop_size), 2)
            winner = population[i] if fitness[i] > fitness[j] else population[j]
            new_population.append(winner[:])
        
        for i in range(0, pop_size, 2):
            if random.random() < 0.8:
                point = random.randint(1, n - 1)
                new_population[i][point:], new_population[i+1][point:] = \
                    new_population[i+1][point:], new_population[i][point:]
        
        for i in range(pop_size):
            if random.random() < mutation_rate:
                idx = random.randint(0, n - 1)
                new_population[i][idx] = 1 - new_population[i][idx]
        
        population = new_population

    best_ind = max(population, key=lambda ind: evaluate(ind, values, weights, capacity))
    return best_ind, evaluate(best_ind, values, weights, capacity)
