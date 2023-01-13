import random
from scipy import special as sc

NUM_QUEENS = 8
POPULATION_SIZE = 10
MIXING_NUMBER = 2
MUTATION_RATE = 0.05

def fitnessScore(seq):
    score = 0
    for row in range(NUM_QUEENS):
        col = seq[row]
        for other_row in range(NUM_QUEENS):
            if row == other_row:
                continue
            if seq[other_row] == row:
                continue
            if other_row + seq[other_row] == row + col:
                continue
            if other_row - seq[other_row] == row - col:
                continue
            score += 1
    return score/2


