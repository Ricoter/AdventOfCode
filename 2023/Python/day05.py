"""
    Advent of Code 2023, Day 5     🎄🎄🎄🎄🎄
    Python v3.10.12
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time


def readData(infile : str) -> dict:
    data = {}
    with open(infile, 'r') as f:
        # based on the first word in the line, we know what to do
        kind = "None"
        next_kind = "seeds"

        for line in f:
            line = line.strip()

            # skip empty lines
            if line == "":
                continue

            # change kind
            elif line.startswith(next_kind):
                kind = next_kind

                # initial case (= special case)
                if kind == "seeds":
                    initial_seeds = [int(x) for x in line[6:].split()]
                    next_kind = "seed"
                    data[kind] = {
                        "numbers" : initial_seeds,
                        "target" : next_kind
                        }
                    
                # general case
                else:
                    next_kind = re.split(r"-| ", line)[2] # split on - or space and take 3rd element
                    data[kind] = {
                        "numbers" : [],
                        "target" : next_kind
                        }
                    

            # add numbers to kind
            else:
                data[kind]["numbers"].append([int(x) for x in line.split()])
    return data


def next_number(N : int, mapping : list) -> int:
    for o, i, l in mapping:
        if i <= N < i+l:
            return N + (o-i)
    return N


def part1(data : dict) -> int:
    location = np.inf
    for N in data["seeds"]["numbers"]:
        # print(initial_seeds)  
        kind = "seed"
        
        while kind != "location":
            mapping = data[kind]["numbers"]
            N = next_number(N, mapping)
            kind = data[kind]["target"]
        location = min(location, N)
    return location


def range_mapper(N : int, d : int, mappings : list) -> list:
    # order mapping on (i)nput number
    mappings = sorted(mappings, key=lambda x: x[1])
    new_numbers = []

    Na = N          # first number in number range
    Nb = N + d - 1  # last number in number range
    # print(f"- mapping: {mappings}, N: {N}, d: {d}, Nb: {Nb}")

    # cut the number range in pieces according to the mapping
    # the mappings are ordered from low to high
    for o, i, l in mappings:
        ia = i          # first number in map range 
        ib = i + l - 1  # last number in map range
        # print(o, i, l, ib)

        if ib < Na:     # map range is below number range 
            # print("check 1")
            continue
        elif Nb < ia:   # map range is above number range (and all following ranges will be too)
            # print("check 2")
            break
        else:           # map range and number range overlap
            # print("check 3")
            if Na < ia: # add number before map range
                # print("check 3a")
                _N = Na
                _d = ia - Na  
                new_numbers.append((_N, _d))

            # if ib < Nb: # add number after map range
            #     print("check 3b")
            #     _N = ib + 1
            #     _d = Nb - ib
            #     new_numbers.append((_N, _d))

            # add map range
            offset = o - i
            a = max(Na, ia)
            b = min(Nb, ib)
            _N = a + offset
            _d = b - a + 1
            new_numbers.append((_N, _d))
        
        Na = ib + 1 # update number range

    _N = Na
    _d = Nb - Na + 1
    new_numbers.append((_N, _d))
    # print(f"-- returning -> new_numbers: {new_numbers}")
    return new_numbers



def part2(data : NotImplemented) -> NotImplemented:
    # iterate while taking 2 steps at a time
    numbers = []
    for i in range(0, len(data["seeds"]["numbers"]), 2):
        N, d = data["seeds"]["numbers"][i:i+2]
        numbers.append((N, d))

    kind = "seed"
    while kind != "location":
        mapping = data[kind]["numbers"]
        new_numbers = []
        # print("+", kind, numbers, "|", mapping)
        for N, d in numbers:
            new_numbers.extend(range_mapper(N, d, mapping))
        kind = data[kind]["target"]
        numbers = deepcopy(new_numbers)
        # print("++", kind, "| numbers:", numbers)
    # print(numbers)
    return np.min([n for n, _ in numbers])


if __name__=='__main__':
    tic = time()
    data = readData('../Data/day05')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', time()-tic)
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic)