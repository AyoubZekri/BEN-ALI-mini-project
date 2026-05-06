from .evaluate import evaluate
from .greedy import greedy
from .rls import randomized_local_search

def grasp(values, weights, capacity):
    best = None

    for _ in range(50):
        sol, _ = greedy(values, weights, capacity)
        sol, _ = randomized_local_search(values, weights, capacity, sol)

        if best is None or evaluate(sol, values, weights, capacity) > evaluate(best, values, weights, capacity):
            best = sol

    return best, evaluate(best, values, weights, capacity)
