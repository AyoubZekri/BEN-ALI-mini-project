import random
from .evaluate import evaluate

def random_solution(values, weights, capacity):
    n = len(values)
    solution = [random.randint(0, 1) for _ in range(n)]
    return solution, evaluate(solution, values, weights, capacity)
