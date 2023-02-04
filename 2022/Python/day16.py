"""
    Advent of Code 2022, Day 4     🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
from copy import deepcopy, copy
import re
import matplotlib.pyplot as plt
import networkx as nx



def readData(infile : str) -> dict:
    # rates = [] # for inspection only
    data = dict()
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            line = re.split(r" |=|;|, ", line)
            x = line[1]
            rate = line[5]
            Y = line[11:]
            data[x] = {'rate':int(rate), 'Y':Y}
            # rates.append(int(rate)) # for inspection only
    # print(sorted([x for x in rates if x > 0])) # for inspection only
    return data


def makeGraph(data:dict):
    G = nx.Graph()
    # G.add_nodes_from(data.keys(), size=10)
    for key, value in data.items():
        a = key
        # print(value, type(value))
        if a == 'AA':
            G.add_node(a, size=value['rate'], color='red')
        else:
            G.add_node(a, size=value['rate'])
        for b in value['Y']:
            G.add_edge(a,b)
    return G 


def showGraph(data:dict):
    from pyvis.network import Network
    G = makeGraph(data)
    net = Network()
    net.from_nx(G)
    net.show('test.html')


def find_steps(data:dict) -> dict:
    """ For each node: find distance to all other nodes with rate > 0
    the distance is defined as the time it takes to open the vulve at the next node
    (number of edges + 1)

    Args:
        data (dict): 

    Returns:
        dict: _description_
    """
    # Convert data to a graph type and find number of edges between nodes
    G = makeGraph(data)
    sp = dict(nx.all_pairs_shortest_path(G))

    # add all distances to relevant nodes for each node in the data dict
    nonzero_sp = dict()
    for key, value in sp.items():
        if data[key]['rate'] > 0 or key=='AA': 
            nonzero_sp[key] = []
            for k, v in value.items():
                if data[k]['rate'] > 0 or k=='AA':
                    nonzero_sp[key].append((k, data[k]['rate'], len(v))) # node, rate, distance
            nonzero_sp[key].sort(key=lambda x: x[2])
    # print(nonzero_sp)
    return nonzero_sp


def find_path(data:dict, visited:list, time_left:int, current_node:str) -> list:
    # add current position to visited list
    visited.add(current_node)

    # print(data[current_node])
    
    # try all nodes
    score_list = set()
    for node, rate, distance in data[current_node]:

        # nodes are sorted by distence -> all next nodes will exceed timelimit
        if (time_left - distance) <= 0:
            break 


        elif node not in visited:
            _time_left = time_left - distance
            _pressure = rate * _time_left
            _pressure += find_path(data, copy(visited), _time_left, node)
            score_list.add(_pressure)

    if score_list == set():
        return 0
    else:
        return max(score_list)


def find_double_path(data, visited, time_left, current_nodes, depth):
    
    score = 0
    player = np.argmax(time_left)

    for node, rate, distance in data[current_nodes[player]]:
        if depth <= 2:
            print(depth, node)

        # nodes are sorted by distence -> all next nodes will exceed timelimit
        if (time_left[player] - distance) <= 0:
            break 


        elif node not in visited:
            _time_left = time_left[::]
            _time_left[player] -= distance

            _current_nodes = current_nodes[::]
            _current_nodes[player] = node

            _pressure = rate * _time_left[player]
            _pressure += find_double_path(data, visited[::] + [node], _time_left, _current_nodes, depth+1)

            score = max(score, _pressure)
            if depth==1:
                print(score, _pressure)

    return score


def part1(data:dict) -> int:
    data = find_steps(data)
    visited = set()
    time = 30
    current_node = 'AA'
    x = find_path(data, visited, time, current_node)
    
    print(visited)
    # print(closed_valves)
    return x


def part2(data : dict) -> int:
    data = find_steps(data)
    visited = ['AA']
    time = [26, 26]
    current_nodes = ['AA', 'AA']
    x = find_double_path(data, visited, time, current_nodes, 1)
    return x


if __name__=='__main__':
    data = readData('../Data/day16')
    # print(data)
    showGraph(data)
    print("part 1:", part1(deepcopy(data)))
    print("part 2:", part2(data))