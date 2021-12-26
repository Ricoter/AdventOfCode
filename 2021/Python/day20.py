import numpy as np
import matplotlib.pyplot as plt

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]

    # boolean arrays
    enhancement = (np.array(list(data[0])) == '#')
    img = (np.array([list(line) for line in data[2:]]) == '#')

    # binary
    return img.astype(int), enhancement.astype(int)


def solve(data, runs):
    img, enhancement = data
    bitify = np.array([256,128,64,32,16,8,4,2,1])

    pad_value = 0
    img = np.pad(img, pad_width=1, mode='constant', constant_values=pad_value)
    for _ in range(runs):
        
        new_img = np.zeros_like(img)
        rows, cols = new_img.shape
        img = np.pad(img, pad_width=1, mode='constant', constant_values=pad_value)
        
        for i in range(rows):
            for j in range(cols):
                k = img[i:i+3, j:j+3].flatten()
                k = k.dot(bitify)
                new_img[i,j] = enhancement[k]
        
        pad_value = enhancement[pad_value]
        img = np.pad(new_img, pad_width=1, mode='constant', constant_values=pad_value)

    
    return np.sum(img)

def part2(data):
    return 

if __name__=='__main__':
    data = readData('../Data/day20')
    print(solve(data, 2))
    print(solve(data, 50))