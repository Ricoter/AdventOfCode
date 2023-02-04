"""
    Advent of Code 2022, Day 4     🎄🎄🎄🎄
    Python v3.10.6
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
            line = line.strip()
            line = re.split(r"[A-z]| |:|\.", line)
            # n, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs  
            line = [x for x in line if x != '']
            data.append(line)
    return data


def part1(data : list) -> int:
    
    return


def part2(data : NotImplemented) -> NotImplemented:
    return 


if __name__=='__main__':
    tic = time()
    data = readData('../Data/day19t')
    print("data:", data, "\ntime:", tic-time())

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', tic-time())
    tic = time()
    print("part 2:", part2(data), 'time:', tic-time())