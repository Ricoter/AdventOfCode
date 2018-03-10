import os
import sys
import numpy as np


def manhattan_distance(number):
    steps = 0
    smallest_square = 1
    while smallest_square * smallest_square <= number:
        smallest_square += 2
    smallest_square -= 2
    difference = number - smallest_square * smallest_square
    dist1 = (smallest_square - 1)/2 +1
    print('n: ', smallest_square)
    print('squared', smallest_square * smallest_square)
    print('dist: ',dist1)
    steps += dist1 # distance to ring
    steps += (difference + dist1) % dist1
    print(int(steps))

def loop_with_addition(number):
    # estimate grid dimensions (every turn roughly doubles)
    order = 1
    while(number > 2**order):
        order += 1
    padding = 2
    d = 1 + int(np.ceil(order / 4.0)) * 2 + padding

    # initialize grid
    grid = np.zeros([d,d])
    middle = int((d - 1)/2)
    x, y = middle, middle
    grid[x,y] = 1

    # initialize movement parameters\
    square = 1 # square to start
    directions = ((0,1), (-1,0), (0,-1), (1,0)) # (right, up, left, down)
    steps = 1 # steps before turn
    k = 0 # direction

    #
    while(True):
        for l in range(int(np.floor(steps))):
            # Move to next square
            i, j = directions[k%4]
            x += i
            y += j

            # Update value
            value = int(np.sum(grid[x-1:x+2,y-1:y+2]))
            grid[x,y] = value
            square += 1

            # Break and print result
            if(value > number):
                print('value: ', value)
                print('square: ', square)
                return(grid)
        # Update direction
        k += 1
        steps += 0.5


#                   __main__
def main(number):
    # manhattan_distance(int(number))
    grid = loop_with_addition(int(number))
    np.set_printoptions(suppress=True, linewidth=400)
    print(grid[1:-1,1:-1])

if __name__ == "__main__":
    main(sys.argv[1])
