import random
from .total_distance import total_distance

def randomized_local_search(cities):
    route = list(cities.keys())
    random.shuffle(route)

    for _ in range(50):
        i, j = random.sample(range(len(route)), 2)
        new_route = route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]

        if total_distance(new_route, cities) < total_distance(route, cities):
            route = new_route

    return route
