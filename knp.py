from knp_algos.evaluate import evaluate
from knp_algos.greedy import greedy
from knp_algos.random_sol import random_solution
from knp_algos.ls_first import local_search_first
from knp_algos.ls_best import local_search_best
from knp_algos.sa import simulated_annealing
from knp_algos.tabu import tabu_search
from knp_algos.rls import randomized_local_search
from knp_algos.grasp import grasp
from knp_algos.ga import genetic_algorithm

class KnapsackSolver:
    def __init__(self, values, weights, capacity):
        self.values = values
        self.weights = weights
        self.capacity = capacity

    def run_all(self):
        v, w, c = self.values, self.weights, self.capacity
        print("\n=== KNAPSACK RESULTS (Modular) ===\n")
        print("Greedy:", greedy(v, w, c))
        print("Random:", random_solution(v, w, c))
        print("Local First:", local_search_first(v, w, c))
        print("Local Best:", local_search_best(v, w, c))
        print("SA:", simulated_annealing(v, w, c))
        print("Tabu:", tabu_search(v, w, c))
        print("Random LS:", randomized_local_search(v, w, c))
        print("GRASP:", grasp(v, w, c))
        print("GA:", genetic_algorithm(v, w, c))

if __name__ == "__main__":
    v = [60, 100, 120, 80, 30]
    w = [10, 20, 30, 40, 10]
    c = 60
    
    solver = KnapsackSolver(v, w, c)
    solver.run_all()
    # 