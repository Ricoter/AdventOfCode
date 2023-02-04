"""
    Advent of Code 2022, Day 12     🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re

def readData(infile : str) -> np.array:
    with open(infile, 'r') as f:
        data = [line.strip() for line in f]

    # split lines in chunks
    # data = [re.split(r"-|,", line) for line in data]

    # to numpy 2D array (characterwise)
    data = np.array([list(line) for line in data])
    return np.array(data)

def adjacent(i, j, max_i, max_j, min_i=0, min_j=0):
    i ,j = int(i), int(j)
    X = []
    if i > min_i:
        X.append((i-1, j))
    if i < max_i-1:
        X.append((i+1,j))
    if j > min_j:
        X.append((i,j-1))
    if j < max_j-1:
        X.append((i,j+1))
    return X

def part1(data : np.array) -> int:

    x = 0
    S = np.where(data == 'S')
    E = np.where(data == 'E')
    data[S] = 'a'
    data[E] = 'z'
    steps = 0
    visited = []
    nbrs = [S]
    walker = np.zeros(data.shape)
    print(walker)
    while nbrs:
        # loop over edge
        _nbrs = []
        for n in nbrs:
            visited.append(n)
            walker[n] = steps
            level = data[n][0]
            if n == E:
                # print(walker)
                return steps
            else:
                for x in adjacent(*n,*data.shape):
                    if ord(data[x]) <= (ord(level)+1):
                        _nbrs.append(x)
        # clean neighbors 
        nbrs = [x for x in set(_nbrs) if x not in visited]
        steps += 1

    return -1

def part2(data : np.array) -> int:
    S = np.where(data=='S')
    E = np.where(data=='E')
    data[S] = 'a'
    data[E] = 'z'
    steps = 0
    visited = []
    nbrs = [E]
    while nbrs:
        _nbrs = []
        for n in nbrs:
            visited.append(n)
            level = data[n][0]
            if level == 'a':
                return steps
            else:
                for x in adjacent(*n, *data.shape):
                    if ord(data[x]) >= (ord(level)-1):
                        _nbrs.append(x)
        # clean neighbors 
        nbrs = [x for x in set(_nbrs) if x not in visited]
        steps += 1

    return -1               

if __name__=='__main__':
    data = readData('../Data/day12')
    print(data)

    print("part 1:", part1(deepcopy(data)))
    print("part 2:", part2(data))