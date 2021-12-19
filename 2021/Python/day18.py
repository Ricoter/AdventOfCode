import numpy as np
from numpy.lib.function_base import interp

def readData(infile):
    with open(infile, 'r') as f:
        data = []
        for line in f:
            sub_data = []
            for c in line.strip('\n'):
                if c.isdigit():
                    sub_data.append(int(c))
                elif c in '[]':
                    sub_data.append(c)
            data.append(sub_data)
    return data


def split(n, i):
    a = n[i]//2
    b = n[i] - a
    n =  n[:i] + ['[', a, b, ']'] + n[i+1:] 
    return n


def explosion(n, i):
    a = n[i+1]
    b = n[i+2]
    n = n[:i] + [0] + n[i+4:]

    # a to left
    for _i in range(i-1, -1, -1):
        if type(n[_i]) == int:
            n[_i] += a
            break

    # b to right
    for _i in range(i+1, len(n)):
        if type(n[_i]) == int:
            n[_i] += b
            break
    return n


def reduce(n):
    action = True
    while action:
        depth, action = 0, False

        # explosion loop
        for i, c in enumerate(n):
            # update depth
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            if depth > 4:
                n = explosion(n, i)
                action = True
                break
        
        # split loop
        if not action:
            for i, c in enumerate(n):
                if (type(c)==int) and (c>9):
                    n = split(n, i)
                    action = True
                    break
    return n


def addition(a, b):
    return ['['] + a + b + [']']


def magnitude(n):
    while len(n) > 1:
        for i in range(1,len(n)):
            a = n[i-1]
            b = n[i]
            if type(a)==int and type(b)==int:
                n = n[:i-2] + [3*a + 2*b] + n[i+2:]
                break
    return n[0]


def part1(data):
    sum = data[0]
    for i in range(1, len(data)):
        sum = reduce(addition(sum, data[i]))
    return magnitude(sum)


def part2(data):
    import itertools
    largest_magnitude = 0
    for a, b in itertools.combinations(data, 2):
        mag_ab = magnitude(reduce(addition(a, b)))
        mag_ba = magnitude(reduce(addition(b, a)))
        largest_magnitude = max(largest_magnitude, mag_ab, mag_ba)
    return largest_magnitude


if __name__=='__main__':
    data = readData('../Data/day18')
    print(part1(data))
    print(part2(data))