import numpy as np

def readData(infile):
    # target area: x=60..94, y=-171..-136
    x_range = 60, 94
    y_range = -171, -136
    return x_range, y_range


def triangular(n):
    return n*(n+1)//2


def part1(data):  
    """
        y going up and down is partly symmetrical (it will come back to y0)
        the highest shot will be (when going down) just slow enough to not mis y_min forever
        
        - there is a minus 1 because the first step below y0 is increased by 1
        - the triangular formula is the sum of n n-1 n-2 n-3 ... 0
    """
    return triangular(-data[1][0] - 1)


def check(dx, x_min, x_max, dy, y_min, y_max):
    x, y = 0, 0
    while (x <= x_max) & (y >= y_min):
        x += dx
        y += dy
        dy -= 1
        if dx > 0:
            dx -= 1
        if (x_min <= x <= x_max) & (y_min <= y <= y_max):
            return True
    return False


def part2(data):
    x_range, y_range = data
    x_min, x_max = x_range
    y_min, y_max = y_range

    x_first = 0
    while not (x_min < triangular(x_first) < x_max):
        x_first += 1

    count = 0
    for dx in range(x_first, x_max+1):
        for dy in range(-172, 171+1):
            count += check(dx, x_min, x_max, dy, y_min, y_max)
            
    return count

if __name__=='__main__':
    data = readData('../Data/day17')
    print(part1(data))
    print(part2(data))