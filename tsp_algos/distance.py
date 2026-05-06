import math

def distance(a_id, b_id, cities):
    a = cities[a_id]
    b = cities[b_id]
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
