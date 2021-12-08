import numpy as np
import matplotlib.pyplot as plt

def readData(infile):
    with open(infile, 'r') as f:
        data = [[x=='#' for x in line.strip('\n')] for line in f]
    data = np.array(data).astype(int)
    data = np.pad(data, 10, mode='constant')
    print(data.shape)
    return data


def solve(data):
    D = np.array([(-1,0), (0,1), (1,0), (0,-1)])
    curr = ((np.array(data.shape) - 1) / 2).astype(int)
    print(curr)
    infc = 0
    for _ in range(10000):
    
        # turn & flip
        if data[tuple(curr)]:
            D = np.roll(D, -1, axis=0)
            data[tuple(curr)] = 0
        else:
            D = np.roll(D, 1, axis=0)
            data[tuple(curr)] = 1
            infc += 1


        # forward
        curr += D[0]
    return infc


def solve2(data):
    d = np.array([(-1,0), (0,1), (1,0), (0,-1)])
    pos = ((np.array(data.shape) - 1) / 2).astype(int)

    a = np.zeros(1000)
    counter = 0
    for i in range(1000):
        a[i] = counter
        # turn & flip
        x = tuple(pos)
        # print(data[x])

        if data[x] == 1:
            d = np.roll(d, -1, axis=0)
            data[x] = -1
        elif data[x] == 0:
            d = np.roll(d, 1, axis=0)
            data[x] = 2
        elif data[x] == 2:
            data[x] = 1
            counter += 1
        elif data[x] == -1:
            d = np.roll(d, 2, axis=0)
            data[x] = 0
        # print(data)

        # forward
        pos += d[0]
    # plt.plot(a[-200:])
    plt.pcolormesh(data)
    plt.show()
    return counter

if __name__=='__main__':
    data = readData('../input/22t')
    # print(solve(data))
    print(solve2(data))