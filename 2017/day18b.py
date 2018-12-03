import numpy as np
import ipdb

# Read data
with open('input/input18', 'r') as f:
    data = [line.split() for line in f]

testdata = [['set', 'a', '1'],
            ['add', 'a', '2'],
            ['mul', 'a', 'a'],
            ['mod', 'a', '5'],
            ['snd', 'a'],
            ['set', 'a', '0'],
            ['rcv', 'a'],
            ['jgz', 'a', '-1'],
            ['set', 'a', '1'],
            ['jgz', 'a', '-2']]


def operator(instructions, reg, snd, rcv, i): 
    line = instructions[i]
    if line[0] == 'snd':
        snd.append(reg[line[1]])
    elif line[0] == 'set':
        try:
            reg[line[1]] = int(line[2])
        except:
            reg[line[1]] = reg[line[2]]
    elif line[0] == 'add':
        try: 
            reg[line[1]] += int(line[2])
        except:
            reg[line[1]] += reg[line[2]]
    elif line[0] == 'mul':
        try: 
            reg[line[1]] *= int(line[2])
        except:
            reg[line[1]] *= reg[line[2]]
    elif line[0] == 'mod':
        try:
            reg[line[1]] = reg[line[1]] % int(line[2])
        except:
            reg[line[1]] = reg[line[1]] % reg[line[2]]
    elif line[0] == 'rcv':
        if not rcv:
            waiting = True
            return (i, waiting)
        reg[line[1]] = rcv.pop(0) 
    elif line[0] == 'jgz':
        try:
            tmp = reg[line[1]]
        except:
            tmp = int(line[1])
            
        if tmp > 0:
            try:
                i += int(line[2]) - 1 # minus general update
            except:
                i += reg[line[2]] -1
    # return updated index
    return (i+1, False)

# initialize registers
reg0 = {chr(key+97):0 for key in range(26)}
reg1 = {chr(key+97):0 for key in range(26)}
print(type(reg0))
reg1['p'] = 1

i, j = 0, 0 # instruction index
que0, que1 = [], [] # send/recieve queue
sends = 0
# ipdb.set_trace()
while True:
    wait0, wait1 = False, False # is waiting?

    # run program 0
    i, wait0 = operator(data, reg0, que0, que1, i)
        
    bup = len(que1)
    # run program 1
    j, wait1 = operator(data, reg1, que1, que0, j)
    bep = len(que1)
    if bup!=bep:
        sends += 1
        print(sends)

    # check index
    if not (0 <= i < len(data)) and not (0 <= j < len(data)):
        print("Index out of range")
        break
    if wait0 and wait1:
        print("Deadlock reached")
        break

        

