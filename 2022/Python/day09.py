"""
    Advent of Code 2022, Day 9     🎄🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
import re

def readData(infile : str) -> np.array(int):
    with open(infile, 'r') as f:
        data = []
        for line in f:
            a, b = line.strip('\n').split()
            data.append([a, int(b)])

    # split lines in chunks
    # data = [re.split(r"-|,", line) for line in data]

    # to numpy 2D array (characterwise)
    # data = np.array([list(line) for line in data]).astype(int)
    return data

dir = {
    'R' : np.array([ 1, 0]),
    'L' : np.array([-1, 0]),
    'U' : np.array([ 0,-1]),
    'D' : np.array([ 0, 1])
}

def part1(data):
    H = np.array([0,0])
    T = np.array([0,0])
    visited = {tuple(T)}
    for d, steps in data:
        for _ in range(steps):
            H += dir[d] # update head
            diff = H-T  # difference between head and tail

            # Case 1: Tail is still touching Head
            if max(abs(diff)) < 2:
                continue

            # Case 2: x|y distance == 2 AND y|x distance == 0
            elif min(abs(diff)) == 0:
                T += (diff) // 2

            # Case 3: x|y distance == 2 AND y|x distance == (1 or 2)
            elif min(abs(diff)) == 1:
                # movie diagonally
                T += diff//abs(diff)

            visited.add(tuple(T))
    return len(visited)


def part2(data):
    H = np.array([0,0])
    Hs = [H.copy()]
    # print(Hs)
    for d, steps in data:
        for _ in range(steps):
            H += dir[d] # update head
            Hs.append(H.copy())
    # print(Hs)

    for _ in range(9):
        T = np.array([0,0])
        Ts = [T.copy()]

        for H in Hs:
            diff = H-T  # difference between head and tail
            # Case 1: Tail is still touching Head
            if max(abs(diff)) < 2:
                continue
            # Case 2: x|y distance == 2 AND y|x distance == 0
            elif min(abs(diff)) == 0:
                T += (diff) // 2
            # Case 3: x|y distance == 2 AND y|x distance == (1 or 2)
            else:
                # movie diagonally
                T += diff//abs(diff)
            Ts.append(T.copy())
        Hs = Ts
    return len(set([tuple(x) for x in Ts]))


if __name__=='__main__':
    data = readData('../Data/day09')
    print(data)

    print("part 1:", part1(data))
    print("part 2:", part2(data)) # > 2326