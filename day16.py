import numpy as np

def main(data):
    print(data)
    prog = np.asarray(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
    
    order = np.asarray(list(range(16)))

    for move in data:
        if move[0] == 's':
            prog = np.roll(prog, int(move[1:]))
        elif move[0] == 'x':
            a,b = map(int, move[1:].split('/'))
            prog[a], prog[b] = prog[b], prog[a]
        elif move[0] == 'p':
            a,b = move[1:].split('/')
            i,j = np.where(prog==a), np.where(prog==b)
            prog[i], prog[j] = prog[j], prog[i]

    return prog

if __name__ == '__main__':
    with open('input/input16', 'r') as f:
        data = f.readline().split(',')
    #data = testdata
    print(main(data))
