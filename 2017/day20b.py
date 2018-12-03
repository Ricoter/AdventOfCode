import numpy as np
import torch

def main(data):
    for i in range(int(100)):
        data[:,1,:] += data[:,2,:] # v += a
        data[:,0,:] += data[:,1,:] # p += v
        doubles = set() 
        for j in range(np.shape(data)[0]):
            for k in range(np.shape(data)[0]):
                if j>k and np.array_equal(data[j,0,:], data[k,0,:]):
                    doubles.update([j,k])
        data = np.delete(data, list(doubles), axis=0)
        print('iteration:', i, 'new shape:', data.shape, 'removed:', len(doubles))

    print(np.shape(data))
if __name__ == '__main__':
        
    with open('input/input20', 'r') as f:
        # read data to list of lists of lists with dim [#particles, p/v/a, x/y/z] = [1000, 3, 3]
        data = [[list(map(lambda x: int(x), c.strip('apv=<>\n').split(','))) for c in line.split(', ')] for line in f]
    
    data = np.array(data)
    print(np.shape(data))
    main(data)
