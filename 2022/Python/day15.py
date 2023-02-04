"""
    Advent of Code 2022, Day 15     🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re

def d_manhattan(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def readData(infile : str) -> list:
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            _, xs, _, ys, _,xb, _, yb = re.split(r"=|,|:", line)
            data.append([(int(xs), int(ys)), (int(xb), int(yb))])
    
    # add manhattan distance
    for i, (sensor, beacon) in enumerate(data):
        data[i].append(d_manhattan(sensor, beacon))
    return data


def search_line(data:list, Y:int=10, limit=None) -> int:
    count = 0
    
    # find touch per sensor for given y-coordinate
    touch = []    # list of x-ranges (x0, x1) on Y for each sensor
    for (sx, sy), _, r in data:
        dy = r - abs(sy - Y)
        if dy >= 0:
            touch.append((sx-dy, sx+dy))

    # sort ascending for x
    touch.sort(key=lambda x: x[0])

    # Count values that are in range of a sensor. 
    # Because 'touch' is sorted we can update te lower limit to prevent overlap
    match limit:
        case None:
            l0, l1 = touch[0][0]+1, np.inf
        case _:
            l0, l1 = limit

    for x0, x1 in touch:
        x1 += 1
        x0 = max(x0, l0) # remove overlap
        x1 = max(x1, l0) # remove overlap
        x0 = min(x0, l1) # remove overlap
        x1 = min(x1, l1) # remove overlap
        
        if x0 > l0: # part 2
            return l0*4000000 + Y

        # update    
        l0 = x1
        count += abs(x1 - x0)
    return count # part 1


def part1(data:list, Y:int) -> int:
    return search_line(data, Y=Y)


def part2(data:list, limit:tuple) -> int:
    lm = limit[1]
    for y in range(lm):
        x = search_line(data, y, limit=limit)
        if x != lm:
            return x 


if __name__=='__main__':
    infile = '../Data/day15'
    test = 0

    # variable switch for test/real input
    match test:
        case 1: 
            infile += 't'
            Y = 20
            limit = (0, 20)
        case _:
            Y = 2000000
            limit = (0, 4000000)

    data = readData(infile)
    # print(data)

    print("part 1:", part1(deepcopy(data), Y=Y))
    print("part 2:", part2(data, limit=limit))