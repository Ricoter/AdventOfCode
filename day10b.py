import numpy as np

def main(inputstring):
        
    data = [ord(x) for x in inputstring]
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
            dPos = (n-1) + skipsize
            A = np.roll(A, -dPos)
            rolls += dPos
        
    # roll back to original position    
    sparsehash = np.roll(A, rolls)

    # XOR 16 slices of 16 numbers
    densehash = []    
    for i in range(16):
        tmp = 0
        for j in range(16):
            tmp ^= sparsehash[i*16 + j]
        densehash.append(tmp)

    # haxify 
    hexa = [hex(i).lstrip('0x') for i in densehash]
    hashed = ''
    for h in hexa:
        # padding
        if len(h) == 1:
            hashed += '0'
        hashed += h

    return(hashed)

if  __name__ == "__main__":
    realinput = '31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33'
    testinput = ['', 'AoC 2017', '1,2,3', '1,2,4']
    testcheck = ['a2582a3a0e66e6e86e3812dcb672a272', '33efeb34ea91902bb2f59c9920caa6cd',
                 '3efbe78a8d82f29979031a4aa0b16a9d', '63960835bcdc130f0b66d7ff4f6a5a8e']

    # check test input
    testhash = [main(i) for i in testinput]
    if testhash == testcheck:
        print('test complete')
    else:
        print('test failed\n', testhash, '\n', testcheck)

    print(main(realinput))
