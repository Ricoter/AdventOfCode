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


def main(moves):
    pos = np.asarray(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
    tmp = np.copy(pos)
    N = int(1e9)

    # dance untill the pos is same as original
    for k in range(N):
        pos = dance(pos, moves)
        if (pos==tmp).all():
            back_to_base = k+1
            break
    
    # dance the leftovers
    for k in range(N%back_to_base):
        pos = dance(pos, moves)

    # convert to string
    final = ''.join(pos)
    
    return final


if __name__ == '__main__':
    with open('input/input16', 'r') as f:
        data = f.readline().strip().split(',')
    print(main(data))
