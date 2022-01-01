import numpy as np
import re


def readData(infile : str) -> np.ndarray:
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = re.split(r" x=|\.\.|,y=|,z=", line.strip("\n"))

            linedata = []
            for x in line:
                if x=='on':
                    linedata.append(1)
                elif x=='off':
                    linedata.append(0)
                else:
                    linedata.append(int(x))
            
            data.append(linedata)
            
    data = np.array([list(line) for line in data]).astype(int)
    return data


def volume(x : np.ndarray) -> int:
    a = (x[1]-x[0]+1)
    b = (x[3]-x[2]+1)
    c = (x[5]-x[4]+1)
    return a*b*c


def sub_cuboids(a : np.ndarray , b : np.ndarray) -> list[np.ndarray]:
    """ cuts cuboidic regions from all 6 sides of a that do not overlap with b

    Args:
        a (ndarray): cuboid described by (x0, x1, y0, y1, z0, z1)
        b (ndarray): cuboid described by (x0, x1, y0, y1, z0, z1)

    Returns:
        list[ndarray]: list with cuboidic regions of a that do not overlap with b
    """
    original_a = np.copy(a)
    cuboids = []
    for i in range(6):

        # cut from left (x0), upper (y0), back (z0)
        if i%2==0 and b[i]>a[i]:

            # b not in a
            if b[i] > a[i+1]:
                return [original_a]

            # cut from a
            c = np.copy(a)
            c[i+1] = b[i] - 1
            cuboids.append(c)
            a[i] = b[i]

        # cut from right (x1), lower (y1), front (z1)
        elif i%2==1 and b[i]<a[i]:

            # b not in a
            if b[i] < a[i-1]:
                return [original_a]
            
            # cut from a
            c = np.copy(a)
            c[i-1] = b[i] + 1
            cuboids.append(c)
            a[i] = b[i]

    return cuboids


def solve(data):
    score = 0
    for i, line in enumerate(data):
        if line[0] == 0:
            continue

        cubes = [line[1:]]
        for line2 in data[i+1:, 1:]:
            cubes = [y for x in cubes for y in sub_cuboids(x, line2)]
            
        score += sum(volume(x) for x in cubes)
    return score


if __name__=='__main__':
    data = readData('../Data/day22')
    print(solve(data[:20]))
    print(solve(data))