"""
    Advent of Code 2022, Day 10     🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
import matplotlib.pyplot as plt


def readData(infile : str) -> list:
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    return data


def part1(data : list) -> int:
    x = 1
    cycle = 0
    signal_strength = 0
    for line in data:
        cycle += 1
        line = line.split(' ')
        if  cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength += cycle * x
        if len(line) == 2:
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strength += cycle * x
            x += int(line[1])
    return signal_strength


def part2(data):
    CRT = []
    x = 1
    cycle = 0
    for line in data:
        cycle += 1
        CRT.append((x) <= (cycle%40) <= (x+2))

        line = line.split(' ')
        if len(line) == 2:
            cycle += 1
            CRT.append((x) <= (cycle%40) <= (x+2))
            x += int(line[1])

    CRT = np.array(CRT).reshape([-1, 40])
    plt.imshow(CRT)
    plt.show()

    return "see picca"


if __name__=='__main__':
    data = readData('../Data/day10')
    print(data)

    print("part 1:", part1(data))
    print("part 2:", part2(data))