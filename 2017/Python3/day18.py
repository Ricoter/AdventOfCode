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

info = {chr(key+97):0 for key in range(26)}
i = 0
while i < len(data):
    line = data[i]
    if line[0] == 'snd':
        lastsound = info[line[1]]
    elif line[0] == 'set':
        try:
            info[line[1]] = int(line[2])
        except:
            info[line[1]] = info[line[2]]
    elif line[0] == 'add':
        try: 
            info[line[1]] += int(line[2])
        except:
            info[line[1]] += info[line[2]]
    elif line[0] == 'mul':
        try: 
            info[line[1]] *= int(line[2])
        except:
            info[line[1]] *= info[line[2]]
    elif line[0] == 'mod':
        try:
            info[line[1]] = info[line[1]] % int(line[2])
        except:
            info[line[1]] = info[line[1]] % info[line[2]]
    elif line[0] == 'rcv' and info[line[1]] != 0:
        print(lastsound)
        break
    elif line[0] == 'jgz' and info[line[1]] != 0:
        i += int(line[2])
        continue
    i += 1

