from .evaluate import evaluate

def tabu_search(values, weights, capacity):
    n = len(values)
    solution = [0] * n
    best = solution[:]
    tabu = []

    for _ in range(100):
        neighbors = []

        for i in range(n):
            new = solution[:]
            new[i] = 1 - new[i]
            neighbors.append(new)

        neighbors.sort(key=lambda x: evaluate(x, values, weights, capacity), reverse=True)

        for candidate in neighbors:
            if candidate not in tabu:
                solution = candidate
                break

        tabu.append(solution)
        if len(tabu) > 10:
            tabu.pop(0)

        if evaluate(solution, values, weights, capacity) > evaluate(best, values, weights, capacity):
            best = solution[:]

    return best, evaluate(best, values, weights, capacity)
