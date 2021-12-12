import numpy as np
from scipy import ndimage

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    data = np.array([list(line) for line in data]).astype(float)
    data = np.pad(data, pad_width=1, mode='constant', constant_values=-np.inf)
    return data


def part1(data):
    total = 0
    for _ in range(100):
        data += 1
        flash = list(zip(*np.where(data==10)))
        for i, j in flash:
            for di in range(i-1, i+2):
                for dj in range(j-1, j+2):
                    data[di, dj] += 1
                    if data[di, dj] == 10:
                        flash.append((di, dj))
        total += len(flash)
        data[data > 9] = 0
    return int(total)


def part2(data):
    for run in range(1000):
        data += 1
        flash = list(zip(*np.where(data==10)))
        for i, j in flash:
            for di in range(i-1, i+2):
                for dj in range(j-1, j+2):
                    data[di, dj] += 1
                    if data[di, dj] == 10:
                        flash.append((di, dj))
        data[data > 9] = 0 
        if np.sum(data==0) == 100:
            return run+1
    return False

if __name__=='__main__':
    data = readData('../Data/day11')
    print(part1(np.copy(data)))
    print(part2(data))