import numpy as np


def dance(pos, moves):
    for move in moves:
            if move[0] == 's':
                pos = np.roll(pos, int(move[1:]))
            elif move[0] == 'x':
                a,b = map(int, move[1:].split('/'))
                pos[a], pos[b] = pos[b], pos[a]
            elif move[0] == 'p':
                a,b = move[1:].split('/')
                i,j = np.where(pos==a), np.where(pos==b)
                pos[i], pos[j] = pos[j], pos[i]
    return pos


def main(data):
    
    # init array with programs
    prog = np.asarray(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])

    # copy programs to record index and partner swap/shifts after single full dance
    order = np.copy(prog)
    value = np.copy(prog)
    
    # single dance
    for move in data:
        if move[0] == 's':
            order = np.roll(order, int(move[1:]))
        elif move[0] == 'x':
            a,b = map(int, move[1:].split('/'))
            order[a], order[b] = order[b], order[a]
        elif move[0] == 'p':
            a,b = move[1:].split('/')
            i,j = np.where(value==a), np.where(value==b)
            value[i], value[j] = value[j], value[i]

    # convert order changes by index (s,x moves) to index values 
    order = np.asarray([ord(char)-97 for char in order])
    
    # billion dances. 1000*1000*1000*1 dance
    for _ in range(3):
        # partner swap mapping
        partners = {prog[i]:value[i] for i in range(16)}
        # index swap mapping
        d_index = np.copy(order)
        # initialize value and order
        value = np.copy(prog)
        order = np.asarray([ord(char)-97 for char in prog])
        # update state 1000 times
        for _ in range(1000):
            order = order[d_index]
            value = np.asarray(list(map(lambda x: partners[x], value)))

    # apply final position to prog
    prog = value[order]

    final = ''
    for i in prog:
        final += str(i)
    return final

if __name__ == '__main__':
    with open('input/input16', 'r') as f:
        data = f.readline().strip().split(',')
    #data = testdata
    print(main(data))
