from tsp_algos.total_distance import total_distance
from tsp_algos.greedy import greedy_deterministic, greedy_randomized
from tsp_algos.ls import local_search_first, local_search_best
from tsp_algos.ils import iterative_local_search
from tsp_algos.sa import simulated_annealing
from tsp_algos.tabu import tabu_search
from tsp_algos.rls import randomized_local_search
from tsp_algos.grasp import grasp
from tsp_algos.ga import genetic_algorithm

class TSPSolver:
    def __init__(self, cities):
        self.cities = cities

    def run_all(self):
        c = self.cities
        print("\n=== TSP RESULTS (Modular) ===\n")

        g = greedy_deterministic(c)
        print("Greedy:", g, total_distance(g, c))

        gr = greedy_randomized(c)
        print("Randomized Greedy:", gr, total_distance(gr, c))

        lf = local_search_first(g[:], c)
        print("Local First:", lf, total_distance(lf, c))

        lb = local_search_best(g[:], c)
        print("Local Best:", lb, total_distance(lb, c))

        ils = iterative_local_search(c)
        print("ILS:", ils, total_distance(ils, c))

        sa = simulated_annealing(c)
        print("SA:", sa, total_distance(sa, c))

        ts = tabu_search(c)
        print("Tabu:", ts, total_distance(ts, c))

        rls = randomized_local_search(c)
        print("Random LS:", rls, total_distance(rls, c))

        grs = grasp(c)
        print("GRASP:", grs, total_distance(grs, c))

        ga_route, ga_dist = genetic_algorithm(c)
        print("GA:", ga_route, ga_dist)

if __name__ == "__main__":
    cities_data = {
        0: (0, 0),
        1: (1, 5),
        2: (5, 2),
        3: (6, 6),
        4: (8, 3)
    }
    
    solver = TSPSolver(cities_data)
    solver.run_all()