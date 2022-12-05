"""
    Advent of Code 2022, Day 5     🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
import copy

def readData(infile : str) -> np.array(int):

    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]

    # get the current state of the board
    state = [[] for _ in range(9)]
    for line in data[:8]:
        for i in range(9):
            c = line[4*i + 1]
            if c != ' ':
                state[i].append(c)
    state = [x[::-1] for x in state]

    # split lines in chunks
    ops = []
    for line in data[10:]:
        _, N, _, a, _, b = line.split()
        ops.append([int(N),int(a)-1, int(b)-1]) # convert to 0-index

    return state, ops


def part1(state, ops):
    for N, a, b in ops:
        for _ in range(N):
            state[b].append(state[a].pop())
    return "".join([x[-1] for x in state])


def part2(state, ops):
    for N, a, b in ops:
        state[b] += state[a][-N:]
        state[a] = state[a][:-N]
    return "".join([x[-1] for x in state]) 


if __name__=='__main__':
    data = readData('../Data/day05')

    print("part 1:", part1(*copy.deepcopy(data)))
    print("part 2:", part2(*data))