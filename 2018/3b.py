import numpy as np

with open('input/3', 'r') as f: # read data
    data = [line.strip('\n#') for line in f]

data = [x.split() for x in data] # ['1', '@', '1,3:', '4x4']
data = [[i] + j.strip(':').split(',') + k.split('x') for i, _, j, k in data] # ['1', '1', '3', '4', '5']
data = np.asarray(data).astype(int) # to int

grid = np.zeros((10000,10000)) # large grid with zeros

for line in data: # 
    for row in range(line[3]):
        for col in range(line[4]):
            grid[line[1]+row][line[2]+col] += 1 # add 1 every time a grid-position is used

overlap = len(grid[grid>1]) # count all positions on the grid that are used more than once
print(overlap)

def overlap(grid, line): # Returns True if ID has overlap else False
    for row in range(line[3]):
        for col in range(line[4]):
            if grid[line[1]+row][line[2]+col] > 1:
                return(True) # exit function if a grid-position is used more than once
    return(False) # if not exit yet, it doesnt contain a double used position

for line in data:
    if overlap(grid, line) == False: # print id without overlap
        print('ID without overlap:', line[0])
        break
