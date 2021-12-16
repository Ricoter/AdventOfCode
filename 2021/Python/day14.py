import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    start = data[0]
    d = {}
    for line in data[2:]:
        a, b = line.split(" -> ")
        d[a] = (a[0]+b, b+a[1])
    return start, d



def solve(data, runs):
    """ Count pairs so complexity is proportional to the number of pairs """
    seq, d = data

    # counts number of pairs 
    n_pairs = {x:0 for x in d}
    for i in range(len(seq)-1):
        n_pairs[seq[i]+seq[i+1]] += 1

    
    for _ in range(runs):
        next_pairs = {x:0 for x in d}
        for key, value in n_pairs.items():
            if value > 0:
                a, b = d[key]
                next_pairs[a] += value
                next_pairs[b] += value
        n_pairs = next_pairs

    char_counter = {seq[-1]:1}
    for key, value in n_pairs.items():
        c = key[0]
        if c not in char_counter:
            char_counter[c] = 0
        char_counter[c] += value
    
    return max(char_counter.values()) - min(char_counter.values())


if __name__=='__main__':
    data = readData('../Data/day14')
    print(solve(data, 10))
    print(solve(data, 40))