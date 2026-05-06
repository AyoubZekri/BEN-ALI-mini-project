import math
import random
from .total_distance import total_distance

def simulated_annealing(cities):
    route = list(cities.keys())
    random.shuffle(route)

    T = 1000
    alpha = 0.995
    best = route[:]

    while T > 1:
        i, j = random.sample(range(len(route)), 2)
        new_route = route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]

        delta = total_distance(new_route, cities) - total_distance(route, cities)

        if delta < 0 or random.random() < math.exp(-delta / T):
            route = new_route

            if total_distance(route, cities) < total_distance(best, cities):
                best = route[:]

        T *= alpha

    return best
