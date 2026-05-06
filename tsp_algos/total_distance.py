from .distance import distance

def total_distance(route, cities):
    dist = 0
    for i in range(len(route)):
        current = route[i]
        next_city = route[(i + 1) % len(route)]
        dist += distance(current, next_city, cities)
    return dist
