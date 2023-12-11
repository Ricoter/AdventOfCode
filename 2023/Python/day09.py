"""
    Advent of Code 2023, Day 9     🎄🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.12
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time


def readData(infile : str) -> list:
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip().split()
            line = [int(x) for x in line]
            data.append(line)
    return data


def recursive_predictor(x : np.array) -> int:
    last = x[-1]
    dx = x[1:] - x[:-1]
    if np.any(dx != 0):
        d = recursive_predictor(dx) 
        print(last, d)
        return last + d
    else:
        return last

def part1(data : list) -> int:

    return sum([recursive_predictor(np.array(x)) for x in data])


def part2(data : list) -> int:
    return sum([recursive_predictor(np.array(x[::-1])) for x in data])



if __name__=='__main__':
    tic = time()
    data = readData('../Data/day09')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', time()-tic)
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic)