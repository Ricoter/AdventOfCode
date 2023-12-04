"""
    Advent of Code 2023, Day 1     🎄
    Python v3.10.12
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time


def readData(infile : str) -> list:
    data = []
    with open(infile, 'r') as f:
        data = [line.strip() for line in f]
    return data


def part1(data):
    sum = 0
    for line in data:
        digits = [x for x in line if x.isdigit()]
        calibration_value = int(digits[0]) * 10 + int(digits[-1])
        # print(line, digits, calibration_value)
        sum += calibration_value
    return sum


def part2(data):
    # create a dictionary with the written numbers and digits
    numbers_dict = {"one":1, "two":2, "three":3, "four":4, "five":5,
                    "six":6, "seven":7, "eight":8, "nine":9, '1':1, '2':2,
                    '3':3, '4':4, '5':5, '6':6, '7':7,'8':8, '9':9}
    sum = 0
    for line in data:
        # find the first number in the line
        first = re.search(r"one|two|three|four|five|six|seven|eight|nine|\d", line)
        first = first.group() # get the match
        first = numbers_dict[first] # get the value from the dictionary

        # find the last number in the line (reverse the line first due to overlapping words)
        last = re.search(r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d", line[::-1])
        last = last.group()
        last = numbers_dict[last[::-1]]

        calibration_value = first * 10 + last
        # print(line, first, last, calibration_value)
        sum += calibration_value

    return sum



if __name__=='__main__':
    # add a timer to measure runtime
    tic = time()

    # put the data in a list
    data = readData('../Data/day01')
    print("data:", data, "\ntime:", tic-time())

    tic = time()
    # run part 1 with deepcopy to prevent changing the original data
    print("part 1:", part1(deepcopy(data)), 'time:', tic-time())
 
    # 
    # 54391

    tic = time()
    # run part 2
    print("part 2:", part2(data), 'time:', tic-time()) 
