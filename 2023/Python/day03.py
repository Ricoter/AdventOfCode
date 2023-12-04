"""
    Advent of Code 2023, Day 3     🎄🎄🎄
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
            line = line.strip()
            # line = re.split(r"=|,|:", line)
            data.append(line)

    # # split lines in chunks
    # data = [re.split(r"-|,", line) for line in data]
    # # to numpy 2D array (characterwise)
    # data = np.array([list(line) for line in data])
    # # to numpy 2D array
    # data = np.array(data)
    # data = data.astype(int)
    return data

def is_valid(i : int, positions : tuple, data : list) -> bool:
    # find square around the number
    x1 = max(i - 1, 0)
    x2 = min(i + 1, len(data) - 1)
    y1 = max(positions[0] - 1, 0)
    y2 = min(positions[1], len(data[0]) - 1)
    
    grid = np.array([list(line) for line in data])
    symbols = list(grid[x1:x2+1, y1:y2+1].flatten())
    # print(symbols)
    symbols = [s for s in symbols if s != '.' and s.isdigit() is False]
    # print(symbols)
    if symbols:
        return True
    return False

def part1(data : list) -> int:

    sum = 0
    for i, line in enumerate(data):
        # find all numbers in line and their positions in the line
        for match in re.finditer(r"\d+", line):
            n = match.group()
            position = match.span()
            # print(n, position)
            if is_valid(i, position, data):
                sum += int(n)

    return sum


def find_gear_ratio(data : list, pos)    -> list:
    # find square around the asterisk
    x1 = max(pos[0] - 1, 0)
    x2 = min(pos[0] + 1, len(data) - 1)
    y1 = max(pos[1] - 1, 0)
    y2 = min(pos[1] + 1, len(data[0]) - 1)
    # print(pos, x1, x2, y1, y2)

    # find all numbers in the adjacent squares
    numbers = []
    for x in range(x1, x2+1):

        # find all matches in line x
        for match in re.finditer(r"\d+", data[x]):
            n = match.group()       # number
            Y1 = match.span()[0]    # left position OF the number
            Y2 = match.span()[1] -1 # right position OF the number
            # print(n, Y1, Y2)

            if (y1 <= Y1 <= y2) or (y1 <= Y2 <= y2):
                numbers.append(int(n))

    # print(numbers)

    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    if len(numbers) > 2:
        return ValueError("More than 2 numbers found")

    return 0

def part2(data : list) -> int:
    sum = 0
    grid = np.array([list(line) for line in data])
    asterisks = np.where(grid == '*')
    asterisks = zip(*asterisks)
    for pos in asterisks:
        sum += find_gear_ratio(data, pos)
    return sum
 


if __name__=='__main__':
    tic = time()
    data = readData('../Data/day03')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', time()-tic)
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic)