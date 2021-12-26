import numpy as np
import time


def readData(infile):
    with open(infile, 'r') as f:
        data = []
        for line in f:
            line = line.strip('\n')
            if line == '':
                continue
            elif line.startswith('---'):
                data.append([])
            else:
                a, b, c = line.split(',')
                data[-1].append((int(a), int(b), int(c)))
    data = [np.array(x) for x in data]
    return data


def get_rotations():
    """ Provides 24 possible base rotations of a 3D vector

    Returns:
        list: list of numpy arrays
    """
    # rotations around x/y/z
    Rx = np.array([
        [1, 0, 0],
        [0, 0,-1],
        [0, 1, 0]
    ])
    Ry = np.array([
        [0, 0,-1],
        [0, 1, 0],
        [1, 0, 0]
    ])
    Rz = np.array([
        [0,-1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ])

    # Brute force
    R = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                R.append(np.eye(3))
                R[-1] = R[-1].dot(np.linalg.matrix_power(Rx, i))
                R[-1] = R[-1].dot(np.linalg.matrix_power(Ry, j))
                R[-1] = R[-1].dot(np.linalg.matrix_power(Rz, k))

    # make hashable
    R = [tuple(x.flatten()) for x in R]
    
    # save only unique rotations
    R = [np.reshape(x, (3,3)) for x in set(R)]

    return R

ROTATIONS = get_rotations()


def align_scanners(a, b):
    """ Loops over beacon combinations from scanner a and scanner b, where 24 rotations
    of scanner b are also in the loop. if there is an overlap it returns the rotated
    beamers and the scanner wrt to beamer a.

    Args:
        a (numpy.ndarray): scanner a with all beacons
        b (numpy.ndarray): scanner b with all beacons

    Returns:
        numpy.ndarray: IF there is 12 overlap it RETURNS b's beacons wrt a, ELSE 0
        numpy.ndarray: IF there is 12 overlap it RETURNS b's scanner wrt a, ELSE 0
    """
    for bb in b[:-12]:
        for R in ROTATIONS:
            rotated_beacons_b = [tuple(x) for x in (b-bb).dot(R)]
            for ba in a[:-12]:
                beacons_a = [tuple(x) for x in (a- ba)]
                total =  rotated_beacons_b + beacons_a
                if len(total) - len(set(total)) >= 11:
                    return (b-bb).dot(R) + ba, ba-bb.dot(R)
    return 0, 0
    

def Manhattan_distance(a, b):
    return sum(abs(a[i]-b[i]) for i in range(3))


def solve(data):
    scanners = []
    aligned = [data[0]]
    not_aligned = data[1:]
    while not_aligned:
        for a in aligned:
            for i, b in enumerate(not_aligned):
                aligned_b, sb = align_scanners(a, b)
                if type(aligned_b) == np.ndarray:
                    not_aligned.pop(i)
                    aligned.append(aligned_b)
                    scanners.append(sb)
                    print(len(not_aligned))

    n_beacons = len(set(tuple(y) for x in aligned for y in x))
    hi = max(Manhattan_distance(a, b) for a in scanners for b in scanners)
    return n_beacons, hi


if __name__=='__main__':
    data = readData('../Data/day19')
    tic = time.time()
    print(solve(data)) # Brute Force 14682.0
    print("time:", time.time()-tic)