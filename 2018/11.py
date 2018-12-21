import numpy as np
import torch
import torch.nn.functional as F


def power_level(x, y): # compute power level
    rack_id = x + 10
    power = y * rack_id
    power += serial
    power *= rack_id
    power = int((power%1000)/100)
    power -= 5
    return power

def power_grid(size):
    grid = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            grid[i][j] = power_level(i+1, j+1)
    return grid

def conv_sum(ndarray, filtersize):
    if torch.cuda.is_available():
        device = "cuda" 
    else:
        device = "cpu"
    with torch.no_grad():
        tensor = torch.Tensor(ndarray[None, None, :, :], device=device) # to Tensor [1,1,300,300]
        filters = torch.ones(1,1,filtersize,filtersize) # 1 filter of 1's to sum
        convolved = F.conv2d(tensor, filters) # convolution
    return convolved.to("cpu").squeeze().numpy() # return numpy [298,298]

def sliding_window(ndarray, windowsize): # alternative for conv_sum 
    new_size = ndarray.shape[0] - windowsize + 1
    conv = np.zeros((new_size, new_size))
    for i in range(new_size):
        for j in range(new_size):
            conv[i,j] = ndarray[i:i+windowsize,j:j+windowsize].sum()
    return conv

def max_index(ndarray):
    index = np.unravel_index(np.argmax(conv, axis=None), conv.shape)
    return (index[0]+1, index[1]+1)

def max_value(ndarray):
    return int(np.max(ndarray))


if __name__=='__main__':
    serial = int(input('serial: ')) # get input
    grid = power_grid(300)
    conv = conv_sum(grid, 3)
        
    print(max_value(conv), max_index(conv))

    hi = dict.fromkeys(['value','size','index'])
    hi['value'] = -np.inf
    for size in range(1,301):
        conv = conv_sum(grid, size)
        #conv = sliding_window(grid, size)
        if max_value(conv) > hi['value']:
            hi['value'] = max_value(conv)
            hi['size'] = size
            hi['index'] = max_index(conv)
        print(size, '\thi:', hi)
