from .evaluate import evaluate

def local_search_first(values, weights, capacity):
    n = len(values)
    solution = [0] * n
    improved = True

    while improved:
        improved = False
        for i in range(n):
            new = solution[:]
            new[i] = 1 - new[i]

            if evaluate(new, values, weights, capacity) > evaluate(solution, values, weights, capacity):
                solution = new
                improved = True
                break

    return solution, evaluate(solution, values, weights, capacity)
