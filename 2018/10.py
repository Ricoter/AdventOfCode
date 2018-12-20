import numpy as np
import matplotlib.pyplot as plt

def timesteps_to_centre(_x, _dx):
    centre_of_momentum_frame = _dx - _dx.mean() # boost to comoving reference frame
    centre_of_mass = _x - _x.mean() # centre of mass  
    return round(-(centre_of_mass/centre_of_momentum_frame).mean())


def show_message(x,y):
    x, y = x.astype(int), y.astype(int) # to int
    x -= min(x) # trim zeros
    y -= min(y)

    grid = np.zeros((max(y)+1,max(x)+1)) # put text in grid
    for i in range(len(x)):
        grid[y[i]][x[i]] = 1

    plt.imshow(grid.T) # show text
    plt.show()


if __name__=='__main__':
        
    with open('input/10', 'r') as f: # read data
        table = str.maketrans(dict.fromkeys(',position=<\n>velocity=<'))
        data = [line.translate(table).split() for line in f] 
        x, y, dx, dy = np.asarray(data, dtype=float).T

    t = timesteps_to_centre(x, dx) # calculate timesteps
    x += t*dx # move to centre
    y += t*dy

    print('timesteps', t)
    show_message(x,y) # headshot -_-
