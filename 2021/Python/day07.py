import numpy as np

def readData(infile):
    with open(infile, 'r') as f:
        data = np.array(f.readline().split(',')).astype(int)
    return data

def part1(data):
    fuelCosts = np.zeros(max(data))
    positions = np.arange(max(data))
    for x in data:
        dx = np.abs(positions - x)
        fuelCosts += dx
    return  int(fuelCosts.min())

def part2(data):
    fuelCosts = np.zeros(max(data))
    positions = np.arange(max(data))
    for x in data:
        dx = np.abs(positions - x)
        fuelCosts += dx*(dx+1)/2
    return  int(fuelCosts.min())

if __name__=='__main__':
    data = readData('../Data/day07')
    print(part1(data))
    print(part2(data))