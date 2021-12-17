import numpy as np
import matplotlib.pyplot as plt

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    
    # Convert to numpy matrix
    data = np.array([list(line) for line in data]).astype(int)
    return data

def find_neighbours(coordinate, rows, cols):
    """ return neightbours within boundary """
    i, j = coordinate
    neighbours = (i+1,j), (i-1,j), (i, j-1), (i, j+1)
    return [(i, j) for i, j in neighbours if 0<=i<rows and 0<=j<cols]

def part1(data):
    rows, cols = data.shape

    # dict for fast lookup
    edges = {data[0,0]: [(0,0)]}

    # set for fast lookup
    computed = set([(0,0)])

    while len(computed) < np.size(data):
        lowest_edges = edges.pop(min(edges))
        for e in lowest_edges:
            for i, j in find_neighbours(e, rows, cols):
                # skip computed neighbours
                if (i,j) in computed:
                    continue

                # update tile value
                data[i, j] += data[e]

                # return when finished
                if (i,j) == (rows-1,cols-1):
                    return data[i,j] - data[0,0]
                
                # update edge tiles
                if data[i,j] not in edges:
                    edges[data[i,j]] = [(i,j)]
                else:  
                    edges[data[i,j]].append((i,j))
                
                # update list of computed tiles
                computed.add((i,j))
    return 0


def increase_map(map):
    rows, cols = map.shape

    # intialize empty map
    new_map = np.zeros((5*rows, 5*cols))
    for i in range(5):
        for j in range(5):
            # copy full tile with added value
            new_map[i*rows:(i+1)*rows, j*cols:(j+1)*cols] = map + i + j
    
    # show the new map
    plt.imshow(new_map)
    plt.show()

    # every 9 goes back to 1
    return ((new_map-1) % 9 + 1).astype(int)


def part2(data):
    return part1(increase_map(data))


if __name__=='__main__':
    data = readData('../Data/day15')
    print(part1(np.copy(data)))
    print(part2(data))