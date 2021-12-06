import numpy as np
from numpy.lib.shape_base import split

def readData(infile):
    with open(infile, 'r') as f:
        data = [int(x) for x in f.readline().split(',')]
    # data = np.array(data).astype(int)
    print(data)
    return data

def part1(fish):
    for day in range(80):
        babies = 0
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] == -1:
                fish[i] = 6
                babies += 1
        fish += [8] * babies
        # print(fish)
    return len(fish)

def part2(data, days=256):
    """Strategie: group fish by cycle day, than you complexity is O(1)"""

    fishList = [0 for _ in range(9)]
    for fish in data:
        fishList[fish] += 1
    

    for _ in range(days):
        new_fish = fishList[0]

        fishList[0] = fishList[1]
        fishList[1] = fishList[2]
        fishList[2] = fishList[3]
        fishList[3] = fishList[4]
        fishList[4] = fishList[5]
        fishList[5] = fishList[6]
        fishList[6] = fishList[7] + new_fish
        fishList[7] = fishList[8] 
        fishList[8] = new_fish

    return sum(fishList)

if __name__=='__main__':
    data = readData('../Data/day06')
    print(part1(data[:]))
    print(part2(data[:]))