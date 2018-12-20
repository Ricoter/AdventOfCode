import numpy as np

test = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
test = [line.strip('#') for line in test]

with open('input/3', 'r') as f:
    data = [line.strip('\n#') for line in f]

#data = test # '1 @ 1,3: 4x4'

data = [x.split() for x in data] # ['1', '@', '1,3:', '4x4']

data = [[i] + j.strip(':').split(',') + k.split('x') for i, _, j, k in data] # ['1', '1', '3', '4', '5']

grid = np.zeros((10000,10000))
for line in data:
    for row in range(int(line[3])):
        for col in range(int(line[4])):
            grid[int(line[1])+row][int(line[2])+col] += 1

overlap = (grid>1).sum()
print(overlap)
print(grid)
