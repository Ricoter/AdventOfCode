"""
    Advent of Code 2022, Day 3     🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""

import numpy as np


def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    return data


def overlap(a : str, b : str) -> chr:
    return list(set(a) & set(b))[0]


def priority(c : chr) -> int:
    if c.isupper(): 
        val = ord(c) - ord('A') + 27
    else:
        val = ord(c) - ord('a') + 1
    return val


def part1(data):
    priorities = 0
    for line in data:
        l = len(line)//2
        a, b = line[:l], line[-l:]
        priorities += priority(overlap(a, b))
    return priorities


def part2(data):
    priorities = 0
    data = np.array(data).reshape(-1, 3)
    for a, b, c in data:
        priorities += priority(list(set(a) & set(b) & set(c))[0])
    return priorities


if __name__=='__main__':
    data = readData('../Data/day03')
    # print(data)

    print("part 1:", part1(data))
    print("part 2:", part2(data))