import numpy as np
from copy import deepcopy

# index variables of board items
STATE, VALUES, PUSHED = 0, 1, 2

BINS = ['0','1','2','3']
BUFFERS = ['l','01','12','23', 'r']
KEYS = ['l', '0', '01', '1','12','2','23','3','r']

HIGHSCORE = np.inf

def show(board):
    print(f"#{board['l'][1]}.{board['01'][1]}.{board['12'][1]}.{board['23'][1]}.{board['r'][1][::-1]}#")
    for c in '0123':
        print(board[c])


def check(bufs : list, board : dict, a : str) -> bool:
    for b in bufs:
        if b in ['01', '12', '23'] and board[b][1] and b != a:
            return False
    return True 


def solver(board : dict, points : int, bin_size : int, history : list = []) -> bool:
    global HIGHSCORE
    if [board[str(i)][STATE] for i in range(4)] == [0,0,0,0]:
        if points < HIGHSCORE:
            HIGHSCORE = points
            print(points)
            for line in history:
                print("\t", line)
        return True

    # from a to b
    for i, a in enumerate(KEYS):
        if board[a][VALUES] == []:
            continue

        # get first Amphipod
        amphipod = board[a][VALUES][-1]

        # buf/bin to bin
        if board[amphipod][STATE] > 0:

            # buffers in between
            k, l = sorted([i, int(amphipod)*2+1])
            if check(KEYS[k:l], board, a):
                new_board = deepcopy(board)
                new_points = points

                # update b
                new_board[amphipod][STATE] -= 1

                # update a
                new_board[a][VALUES].pop()
                if (a in BINS):
                    if new_board[a][VALUES]==[]:
                        new_board[a][STATE] = bin_size
                else:
                    new_board[a][STATE] += 1

                    # clear pushed
                    if a in ['l', 'r'] and new_board[a][VALUES]==[] and new_board[a][PUSHED]==1:
                        new_board[a][PUSHED] = 0

                # points
                steps = l-k
                new_points += 10**int(amphipod) * steps
                        
                if new_points >= HIGHSCORE:
                    continue

                new_history = history + [(amphipod, a, amphipod, new_points)]

                # evolve next state
                solver(new_board, new_points, bin_size, new_history)
                continue

        # bin to buffer
        if a in BINS:
            for j, b in enumerate(BUFFERS):
                if (board[b][STATE] > 0):

                    k, l = sorted([i, 2*j])
                    if check(KEYS[k:l], board, a):
                        new_board = deepcopy(board)
                        new_points = points

                        # update b
                        new_board[b][STATE] -= 1
                        new_board[b][VALUES].append(amphipod)

                        # update a
                        new_board[a][VALUES].pop()
                        if new_board[a][VALUES] == []:
                            new_board[a][STATE] = bin_size

                        # points
                        steps = l-k
                        new_points += 10**int(amphipod) * steps
                        
                        # pushed deeper
                        if b in ['l', 'r'] and new_board[b][STATE]==0 and new_board[b][PUSHED]==0:
                            new_board[b][PUSHED] = 1
                            new_points += 10**int(new_board[b][VALUES][0]) * 2

                        if new_points >= HIGHSCORE:
                            continue

                        new_history = history+[(amphipod, a, b, new_points)]

                        # evolve next state
                        solver(new_board, new_points, bin_size, new_history)

    return HIGHSCORE

        
def part1():
    """
        #############
        #...........#
        ###C#D#A#B###
          #B#A#D#C#
          #########

        A=0, B=1, C=2, D=3
    """
    # reset highscore and initialize board
    global HIGHSCORE
    HIGHSCORE = np.inf
    board = {
        '0': [-1, list('12')],
        '1': [-1, list('03')],
        '2': [-1, list('30')],
        '3': [-1, list('21')],
        'l': [2, [], 0],
        'r': [2, [], 0],
        '01': [1, []],
        '12': [1, []],
        '23': [1, []],
    }
    starting_points = 2*(2+1) * (1+10+100+1000)
    print("starting_points:", starting_points)
    return solver(board, points=starting_points, bin_size=2)
    

def part2():
    """
        #############
        #...........#
        ###C#D#A#B###
          #D#C#B#A#
          #D#B#A#C#
          #B#A#D#C#
          #########
        
        A=0, B=1, C=2, D=3
    """
    # reset highscore and initialize board
    global HIGHSCORE
    HIGHSCORE = np.inf
    board = {
        '0': [-1, list('1332')],
        '1': [-1, list('0123')],
        '2': [-1, list('3010')],
        '3': [-1, list('2201')],
        'l': [2, [], 0],
        'r': [2, [], 0],
        '01': [1, []],
        '12': [1, []],
        '23': [1, []],
    }
    starting_points = 2*(4+3+2+1) * (1+10+100+1000)
    print("starting_points:", starting_points)
    return solver(board, points=starting_points, bin_size=4)


if __name__=='__main__':
    print("\n\n# # PART ONE # #\n")
    print(part1()) #by hand
    print("\n\n# # PART TWO # #\n")
    print(part2())