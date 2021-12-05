import numpy as np
import re

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    data = [re.split(' -> |,', line) for line in data]
    data = np.array(data).astype(int)
    # print(data.shape) # (500 x 4)
    return data

def part1(data):
    N = np.max(data)
    grid = np.zeros((N, N))
    for (x1, y1, x2, y2) in data:
        if (x1 != x2) and (y1 != y2):
            continue
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        grid[x1:x2+1, y1:y2+1] += 1 
    return np.sum(grid > 1)


def part2(data):
    N = np.max(data) + 1
    grid = np.zeros((N, N))
    for (x1, y1, x2, y2) in data:
        # diagonal
        if (x1 != x2) and (y1 != y2):
            nx, ny = (x2-x1)/abs(x2-x1), (y2-y1)/abs(y2-y1)
            for d in range(abs(x2-x1)+1):
                xi = int(x1 + d*nx)
                yi = int(y1 + d*ny)
                grid[xi,yi] += 1
        # horizontal + vertical
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            grid[x1:x2+1, y1:y2+1] += 1 

    return np.sum(grid > 1)


if __name__=='__main__':
    data = readData('../Data/day05')
    print(part1(data))
    print(part2(data))