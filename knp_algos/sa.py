import random
from .evaluate import evaluate

def simulated_annealing(values, weights, capacity):
    n = len(values)
    solution = [random.randint(0, 1) for _ in range(n)]
    best = solution[:]

    T = 1000
    alpha = 0.99

    while T > 1:
        i = random.randint(0, n - 1)
        new = solution[:]
        new[i] = 1 - new[i]

        delta = evaluate(new, values, weights, capacity) - evaluate(solution, values, weights, capacity)

        if delta > 0 or random.random() < pow(2.718, delta / T):
            solution = new

            if evaluate(solution, values, weights, capacity) > evaluate(best, values, weights, capacity):
                best = solution[:]

        T *= alpha

    return best, evaluate(best, values, weights, capacity)
