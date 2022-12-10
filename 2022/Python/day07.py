"""
    Advent of Code 2022, Day 7     🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
import re

def readData(infile : str) -> np.array(int):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]

    # split lines in chunks
    # data = [re.split(r"-|,", line) for line in data]

    # to numpy 2D array (characterwise)
    # data = np.array([list(line) for line in data]).astype(int)
    return data
    return np.array(data).astype(int)

def find_last_index(search_list, search_item):
    return len(search_list) - 1 - search_list[::-1].index(search_item)

def dataPrep(data) -> dict:
    i = 0
    D = {'/':{'parent' : '/', 'files' : [], 'dirs' : [], 'depth' : 0, 'size' : 0}}
    current = '/'
    while i < len(data):
        line = data[i]

        # change directory
        if line[:4] == '$ cd':
            # print(current, line[5:])
            if line[5:] == '..':
                current = D[current]['parent']
            elif line[5:] == '/':
                current = '/'
            else:
                current += line[5:] + '/'
            i += 1
        
        # list files and directories
        elif line[:4] == '$ ls':
            i += 1
            if i >= len(data):
                break
            line = data[i]
            while line[0] != '$':
                # add directory
                if line[:4] == 'dir ':
                    dir = line[4:]
                    path = current + dir + '/'
                    if path not in D:
                        D[path] = {
                            'parent' : current, 
                            'files' : [], 
                            'dirs' : [], 
                            'depth' : D[current]['depth'] + 1, 
                            'size' : 0
                            }
                    # else:
                        # print("!", path)
                    D[current]['dirs'].append(dir)
                # add file
                else:
                    size, name = line.split(' ')
                    D[current]['files'].append([int(size), name])
                    D[current]['size'] += int(size)
                    path = current
                    while len(path) > 1:
                        # print( path, find_last_index(path[:-1], '/'))
                        path = path[:find_last_index(path[:-1], '/')+1]
                        
                        D[path]['size'] += int(size)

                # next line
                i += 1
                if i >= len(data):
                    break
                line = data[i]         
    return D

def part1(data):
    D = dataPrep(data)
    total_size = 0
    for path in D:
        # print(path, type(path))
        if D[path]['size'] <= 1e5:
            total_size += D[path]['size']
    # print(D)
    return total_size


def part2(data):
    D = dataPrep(data)
    free = int(7e7) - D['/']['size']
    sizes = [D[key]['size'] + free for key in D]
    for s in sorted(sizes):
        if s >= 3e7:
            return s - free
    return -1


if __name__=='__main__':
    data = readData('../Data/day07')
    # print(data)

    print("part 1:", part1(data))
    print("part 2:", part2(data))