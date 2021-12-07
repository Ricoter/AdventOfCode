import numpy as np

def readData(infile):
    with open(infile, 'r') as f:
        data = [int(x) for x in f.readline().split(',')]
    return data

def solve(data, days):
    """Strategie: group fish by cycle day, than your complexity is O(1)"""

    fishList = np.zeros(9, int)
    for fish in data:
        fishList[fish] += 1
    
    for _ in range(days):
        fishList = np.roll(fishList, -1)
        fishList[6] += fishList[-1]

    return sum(fishList)

if __name__=='__main__':
    data = readData('../Data/day06')
    print(solve(data[:], 80))
    print(solve(data[:], 256))