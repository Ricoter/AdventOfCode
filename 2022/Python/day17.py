"""
    Advent of Code 2022, Day 4     🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time
import matplotlib.pyplot as plt

def DEFINE_XY_ROCKSHAPES():
    global XY_ROCKSHAPES

    # Visual patterns
    rockshape_patterns = [
        np.array([['#','#','#','#']]),

        np.array([['.','#','.'],
                  ['#','#','#'],
                  ['.','#','.']]),

        np.array([['#','#','#'],
                  ['.','.','#'],
                  ['.','.','#']]),

        np.array([['#'],
                  ['#'],
                  ['#'],
                  ['#']]),

        np.array([['#','#'],
                  ['#','#']])
    ]

    # Convert to indices
    XY_ROCKSHAPES = []
    for A in rockshape_patterns:
        XY = np.where(A=='#')
        XY = XY[0], XY[1]+2 # left edge is two units away from the left wall
        XY_ROCKSHAPES.append(XY)


def readData(infile : str) -> list:
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            for c in line:
                if c == '<':
                    data.append(-1)
                elif c == '>':
                    data.append(1)
    return data


def overlap(C_cave, X_rock, Y_rock):
    """ Checks if new rock overlaps upper (margin) rocks in the cave """
    C_rock = zip(X_rock, Y_rock)
    return sum([(c in C_cave) for c in C_rock]) > 0


def move_sideways(direction, X, Y, C_cave = [[], []]):
    if direction == -1:
        if (np.min(Y) > 0) and not overlap(C_cave, X, Y-1):
            Y -= 1
    elif (np.max(Y) < 6) and not overlap(C_cave, X, Y+1):
        Y += 1
    return Y



def part1(pattern : list) -> int:
    """Naive solution using index arrays for rock positions"""
    # pattern = np.array(pattern)
    pi = 0  # pattern index
    top = 0 # top coordinate of cave
    XX, YY = np.array([]).astype(int), np.array([]).astype(int)

    for i in range(2022):
        margin = 100
        C_cave = set(zip(XX[-margin:],YY[-margin:]))
        # get the shape of the next rock
        X, Y = deepcopy(XY_ROCKSHAPES[i%5])
        # print(XY_ROCKSHAPES[0])
        # roll first 4 times
        for _ in range(4):
            d = pattern[pi]             # current gas direction
            pi = (pi + 1) % len(pattern)# update pattern index
            Y = move_sideways(d, X, Y)  # move sideways

        X += top # Set the new rock on the proper hight 

        # Fall down
        while True:
            # Botton
            if np.min(X) <= 0:
                break
            
            # Try to move down
            if overlap(C_cave, X-1, Y):
                break
            else:
                X -= 1

            d = pattern[pi]             # current gas direction
            pi = (pi + 1) % len(pattern)# update pattern index

            Y = move_sideways(d, X, Y, C_cave=C_cave)

        XX = np.array([*XX, *X])
        YY = np.array([*YY, *Y])
        top = np.max(XX) + 1
    #     if top % 1000 == 0:
    #         print(top, XX)
    # grid = np.zeros((max(XX)+1, max(YY)+1))
    # grid[(XX,YY)] = 1
    # print(grid)
    return top

class hyperjump:
    def __init__(self, n_iterations : int):
        self.n_iterations = n_iterations
        self.visited_states = []
        self.visited_scores = []
        self.current_index = 0
        self.has_jumped = 0

    def add_state(self, state : any, current_index : int, current_score):
        if self.has_jumped == 0:
            if state in self.visited_states:
                previous_index = self.visited_states.index(state) #
                previous_score = self.visited_scored[previous_index] #
                cycle_length = current_index - previous_index #
                print("hyperjump at:", current_index, "with cycle length:", cycle_length)
                iterations_left = self.n_iterations - (current_index + 1) #
                n_cycles = iterations_left // cycle_length
                d_score = n_cycles * (current_score - previous_score)

                i += n_cycles * cycle_length # hyper jump
                self.has_jumped = True

def part2(pattern : NotImplemented) -> NotImplemented:
    # pattern = np.array(pattern)
    pi = 0  # pattern index
    top = 0 # top coordinate of cave
    d_top = 0
    XX, YY = np.array([]).astype(int), np.array([]).astype(int)

    visited_states = []
    visited_tops = []
    i = 0
    has_jumped = False
    N = int(1e12)
    N = 2022
    while i < N:
        margin = 100
        C_cave = set(zip(XX[-margin:],YY[-margin:]))

        if has_jumped == False:
            # collect all variables for this loop
            state = (i%5, pi, (XX[-margin:]-top).tobytes(),YY[-margin:].tobytes())
            # state = hash(state)
            if state in visited_states:
                index_previous_state = visited_states.index(state) #
                previous_top = visited_tops[index_previous_state] #
                cycle_length = i - index_previous_state #
                print("hyperjump at:", i, cycle_length)
                rocks_left = N - (i + 1) #
                N_jumps = rocks_left // cycle_length
                d_top = N_jumps * (top - previous_top)

                i += N_jumps * cycle_length # hyper jump
                # print(i, N_jumps, d_top)
                has_jumped = True
            else:
                visited_states.append(state)
                visited_tops.append(top)

        # get the shape of the next rock
        X, Y = deepcopy(XY_ROCKSHAPES[i%5])

        # roll first 4 times
        for _ in range(4):
            d = pattern[pi]             # current gas direction
            pi = (pi + 1) % len(pattern)# update pattern index
            Y = move_sideways(d, X, Y)  # move sideways

        X += top # Set the new rock on the proper hight 

        # Fall down
        while True:
            # Botton
            if np.min(X) <= 0:
                break
            
            # Try to move down
            if overlap(C_cave, X-1, Y):
                break
            else:
                X -= 1

            d = pattern[pi]             # current gas direction
            pi = (pi + 1) % len(pattern)# update pattern index

            Y = move_sideways(d, X, Y, C_cave=C_cave)

        XX = np.array([*XX, *X])
        YY = np.array([*YY, *Y])
        top = np.max(XX) + 1
        i += 1
        # if top % 1000 == 0:
        #     print(top, XX)
    # grid = np.zeros((max(XX)+1, max(YY)+1))
    # grid[(XX,YY)] = 1
    # print(grid)
    return top #+ d_top - 1



if __name__=='__main__':
    data = readData('../Data/day17t')
    # print(data)

    DEFINE_XY_ROCKSHAPES()

    tic = time()
    print("part 1:", part1(data), '--> time:', time() - tic)
    tic = time()
    print("part 2:", part2(data), '--> time:', time() - tic)