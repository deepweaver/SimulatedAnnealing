from random import random, gauss 
from math import exp
def cost(x):
    return x*x*x*x + x * x * x + x * x + x 

def neighbor(x):
    return x + gauss(0,1)
    # return x + random() - 0.5

def acceptance_probability(old_cost, new_cost, T):
    return exp(-(new_cost - old_cost) / T)
# if new_cost < old_cost, probability of adopting this point is ap > 1
# if new_cost > old_cost, probability of adopting this point is ap < 1
# with T getting smaller, the probability of this alg taking changes is decreasing

def anneal(solution):
    old_cost = cost(solution)
    T = 1.0
    T_min = 0.0001
    alpha = 0.9
    while T > T_min:
        for _ in range(100):
            new_solution = neighbor(solution)
            new_cost = cost(new_solution)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random():
                solution = new_solution
                old_cost = new_cost
        T *= alpha 
    return solution, old_cost

if __name__ == "__main__":
    print(anneal(-2))