import numpy as np
from scipy import ndimage


def readData(infile):
    with open(infile, 'r') as f:
        data = [list(line.strip('\n')) for line in f]
    return np.array(data).astype(int)


def part1(data):
    D = np.pad(data, pad_width=1, mode='maximum')

    rows = D.shape[0]
    cols = D.shape[1]

    minima = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            d = D[i,j]
            if d<D[i+1,j] and d<D[i-1,j] and d<D[i,j+1] and d<D[i,j-1]:
                minima += d + 1
    return minima


def part2(data):
    # label basins from 1 to nLabels
    basins, nLabels = ndimage.label(data < 9)

    sizes = [np.sum(basins == n) for n in range(1, nLabels+1)]
    return np.prod(np.sort(sizes)[-3:])

if __name__=='__main__':
    data = readData('../Data/day09')
    print(part1(data))
    print(part2(data))