"""
    Advent of Code 2023, Day 6     🎄🎄🎄🎄🎄🎄
    Python v3.10.12
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time


def readData(infile : str) -> list:
    with open(infile, 'r') as f:
        return [x.strip().split()[1:] for x in f]


def part1(data : list) -> int:
    " Brute force"
    product = 1
    for time, distance in zip(*data):
        time = int(time)
        distance = int(distance)
        winners = sum([1 for t in range(time) if (t * (time-t)) > distance])
        product *= winners
    return product


def part2(data : list) -> int:
    # glue the input numbers together
    time = int(str.join('', data[0]))
    distance = int(str.join('', data[1]))

    # find the first time that the distance is exceeded
    better_start = distance // time
    for t in range(better_start,time+1):
        if (t * (time-t)) > distance:
            return time - 2*t + 1 # use time symmetry

    
if __name__=='__main__':
    tic = time()
    data = readData('../Data/day06')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', time()-tic)
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic)