import numpy as np

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
    for _ in range(runs):
        # create output img
        rows, cols = img.shape[0] + 2, img.shape[1] + 2
        new_img = np.zeros((rows, cols), int)

        # pad input img
        img = np.pad(img, pad_width=2, mode='constant', constant_values=pad_value)

        for i in range(rows):
            for j in range(cols):
                # window to binary array
                x = img[i:i+3, j:j+3].flatten()

                # binary array to integer
                x = x.dot(bitify)

                # write output img
                new_img[i,j] = enhancement[x]
        
        # updates
        pad_value = enhancement[pad_value]
        img = new_img

    return np.sum(img)


if __name__=='__main__':
    data = readData('../Data/day20')
    print(solve(data, 2))
    print(solve(data, 50))