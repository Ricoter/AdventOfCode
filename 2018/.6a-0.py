import numpy as np

with open('input/6', 'r') as f: # read data
    coordinates = [line.strip('\n').split(', ') for line in f]

coordinates = np.asarray(coordinates).astype(int).T # transform data

counter = 0 # initialize variables
gridsize = np.max(coordinates) - 1

def total_man(i,j): # calculate total manhattan distance
    x = abs(coordinates[0,None] - i)
    y = abs(coordinates[1,None].T - j)
    return(min(x+y))

#for i in range(gridsize): # loop over all possible grid positions
#    for j in range(gridsize):
#        if total_man(i,j) < 10000: # count locations 
#            counter += 1

print(counter)


def func(x, y):
    return sum(abs(x-y))

x = np.arange(gridsize)
y = np.arange(gridsize)
result = total_man(x[:,None], y[None,:])
print(result.shape)
print((result<10000).sum())
