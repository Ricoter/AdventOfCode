"""
    Advent of Code 2023, Day 7     🎄🎄🎄🎄🎄🎄🎄
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
        for line in f:
            line = line.strip().split()
            data.append(line)

    return data


def kind(counts : list) -> int:
    
    match counts:
        case [5]:
            # 5 of a kind
            return 0
        case [1, 4]:
            # 4 of a kind
            return 1
        case [2, 3]:
            # full house
            return 2
        case [1, 1, 3]:
            # 3 of a kind
            return 3
        case [1, 2, 2]:
            # 2 pairs
            return 4
        case [1, 1, 1, 2]:
            # 1 pair
            return 5
        case [1, 1, 1, 1, 1]:
            # high card
            return 6
        case _:
            print("Something went wrong")
            print("counts:", counts)
            return -1


def total_winnings(data : list) -> int:
    # sort data by kind and label values
    data.sort(key=lambda x: (x[-2], x[-1]), reverse=True)

    # return sum of winnings
    return sum([rank * int(bid) for rank, (_, bid, _, _) in enumerate(data, 1)])


def part1(data : list) -> int:

    label = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, 
             '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
    
    for i, (hand, _) in enumerate(data):
        # count occurences of each card in list
        _, counts = np.unique(list(hand), return_counts=True)
        
        # sort counts in ascending order
        counts = list(np.sort(counts)) 

        # add kind to data
        data[i].append(kind(counts))

        # add label values to data
        data[i].append([label[x] for x in hand])

    # return "total winnings"
    return total_winnings(data)


def part2(data : list) -> int:

    label = {'A': 1, 'K': 2, 'Q': 3, 'J': 14, 'T': 5, '9': 6, '8': 7, 
             '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
    
    for i, (hand, _) in enumerate(data):
        
        n_jokers = len([1 for x in hand if x == 'J'])

        if n_jokers == 5:
            counts = [5]
        else:
            hand_without_J = [x for x in hand if x != 'J']

            # count occurences of each card in list
            _, counts = np.unique(hand_without_J, return_counts=True)
            
            # sort counts in ascending order
            counts = list(np.sort(counts)) 
            # print("hand:", hand_without_J, "counts:", counts, "jokers:", n_jokers)

            # add number of jokers to the best number in counts (which is last)
            counts[-1] += n_jokers

        # add kind to data
        data[i].append(kind(counts))

        # add label values to data
        data[i].append([label[x] for x in hand])

    # return "total winnings"
    return total_winnings(data)


if __name__=='__main__':
    tic = time()
    data = readData('../Data/day07')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    print("part 1:", part1(deepcopy(data)), 'time:', time()-tic)
    
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic)