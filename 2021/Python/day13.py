import numpy as np
from matplotlib import pyplot as plt 

def readData(infile):
    with open(infile, 'r') as f:
        paper, folds = [], []
        for line in f:
            if line[0].isdigit():
                x, y = line.strip('\n').split(',')
                paper.append([int(x), int(y)])
            elif line[0].startswith('f'):
                _, _, fold = line.strip('\n').split()
                if fold[0] == 'x': # transposed wrt to lists or numpy
                    axis = 0
                else:
                    axis = 1
                folds.append((axis, int(fold[2:])))
    # print(paper, folds)
    
    # data = [line.split(' ') for line in data]
    # data = np.array([list(line) for line in data]).astype(int)
    return (paper, folds)

def part1(data):
    paper, folds = data
    ax, f = folds[0]

    for i, _ in enumerate(paper):
        if paper[i][ax] > f:
            paper[i][ax] = 2*f-paper[i][ax]
    paper = set(tuple(x) for x in paper)
    return len(paper)


def part2(data):
    paper, folds = data
    size = [0,0]
    for ax, f in folds:
        for i, _ in enumerate(paper):
            if paper[i][ax] > f:
                paper[i][ax] = 2*f-paper[i][ax]
        size[ax] = f
    paper = list(set(tuple(x) for x in paper))
    matrix = np.zeros(size)
    for x, y in paper:
        matrix[x, y] = 1
    plt.imshow(matrix.T)
    plt.show()
    return "read the image ;)"


if __name__=='__main__':
    data = readData('../Data/day13')
    print(part1(data))
    print(part2(data))