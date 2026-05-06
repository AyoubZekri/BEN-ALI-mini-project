from .evaluate import evaluate

def greedy(values, weights, capacity):
    n = len(values)
    ratio = [(i, values[i] / weights[i]) for i in range(n)]
    ratio.sort(key=lambda x: x[1], reverse=True)

    solution = [0] * n
    total_w = 0

    for i, _ in ratio:
        if total_w + weights[i] <= capacity:
            solution[i] = 1
            total_w += weights[i]

    return solution, evaluate(solution, values, weights, capacity)
