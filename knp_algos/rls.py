import random
from .evaluate import evaluate

def randomized_local_search(values, weights, capacity, initial_solution=None):
    n = len(values)
    if initial_solution is None:
        solution = [random.randint(0, 1) for _ in range(n)]
    else:
        solution = initial_solution[:]

    for _ in range(50):
        i = random.randint(0, n - 1)
        new = solution[:]
        new[i] = 1 - new[i]

        if evaluate(new, values, weights, capacity) > evaluate(solution, values, weights, capacity):
            solution = new

    return solution, evaluate(solution, values, weights, capacity)
