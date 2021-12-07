import numpy as np

def readData(infile):
    with open(infile, 'r') as f:
        data = np.array(f.readline().split(',')).astype(int)
    return data

def linear(x):
    return x

def stepwiseIncremental(dx):
    return dx*(dx+1)/2

def solve(data, costFn):
    fuelCosts = np.zeros(max(data))
    positions = np.arange(max(data))
    for x in data:
        dx = np.abs(positions - x)
        fuelCosts += costFn(dx)
    return  int(fuelCosts.min())

if __name__=='__main__':
    data = readData('../Data/day07')
    print(solve(data, costFn=linear))
    print(solve(data, costFn=stepwiseIncremental))