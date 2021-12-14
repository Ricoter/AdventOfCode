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
        d[a] = b
    # data = [line.split(' ') for line in data]
    # data = np.array([list(line) for line in data]).astype(int)
    return start, d

def part1(data):
    seq, d = data
    for _ in range(10):
        new_seq = [seq[0]]
        for i in range(len(seq)-1):
            new_seq += [d[seq[i:i+2]], seq[i+1]]
        seq = "".join(new_seq)
    count = Counter(seq).values()
    return max(count)- min(count)

def part2(data):
    # seq, d = data
    # vals = []
    # for _ in range(20):
    #     new_seq = [seq[0]]
    #     for i in range(len(seq)-1):
    #         new_seq += [d[seq[i:i+2]], seq[i+1]]
    #     seq = "".join(new_seq)
    #     count = Counter(seq).values()
    #     vals.append(max(count)- min(count))
    #     print(max(count), min(count))
    # print(vals)
    # print([vals[i+1]/vals[i] for i in range(len(vals)-1)])
    # plt.plot(vals)
    # plt.show()
    return

    
if __name__=='__main__':
    data = readData('../Data/day14')
    print(data)
    print(part1(data))
    print(part2(data))