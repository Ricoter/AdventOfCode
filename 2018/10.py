import numpy as np
import matplotlib.pyplot as plt

with open('input/10', 'r') as f: # read data
    table = str.maketrans(dict.fromkeys(',position=<\n>velocity=<')) # chars to remove
    data = [line.translate(table).split() for line in f] 

x, y, dx, dy = np.asarray(data, dtype='f').T


def steps_to_centre_of_mass(_x, _dx):
    centre_of_momentum_frame = _dx - _dx.mean() # view from comoving reference frame
    centre_of_mass = _x - _x.mean() # centre of mass  
    return round(-(centre_of_mass/centre_of_momentum_frame).mean())

t = steps_to_centre_of_mass(x, dx) # headshot
print('timesteps', t)

x += t*dx # move to centre
y += t*dy

x -= min(x) # normalize
y -= min(y)

x = x.astype('i') # to integer
y = y.astype('i')

grid = np.zeros((max(x)+1,max(y)+1)) # initialize grid that fits text

for i in range(len(x)): # write text in the grid
    grid[x[i]][y[i]] = 1

grid = grid.T # correct x,y mistake

plt.imshow(grid) # show text
plt.show()
