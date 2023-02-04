"""
    Advent of Code 2022, Day 14     🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
# import sys 
# import os
# sys.path.append(os.path.abspath("../"))
# from utils.python.plots.showGrid import showGrid
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

def showGrid(x : np.array) -> print:
    """ Transpose image so water flows downwards """
    plt.imshow(x)
    plt.show()

# from plots/GridAnimation import *
def readData(infile : str) -> np.array:
    """ Note: The water flows from left to right in the grid,
    water starts at (500,0)

    -> This means that for this problem down is x-=1 and left is y-=1 
    """
    data = np.zeros([1000,1000])
    data[500,0] = -1
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(' -> ')
            for i in range(len(line)-1):
                a = line[i]
                b = line[i+1]
                ax, ay = eval(a)
                bx, by = eval(b)
                ax, bx = sorted([ax, bx])
                ay, by = sorted([ay, by])
                for x in range(ax, bx+1):
                    for y in range(ay, by+1):
                        data[x,y] = 1
    # trim the zero padding
    i = np.nonzero(data)
    data = data[min(i[0]):max(i[0])+1, min(i[1]):max(i[1])+1]
    # showGrid(data)
    return data


def animate_arrays(arrays):
    import matplotlib.animation as animation

    fig, ax = plt.subplots()

    def update(num):
        ax.imshow(arrays[num])

    ani = animation.FuncAnimation(fig, update, frames=len(arrays), repeat=False, interval=10, blit=True)
    plt.show()


def run(data : np.array) -> int:
    x_max, y_max = data.shape
    frames = [] # save frames for animation
    for sand in range(data.size): # just an upperlimit
        sand_origin = np.argwhere(data==-1)
        if len(sand_origin) == 0: 
            # animate_arrays(frames)    
            print('origin')
            return sand, data
        x, y = sand_origin[0] # coordinates of sand origin

        # go downward while possible
        while True:
            if (y + 1) >= y_max:       # infinite fall
                print('down')
                # animate_arrays(frames)
                return sand, data
            elif (data[x, y+1] == 0):   # move down
                y += 1
            elif x-1 < 0:               # infinite fall (l)
                print('left')
                # animate_arrays(frames)
                return sand, data
            elif data[x-1, y+1] == 0:   # move diagonally left/down
                x -= 1
                y += 1
            elif x+1 >= x_max:          # infinite fall (r)
                # animate_arrays(frames)
                print('right')
                return sand, data
            elif data[x+1, y+1] == 0:   # move diagonally right/down
                
                x += 1
                y += 1
            else:                       # place sand unit on the grid
                data[x, y] = 2
                break

        # add frame
        # current_layer = np.zeros_like(data)
        # current_layer[x,y] = 2
        # current_layer += data
        # frames.append(current_layer.T)
        # plt.imshow(current_layer.T)

    # animate_arrays(frames[:100])
    return 0

def part1(data : np.array) -> int:
    n, data = run(data)            
    showGrid(data.T)
    return n


def part2(data : NotImplemented) -> NotImplemented:
    # create new grid
    x_max, y_max = data.shape   
    origin = np.argwhere(data==-1)[0]
    data = np.pad(data, pad_width=((y_max-origin[0]+1, y_max-(x_max-origin[0])+2), (0,1)))
    data = np.pad(data, pad_width=((0,0), (0,1)), constant_values=1)

    # run simulation
    n, data = run(data)            
    showGrid(data.T)
    return n


if __name__=='__main__':
    data = readData('../Data/day14')
    print(data)

    print("part 1:", part1(deepcopy(data)))
    print("part 2:", part2(data))
