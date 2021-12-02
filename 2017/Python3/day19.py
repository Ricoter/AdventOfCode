import numpy as np
import matplotlib as plt

V, H, TURN = '|', '-', '+' # vertical, horizontal, turn
LEFT, DOWN, UP, RIGHT  = np.array([0, -1]), np.array([1, 0]), np.array([-1, 0]), np.array([0, 1])

def main(data):

    pos = (0, np.where(data[0] == V)[0][0]) # must be tuple for indexing
    direction = DOWN # must be np.array for elementwise addition
    text = ''
    steps = 1

    while True:

        while data[pos] not in [TURN, ' ', 'Y']: # keep walking
            if data[pos].isalpha(): # save letter
                text += data[pos]

            pos = tuple(pos + direction) # update
            steps += 1
            
        if data[pos] == TURN: # turn
            print(data[pos], pos, type(direction), type(UP), DOWN)
            if np.all(direction == UP) or np.all(direction == DOWN):
                if data[tuple(pos + RIGHT)] == H:
                    direction = RIGHT
                elif data[tuple(pos + LEFT)] == H:
                    direction = LEFT
                else:
                    print('horizontal direction error', pos)
            elif np.array_equal(direction, LEFT) or np.array_equal(direction, RIGHT):
                if data[tuple(pos + DOWN)] == V:
                    direction = DOWN
                elif data[tuple(pos + UP)] == V:
                    direction = UP
                else:
                    print('vertical direction error', pos)
            pos = tuple(pos + direction)
            steps += 1

        if data[pos] == 'Y': # final letter
            text += 'Y'
            print(text, steps)
            break

    return 0

if __name__ == "__main__":
    with open("input/input19", 'r') as f:
        data = [[c for c in line.strip('\n')] for line in f]

    data = np.array(data)
    print(main(data))

