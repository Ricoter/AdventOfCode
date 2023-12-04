"""
    Advent of Code 2023, Day 4     🎄🎄🎄🎄
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
            line = re.split(r":|\|", line)
            winning_numbers = [int(x) for x in line[1].split()]
            your_numbers = [int(x) for x in line[2].split()]
            data.append([winning_numbers, your_numbers])

    # # split lines in chunks
    # data = [re.split(r"-|,", line) for line in data]
    # # to numpy 2D array (characterwise)
    # data = np.array([list(line) for line in data])
    # # to numpy 2D array
    # data = np.array(data)
    # data = data.astype(int)
    return data

def score(n):
    if n == 0:
        return 0
    return 2**(n-1)


def part1(data : list) -> int:

    sum = 0
    for winning_numbers, your_numbers in data:
        # find overlap
        overlap = set(winning_numbers).intersection(your_numbers)
        # calculate score
        sum += score(len(overlap))
        # print(overlap, score(len(overlap)), sum)
    return sum


def part2(data : list) -> int:
    card_count = np.ones(len(data))
    for i, (winning_numbers, your_numbers) in enumerate(data):
        # find overlap
        overlap = set(winning_numbers).intersection(your_numbers)
        # calculate score
        card_count[i+1 : i+1+len(overlap)] += card_count[i]

    return int(card_count.sum())


if __name__=='__main__':
    tic = time()
    data = readData('../Data/day04')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', time()-tic)
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic)