import numpy as np


def readData(infile : str) -> list[list]:
    data = []
    with open(infile, 'r') as f:
        for line in f:
            x = line.strip('\n').split()
            if x[0] == 'inp':
                data.append([])
            data[-1].append(x)
    return data


def check(data : list[list]) -> int:
    """proves only that at all unique variables per pack are known"""
    known_differences = [(4,2), (5,2), (15,2)]
    diff = 0
    for k, pack in enumerate(data[1:]):
        for i, line in enumerate(pack):
            for j, x in enumerate(line):
                if (i,j) in known_differences:
                    continue
                elif data[0][i][j] != x:
                    diff += 1
                    print("difference found at:", k,i,j)
    print(diff,"unknown differences found")
    return diff
            

def solve(data : list[list], order : range) -> int:
    z = np.zeros(1)
    n = np.zeros(1)
    for i, pack in enumerate(data):
        # Operation Variables
        a = int(pack[4][2])
        b = int(pack[5][2])
        c = int(pack[15][2])

        new_z = np.array([])
        new_n = np.array([])
        for w in order:
            mask = ~((z%26) == (w-b))
            _z = np.copy(z)
            # _n = np.copy(n)
            # _n += w * 10**(13-i)

            _z //= a 
            _z[mask] *= 26
            _z[mask] += w+c
  
            new_z = np.concatenate((new_z, _z))
            new_n = np.concatenate((new_n, n+w*10**(13-i)))
        z, idx = np.unique(new_z, return_index=True)
        n = new_n[idx]
        # print(len(z))
        
    return int(n[z==0])


if __name__=='__main__':
    data = readData('../Data/day24')
    print(solve(data, order=range(9,0,-1))) # 52926995971999
    print(solve(data, order=range(1,10)))   # 11811951311485