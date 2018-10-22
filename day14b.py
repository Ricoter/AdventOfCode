from day10b import main as hash_fn
import numpy as np
from scipy.ndimage.measurements import label

def main(data):
    used = 0
    grid = np.zeros((128,128))
    for row in range(128):
        knothash = hash_fn(data + '-' + str(row))
        print(knothash, type(knothash))        
        col = 0
        for c in knothash:
            hexscale, num_of_bits = 16, 4
            b = bin(int(c, hexscale))[2:].zfill(num_of_bits)
            for i in b:
                grid[row, col] = int(i)
                col += 1

    _, num_islands =  label(grid)
    return num_islands


if __name__ == '__main__':
    print(main('uugsqrei'))
