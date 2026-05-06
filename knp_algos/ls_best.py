from .evaluate import evaluate

def local_search_best(values, weights, capacity):
    n = len(values)
    solution = [0] * n
    improved = True

    while improved:
        improved = False
        best = solution

        for i in range(n):
            new = solution[:]
            new[i] = 1 - new[i]

            if evaluate(new, values, weights, capacity) > evaluate(best, values, weights, capacity):
                best = new

        if evaluate(best, values, weights, capacity) > evaluate(solution, values, weights, capacity):
            solution = best
            improved = True

    return solution, evaluate(solution, values, weights, capacity)
