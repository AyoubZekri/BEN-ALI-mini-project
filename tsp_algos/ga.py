import random
from .total_distance import total_distance

def genetic_algorithm(cities, pop_size=20, generations=100, mutation_rate=0.2):
    city_ids = list(cities.keys())
    n = len(city_ids)
    
    population = []
    for _ in range(pop_size):
        ind = city_ids[:]
        random.shuffle(ind)
        population.append(ind)
    
    for _ in range(generations):
        fitness = [total_distance(ind, cities) for ind in population]
        new_population = []
        for _ in range(pop_size):
            i, j = random.sample(range(pop_size), 2)
            winner = population[i] if fitness[i] < fitness[j] else population[j]
            new_population.append(winner[:])
        
        for i in range(0, pop_size, 2):
            if random.random() < 0.7:
                p1, p2 = new_population[i], new_population[i+1]
                start, end = sorted(random.sample(range(n), 2))
                
                def ox(parent1, parent2):
                    child = [None] * n
                    child[start:end] = parent1[start:end]
                    ptr = end
                    for city in parent2:
                        if city not in child:
                            if ptr >= n: ptr = 0
                            child[ptr] = city
                            ptr += 1
                    return child

                new_population[i] = ox(p1, p2)
                new_population[i+1] = ox(p2, p1)
        
        for i in range(pop_size):
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(n), 2)
                new_population[i][idx1], new_population[i][idx2] = \
                    new_population[i][idx2], new_population[i][idx1]
        
        population = new_population

    best_ind = min(population, key=lambda ind: total_distance(ind, cities))
    return best_ind, total_distance(best_ind, cities)
