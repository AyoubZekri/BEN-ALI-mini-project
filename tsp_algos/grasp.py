from .greedy import greedy_randomized
from .ls import local_search_best
from .total_distance import total_distance

def grasp(cities):
    best = None

    for _ in range(50):
        route = greedy_randomized(cities)
        route = local_search_best(route, cities)

        if best is None or total_distance(route, cities) < total_distance(best, cities):
            best = route

    return best
