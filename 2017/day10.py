import numpy as np

# read data
with open("input10", "r") as f:
    data = f.readline().strip('\n').split(',')

# convert to int
data = list(map(int, data))
print(data)

A = np.asarray(range(256))
skipsize = 0
index = 0
rolls = 0
for n in data:
    A[:n] = A[:n][::-1]
    skipsize += 1
    A = np.roll(A,-( n - 1 + skipsize))
    rolls += n + skipsize -1
    
A = np.roll(A, rolls)
print(A)
print(A[0]*A[1])
