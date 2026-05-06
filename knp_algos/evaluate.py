def evaluate(solution, values, weights, capacity):
    n = len(values)
    total_w = sum(weights[i] for i in range(n) if solution[i] == 1)
    total_v = sum(values[i] for i in range(n) if solution[i] == 1)

    if total_w > capacity:
        return 0  # غير صالح
    return total_v
