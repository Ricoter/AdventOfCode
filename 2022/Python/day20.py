"""
    Advent of Code 2022, Day 20 🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time

def readData(infile : str) -> NotImplemented:
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            line = re.split(r"=|,|:", line)
            data.append(line)

    # # split lines in chunks
    # data = [re.split(r"-|,", line) for line in data]
    # # to numpy 2D array (characterwise)
    # data = np.array([list(line) for line in data])
    # # to numpy 2D array
    # data = np.array(data)
    # data = data.astype(int)
    return data


def part1(data : NotImplemented) -> NotImplemented:
    return


def part2(data : NotImplemented) -> NotImplemented:
    return 


if __name__=='__main__':
    tic = time()
    data = readData('../Data/day')
    print("data:", data, "\ntime:", tic-time())

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', tic-time())
    tic = time()
    print("part 2:", part2(data), 'time:', tic-time())