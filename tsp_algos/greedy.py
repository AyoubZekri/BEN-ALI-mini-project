import random
from .distance import distance

def greedy_deterministic(cities):
    unvisited = list(cities.keys())
    route = [unvisited.pop(0)]

    while unvisited:
        last = route[-1]
        next_city = min(unvisited, key=lambda c: distance(last, c, cities))
        route.append(next_city)
        unvisited.remove(next_city)

    return route

def greedy_randomized(cities, k=2):
    unvisited = list(cities.keys())
    route = [unvisited.pop(0)]

    while unvisited:
        last = route[-1]
        sorted_cities = sorted(unvisited, key=lambda c: distance(last, c, cities))
        candidates = sorted_cities[:k]
        next_city = random.choice(candidates)

        route.append(next_city)
        unvisited.remove(next_city)

    return route
