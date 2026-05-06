import random
from .greedy import greedy_deterministic
from .ls import local_search_best
from .total_distance import total_distance

def iterative_local_search(cities):
    route = greedy_deterministic(cities)
    best = local_search_best(route, cities)

    for _ in range(10):
        new_route = best[:]
        i, j = random.sample(range(len(route)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]

        new_route = local_search_best(new_route, cities)

        if total_distance(new_route, cities) < total_distance(best, cities):
            best = new_route

    return best
