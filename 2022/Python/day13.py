"""
    Advent of Code 2022, Day 4     🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re

def readData(infile : str) -> list:
    data = [[]]
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip('\n')
            # new pair
            if line == "":
                data.append([])
            # text to code
            else:
                data[-1].append(eval(line))
    return data


def correct_order(A, B):
    for i, a in enumerate(A):
        if i >= len(B): 
            return 0
        else:
            b = B[i]
        # print(a, b)
        
        if type(a) == type(b) == int:
            if a < b: return 1
            if a > b: return 0
        else:
            if type(a) == int:
                a = [a]
            elif type(b) == int:
                b = [b]
            x = correct_order(a, b)
            if x == None:
                continue
            else:
                return x    
    if len(A) < len(B):
        return 1
    else: 
        return None


def part1(data : list) -> int:
    count = 0
    for i, (a, b) in enumerate(data):
        count += correct_order(a, b) * (i+1)
    return count


def part2(data : list) -> int:
    data = [x for y in data for x in y] # flatten the data
    specials = [[[2]], [[6]]] # add specials
    data += specials
    # order
    for i, new in enumerate(data):
        for j in range(i):
            x = correct_order(data[j], new) 
            # print(data[j], new, x)
            if x == 0:
                data.insert(j, data.pop(i))
                break
    # find key
    key = 1
    for i, x in enumerate(data):
        if x in specials:
            key *= (i+1)
    print(data)
    return key


if __name__=='__main__':
    data = readData('../Data/day13')
    print(data)

    print("part 1:", part1(deepcopy(data)))
    print("part 2:", part2(data))