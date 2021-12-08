import numpy as np
import re

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    data = [re.split(" \| | ", line) for line in data]
    return data

# returns the number(s) from the length
getNum = {
    2 : [1],
    3 : [7],
    4 : [4],
    5 : [2, 3, 5],
    6 : [0, 6, 9],
    7 : [8]
}

def part1(data):
    counter = 0
    for line in data:
        for string in line[-4:]:
            if len(string) in [2,3,4,7]:
                counter += 1
    return counter

def part2(data):
    answer = 0
    for line in data:

        # this saves the codes by LENGTH! also all lengths are filled for every line
        nums = {i:[] for i in range(2,8)}
        for s in line:
            nums[len(s)].append(s)
        
        # find 4-digit number by comfirming subsets
        n = ""
        for s in line[-4:]:
            # trivial case
            if len(s) in [2, 3, 4, 7]:
                n += str(getNum[len(s)][0])
            
            if len(s) == 5:
                # Combined code for letters 'b' and 'd'
                bd = [c for c in list(nums[4][0]) if c not in list(nums[2][0])] # 4-1 = bd
                if set(bd).issubset(s):
                    n += "5"
                elif set(nums[2][0]).issubset(s): # 
                    n += "3"
                else:
                    n += "2"

            if len(s) == 6:
                if set(nums[4][0]).issubset(s):
                    n += "9"
                elif set(nums[2][0]).issubset(s):
                    n += "0"
                else:
                    n += "6"

        answer += int(n)
    return answer

if __name__=='__main__':
    data = readData('../Data/day08')
    print(part1(data))
    print(part2(data))