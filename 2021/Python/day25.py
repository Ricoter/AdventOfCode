import numpy as np

def readData(infile : str) -> np.ndarray:
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    data = np.array([list(line) for line in data])
    return data

def solve(grid : np.ndarray) -> int:
    rows, cols = grid.shape

    counter = 0
    while True:
        x = False

        old_grid = np.copy(grid)
        for i in range(rows):
            for j in range(cols):
                jj = (j+1)%cols
                if old_grid[i,j] == '>' and old_grid[i,jj] == '.':
                    grid[i,j] = '.'
                    grid[i,jj] = '>'
                    x = True

        old_grid = np.copy(grid)
        for i in range(rows):
            for j in range(cols):
                ii = (i+1)%rows
                if old_grid[i,j] == 'v' and old_grid[ii,j] == '.':
                    grid[i,j] = '.'
                    grid[ii,j] = 'v'
                    x = True

        counter += 1  
        if not x:
            return counter


if __name__=='__main__':
    data = readData('../Data/day25')
    print(solve(data))