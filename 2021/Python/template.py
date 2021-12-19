import numpy as np

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    # data = [line.split(' ') for line in data]
    # data = np.array([list(line) for line in data]).astype(int)
    return data

def part1(data):
    return

def part2(data):
    return 

if __name__=='__main__':
    data = readData('../Data/day13')
    print(part1(data))
    print(part2(data))