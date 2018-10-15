import numpy as np

# read data
#data = []
#with open("input10t", "r") as f:
#    for character in f.readline().strip():
#        data.append(ord(character))

data = [ord(x) for x in "31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33"]

# add extra
data += [17, 31, 73, 47, 23]

# init array
A = np.asarray(range(256))
skipsize = 0
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

# haxify 
hexa = [hex(i).strip('0x') for i in densehash]
hashed = ''
for h in hexa:
    # padding
    if len(h) == 1:
        hashed += '0'
    hashed += h

print(hashed)
