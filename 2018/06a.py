import numpy as np

with open('input/6', 'r') as f:
    coordinates = [line.strip('\n').split(', ') for line in f]
coordinates = np.asarray(coordinates).astype(int) 

L = np.max(coordinates) -1

def manhattan(a,b):
    a, b = np.array(a), np.array(b)
    return(sum(abs(a-b)))

def minimal_distance(a, coordinates):
    minimal_distance = np.inf 
    for n, coor in enumerate(coordinates):
        distance = manhattan(coor, (i,j))
        if distance < minimal_distance:
            minimal_distance = distance
            num = n + 1
        elif distance == minimal_distance:
            num = -1
    return num
    
grid = np.zeros((L,L))
for i in range(L):
    for j in range(L):
        grid[j,i] = minimal_distance((i,j), coordinates)

print(grid)

import collections

counts = collections.Counter(grid.flatten())
counts[-1] = 0
edges = np.unique(np.array(list(np.unique(grid[0]))+list(np.unique(grid[L-1]))+ list(np.unique(grid[:,L-1]))+list( np.unique(grid[:,0])) ) )
for e in edges:
    counts[e] = 0
print(max(counts.values()))
print(counts)
