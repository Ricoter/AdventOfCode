import numpy as np

with open('input/6', 'r') as f: # read data
    coordinates = [line.strip('\n').split(', ') for line in f]

coordinates = np.asarray(coordinates).astype(int).T # transform data

counter = 0 # initialize variables
gridsize = np.max(coordinates) - 1

def total_man(i,j): # calculate total manhattan distance
    x = abs(coordinates[0] - i)
    y = abs(coordinates[1] - j)
    return(sum(x+y))

for i in range(gridsize): # loop over all possible grid positions
    for j in range(gridsize):
        if total_man(i,j) < 10000: # count locations 
            counter += 1

print(n)
