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
    data = [re.split(r"-|,", line) for line in data]

    return np.array(data).astype(int)


def part1(data : np.array(int)) -> int:
    # Create and count booleans
    return sum([(x0 <= y0 and x1 >= y1) or (x0 >= y0 and x1 <= y1) for x0, x1, y0, y1 in data])


def part2(data):
    counter = 0
    for x0, x1, y0, y1 in data:
        # create lists of numbers
        x = list(range(x0, x1+1))
        y = list(range(y0, y1+1))

        # add them
        xy = x + y
        
        # check for doubles
        if len(xy) != len(set(xy)):
            counter += 1
    return counter


if __name__=='__main__':
    data = readData('../Data/day04')
    print(data)

    print("part 1:", part1(data))
    print("part 2:", part2(data))