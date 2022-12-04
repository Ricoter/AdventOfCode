"""
    Advent of Code 2022, Day 4     🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
import re

def readData(infile : str) -> np.array(int):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]

    # split lines in chunks
    # data = [re.split(r"-|,", line) for line in data]

    # to numpy 2D array (characterwise)
    # data = np.array([list(line) for line in data]).astype(int)
    return np.array(data).astype(int)


def part1(data):
    return


def part2(data):
    return 


if __name__=='__main__':
    data = readData('../Data/day02')
    print(data)

    print("part 1:", part1(data))
    print("part 2:", part2(data))