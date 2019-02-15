# from SimulatedAnnealing import anneal
from random import random, gauss, randint
from copy import deepcopy
from math import exp 
n = 16
init_board = [0]*n

def printBoard(board):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print('1 ',end='')
            else:
                print('0 ',end='')
        print('\n',end='')


# printBoard(init_board,/)
def cost(board):
    cnt = 0 # conflit counter
    for i in range(n):
        for j in range(i+1,n):
            if board[i] == board[j]:
                cnt += 1
            elif abs(i-j) == abs(board[i]-board[j]):
                cnt += 1
    return cnt 

def neighbor(board):
    new_neighbor = deepcopy(board)
    new_neighbor[randint(0,n-1)] = randint(0,n-1)
    return new_neighbor
def acceptance_probability(old_cost, new_cost, T):
    return exp(-(new_cost - old_cost) / T)

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

solution, cost = anneal(init_board)
printBoard(solution)
print(cost)        
