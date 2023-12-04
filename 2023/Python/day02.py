"""
    Advent of Code 2023, Day 2     🎄🎄
    Python v3.10.12
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time

def readData(infile : str) -> list:
    """
    EXAMPLE 
    
        input lines: 
            
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        
        output:
            
            [
                [['3 blue', '4 red'], ['1 red', '2 green', '6 blue'], ['2 green']],
                [['1 blue', '2 green'], ['3 green', '4 blue', '1 red'], ['1 green', '1 blue']]
            ]
    """
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            line = re.split(r":|;", line)
            game = [set.strip().split(',') for set in line[1:]]
            data.append(game)

    return data


def part1(data : list) -> int:
    max_colors = {"red": 12, "green": 13, "blue": 14}
    
    sum = 0
    for i, game in enumerate(data):
        possible = True
        for set in game:
            for color in set:
                n, color = color.split() # '3 blue' -> ['3', 'blue']
                n = int(n)
                if n > max_colors[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            sum += i + 1
    return sum


def part2(data : list) -> int:
    sum = 0

    for game in data:
        min_colors = {"red": 0, "green": 0, "blue": 0}
        for set in game:
            for color in set:
                n, color = color.split()
                n = int(n)
                if n > min_colors[color]: # if n is bigger than the current min, update min
                    min_colors[color] = n
        power = min_colors["red"] * min_colors["green"] * min_colors["blue"] 
        sum += power
    return sum


if __name__=='__main__':
    tic = time()
    data = readData('../Data/day02')
    print("data:", data, "\ntime:", tic-time())

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', tic-time())
    tic = time()
    print("part 2:", part2(data), 'time:', tic-time())