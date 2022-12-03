"""
    Advent of Code 2022, Day 3     🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np


def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    return np.array(data)


def overlap(a : str, b : str) -> chr:
    return (set(a) & set(b)).pop()


def overlap3(a : str, b : str, c : str) -> chr:
    return (set(a) & set(b) & set(c)).pop()


def priority(c : chr) -> int:
    if c.isupper(): 
        value = ord(c) - ord('A') + 27
    else:
        value = ord(c) - ord('a') + 1
    return value


def part1(data):
    priorities = 0
    for line in data:
        l = len(line)//2
        a, b = line[:l], line[-l:]
        priorities += priority(overlap(a, b))
    return priorities


def part2(data):
    data = data.reshape(-1, 3)
    priorities = 0
    for a, b, c in data:
        priorities += priority(overlap3(a, b, c))
    return priorities


if __name__=='__main__':
    data = readData('../Data/day03')
    # print(data)

    print("part 1:", part1(data))
    print("part 2:", part2(data))