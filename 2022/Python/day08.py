"""
    Advent of Code 2022, Day 8     🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
import re

def readData(infile : str) -> np.array(int):
    with open(infile, 'r') as f:
        data = [list(line.strip('\n')) for line in f]

    # split lines in chunks
    # data = [re.split(r"-|,", line) for line in data]

    # to numpy 2D array (characterwise)
    data = np.array([list(line) for line in data]).astype(int)
    return np.array(data).astype(int)

def check(data, i, j):
    S = data[i,j]   # Size
    L = data[:i,j]  # Left
    R = data[i+1:,j]# Right
    T = data[i,:j]  # Top
    B = data[i,j+1:]# Bottom
    return (sum(L>=S)==0) | (sum(R>=S)==0) | (sum(T>=S)==0) | (sum(B>=S)==0)

def part1(data : np.array(int)) -> int:
    visable_trees = 0
    for i in range(data.shape[0]): # vertical
        for j in range(data.shape[1]): # horizontal
            visable_trees += check(data, i, j)
    return visable_trees

def scenic_score(data, i, j):
    S = data[i,j]   # Size
    L = data[:i,j]  # Left
    R = data[i+1:,j]# Right
    T = data[i,:j]  # Top
    B = data[i,j+1:]# Bottom
    score = 1
    for dir in [L[::-1], R, T[::-1], B]:
        trees = 0 
        for t in dir:
            if t<=S:
                trees += 1
            if t>=S:
                break
        score *= trees
    return score


def part2(data):
    highscore = 0
    for i in range(data.shape[0]): # vertical
        for j in range(data.shape[1]): # horizontal
            highscore = max(highscore, scenic_score(data,i,j))
    return highscore


if __name__=='__main__':
    data = readData('../Data/day08')
    print(data)

    print("part 1:", part1(data)) # < 9223
    print("part 2:", part2(data))