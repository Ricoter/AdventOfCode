"""
    Advent of Code 2023, Day 8     🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.12
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time


def readData(infile : str) -> tuple:
    map = {}
    with open(infile, 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                LR_instruction = line.strip()
            elif i > 1:
                line = line.strip()
                a, b1, b2, _ = re.split(r"\ \=\ \(|, |\)", line)
                map[a] = [b1, b2]

    return LR_instruction, map


def part1(data : tuple) -> int:
    LR, map = data

    steps = 0
    node = 'AAA'
    while node != 'ZZZ':
        d = LR[steps%len(LR)] # periodic boundry conditions
        node = map[node][1 if d == 'R' else 0] # update node
        steps += 1
    
    return steps


def find_cycle(node : str, LR : str, map : dict) -> tuple:
    # find the start of the cycle and the cycle length for each node.
    steps = 0
    end_nodes = []
    steps_to_endnodes = []
    while True:
        d = LR[steps%len(LR)]
        steps += 1

        node = map[node][1 if d == 'R' else 0]
        if node[-1] == 'Z':
            if node not in end_nodes:
                end_nodes.append(node)
                steps_to_endnodes.append(steps)
            else:

                start = steps_to_endnodes[end_nodes.index(node)]
                length = steps - start
                print(f"Cycle found with length {length} starting at {start}")
                if len(end_nodes) > 1:
                    print("End nodes are not unique!")
                    return -1
                return start, length
        

def part2(data : tuple) -> int:
    """
        Method: After some point the sequence will become cyclic.
                - find all start nodes
                - for each node, find the cyclic pattern for the end nodes 
                - find the lowest common multiple of the cycle lengths
    """
    LR, map = data
    # find all start nodes
    nodes = [key for key in map.keys() if key[-1] == 'A']

    # find the cycle length for each node
    cycles = [find_cycle(node, LR, map) for node in nodes]  # note that all cycles(lengths) start at 0 !

    # find the lowest common multiple of the cycle lengths
    return np.lcm.reduce([cycle[1] for cycle in cycles])

if __name__=='__main__':
    tic = time()
    data = readData('../Data/day08')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', time()-tic)
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic)