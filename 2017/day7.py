import os
import sys

def read_data(input_file, data, weights):
    with open(input_file, 'r') as f:
        for line in f:
            tmp = []
            n = line.split()
            tmp.append(n[0])
            weights[n[0]] = int(n[1].strip('()'))
            if len(n)>2:
                for name in n[3:]:
                    name = name.strip(',')
                    tmp.append(name)
            data.append(tmp)

def mode(arr):
    # takes list, returns most common value
    return max(set(arr), key=arr.count)

def recursive_search(data, bottom_name, weights):
    # find given tower
    for tower in data:
        if tower[0] == bottom_name:
            # return only weight of itself, if tower is of length 1 (on top)
            if len(tower)==1:
                return weights[tower[0]]
            # return weight of itself + sum of all weights above it
            else:
                # list all weights above it (recursively)
                w = []
                for name in tower[1:]:
                    tmp = recursive_search(data, name, weights)
                    # remove 'None' values from towers that did not match bottom_name? TODO check what happens
                    if tmp != None:
                        w.append(tmp)
                # check if all 'i' weights in 'w' are balanced (the same)
                for n,i in enumerate(w):
                    # if not balanced
                    if i != mode(w):
                        # find difference
                        diff = mode(w) - i
                        # add difference to the unbalanced weight
                        answer = weights[tower[n+1]] + diff
                        print("Weight of '{}' should be: {}".format(tower[n+1], answer))
                        return
                # return weight of itself + sum of all weights above it
                return sum(w)+weights[tower[0]]

def absolute_bottom(data):
    bottom, rest = [], []
    for tower in data:
        for i, name in enumerate(tower):
            if i == 0:
                bottom.append(name)
            else:
                rest.append(name)

    for name in bottom:
        if name not in rest:
            print("Name of bottom disk: {}".format(name))
            return(name)

def main(input_file):
    data, weights = [], dict()
    read_data(input_file, data, weights)
    bottom_name = absolute_bottom(data)
    recursive_search(data[:], bottom_name, weights)

if __name__ == '__main__':
    main('input7.in')
