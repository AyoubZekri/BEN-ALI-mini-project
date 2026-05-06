from .total_distance import total_distance

def local_search_first(route, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 1):
            for j in range(i + 1, len(route)):
                new_route = route[:]
                new_route[i:j] = reversed(route[i:j])

                if total_distance(new_route, cities) < total_distance(route, cities):
                    route = new_route
                    improved = True
                    break
            if improved:
                break
    return route

def local_search_best(route, cities):
    improved = True
    while improved:
        improved = False
        best = route

        for i in range(1, len(route) - 1):
            for j in range(i + 1, len(route)):
                new_route = route[:]
                new_route[i:j] = reversed(route[i:j])

                if total_distance(new_route, cities) < total_distance(best, cities):
                    best = new_route

        if total_distance(best, cities) < total_distance(route, cities):
            route = best
            improved = True
    return route
