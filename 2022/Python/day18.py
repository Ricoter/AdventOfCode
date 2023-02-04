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

def readData(infile : str) -> list:
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            line = re.split(r",", line)
            line = [int(x) for x in line]
            data.append(line)
    return data


def d_manhattan(a, b):
    return sum([abs(a[i] - b[i]) for i in range(len(a))]) 

def part1(data : list) -> int:
    pixels = len(data)
    sides = pixels * 6
    for i, a in enumerate(data):
        for b in data[i+1:]:
            if d_manhattan(a, b) == 1:
                sides -= 2
    return sides

def adjacent(x,y,z):
    return (x+1, y, z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)

def floodfill(droplets:list) -> int:
    score = 0
    upper_limit = np.max(np.array(droplets)) + 2
    lower_limit = np.min(np.array(droplets)) - 2
    to_visit = [(lower_limit, lower_limit, lower_limit)]
    for c in to_visit:
        neighbours = [x for x in adjacent(*c) if (upper_limit not in x) and (lower_limit not in x)]
        to_visit += [x for x in neighbours if (x not in to_visit) and (x not in droplets)]
        score += sum([1 for x in neighbours if x in droplets])
    return score


def part2(data : list) -> int:
    data = [tuple(x) for x in data]
    return floodfill(data)


if __name__=='__main__':
    tic = time()
    data = readData('../Data/day18')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    # print("part 1:", part1(deepcopy(data)), 'time:', time()-tic)
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic) # < 3218