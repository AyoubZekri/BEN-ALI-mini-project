import random
from .total_distance import total_distance

def tabu_search(cities):
    route = list(cities.keys())
    random.shuffle(route)

    best = route[:]
    tabu = []

    for _ in range(100):
        neighbors = []

        for i in range(len(route)):
            for j in range(i + 1, len(route)):
                new_route = route[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]
                neighbors.append(new_route)

        neighbors.sort(key=lambda r: total_distance(r, cities))

        for candidate in neighbors:
            if candidate not in tabu:
                route = candidate
                break

        tabu.append(route)
        if len(tabu) > 10:
            tabu.pop(0)

        if total_distance(route, cities) < total_distance(best, cities):
            best = route[:]

    return best
