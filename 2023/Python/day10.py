"""
    Advent of Code 2023, Day 4     🎄🎄🎄🎄
    Python v3.10.12
    Rico van Midde
"""
import numpy as np
from copy import deepcopy
import re
from time import time


def readData(infile : str) -> np.array:
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            data.append(line)
            
    # # to numpy 2D array (characterwise)
    data = np.array([list(line) for line in data])
    return data

# dictionary of pipes
pipes = {
    '|' : {'N' : 'S', 'S' : 'N'},   # | is a vertical pipe connecting north and south.
    '-' : {'E' : 'W', 'W': 'E'},    # - is a horizontal pipe connecting east and west.
    'L' : {'N' : 'E', 'E' : 'N'},   # L is a 90-degree bend connecting north and east.
    'J' : {'N' : 'W', 'W': 'N'},    # J is a 90-degree bend connecting north and west.
    '7' : {'S' : 'W', 'W' : 'S'},   # 7 is a 90-degree bend connecting south and west.
    'F' : {'S' : 'E', 'E' : 'S'},   # F is a 90-degree bend connecting south and east.
}

directions = {'N' : (-1, 0), 'S' : (1, 0), 'E' : (0, 1), 'W' : (0, -1)}
opposite = {'N' : 'S', 'S' : 'N', 'E' : 'W', 'W' : 'E'} # switch incoming and outgoing direction


def find_start_neighbour(data : np.array) -> list:
    S = np.where(data == 'S')
    S = np.array(S).flatten()
    # find one neighbour of the starting pipe
    for o in directions.keys():
        x = S + directions[o] # neighbour
        try: 
            i = opposite[o] # switch outgoing to incoming direction
            p = data[x[0], x[1]]
            if i in pipes[p].keys():
                return S, x, o
        except:
            pass
    


def part1(data : np.array) -> int:
    S, x, o = find_start_neighbour(data)
    visited = [tuple(S)]
    while data[x[0], x[1]] != 'S':
        visited.append(tuple(x))

        i = opposite[o] # incoming direction
        p = data[x[0], x[1]]
        o = pipes[p][i] # outgoing direction after pipe
        x += directions[o]
        
    return len(visited) // 2, visited


def type_S(visited : list, data : np.array) -> list:
    S = visited[0]
    b = visited[1]
    e = visited[-1]

    conn_b = S[0] - b[0], S[1] - b[1]
    conn_e = S[0] - e[0], S[1] - e[1]

    connections = [k for k, v in directions.items() if v in [conn_b, conn_e]]

    # find pipe type
    for p in pipes.keys():
        p_conn = list(pipes[p].keys())
        if p_conn.sort() == connections.sort():
            return p


def part2(data : np.array) -> int:
    _, visited = part1(data)

    # find and replace the type of S
    data[visited[0][0], visited[0][1]] = type_S(visited, data)
    visited = set(visited)
    for i in range(data.shape[0]):
        is_inside = False
        
        # if above & below are True, we crossed a pipe 
        # Example: F7 or L--J does not cross a pipe, but F---J does 
        above = False # connected to above pipe ('|' or 'L' or 'J')
        below = False # connected to below pipe ('|' or 'F' or '7')

        for j in range(data.shape[1]):
            # we are inside when a odd number of pipes are crossed 
            if (i,j) in visited:
                # check if pipe is crossed
                match data[i,j]:
                    case '|':
                        above = not above
                        below = not below
                    case 'L' | 'J':
                        above = not above
                    case 'F' | '7':
                        below = not below

            if above and below:
                is_inside = not is_inside # switch
                above = False
                below = False
            elif is_inside and (i,j) not in visited :
                data[i,j] = 'X'
        # print((data == 'X').sum())


    return (data == 'X').sum()
    # 440 too high

if __name__=='__main__':
    tic = time()
    data = readData('../Data/day10')
    print("data:", data, "\ntime:", time()-tic)

    tic = time()
    print("part 1:", part1(deepcopy(data))[0], 'time:', time()-tic)
    tic = time()
    print("part 2:", part2(data), 'time:', time()-tic)