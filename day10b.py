import numpy as np

# read data
data = []
with open("input10", "r") as f:
    for character in f.readline().strip():
        data.append(ord(character))

# add extra
data += [17, 31, 73, 47, 23]
# run list 64 times
#data = data*64

# init array
A = np.asarray(range(256))
skipsize = 0
index = 0
rolls = 0
for i in range(64):
    for n in data:
        # revert n numbers
        A[:n] = A[:n][::-1]
        # get to the right position and keep track to roll back later
        skipsize += 1
        A = np.roll(A,-( n - 1 + skipsize))
        rolls += n + skipsize -1
    
# roll back    
sparsehash = np.roll(A, rolls)

# XOR 16 slices of 16 numbers
densehash = []    
for i in range(16):
    tmp = 0
    for j in range(16):
        tmp ^= sparsehash[i*16 + j]
    densehash.append(tmp)

# haxify numbers and add pad with '0' in front to get 2 characters
hexa = [hex(i).strip('0x') for i in densehash]
hashed = ''
for h in hexa:
    if len(h) == 1:
        hashed += '0'
    hashed += h
    print(hashed)


print(hexa)
print(hashed)

print(A)
print(A[0]*A[1])
