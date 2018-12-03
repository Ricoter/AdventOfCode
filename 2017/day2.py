import os
import sys

def read_data(input_file, data):
    with open(input_file, 'r') as f:
        for line in f:
            data.append([int(s) for s in line.split()])

def max_min(data):
    total = 0
    for line in data:
        total += max(line) - min(line)
    print('part1') total

def evenly_devise(data):
    total = 0
    for line in data:
        for i in range(len(line)):
            for j in range(len(line)):
                if i != j:
                    if line[i] % line[j] == 0:
                        total += int(line[i]/line[j])
    return total

#                   __main__
def main(input_file):
    data = []
    read_data(input_file, data)
    # part1 total of max-min value
    max_min(data)
    evenly_devise(data)


if __name__ == "__main__":
    # main(sys.argv[1])
    main("input2.in")
