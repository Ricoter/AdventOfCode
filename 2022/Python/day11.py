"""
    Advent of Code 2022, Day 11     🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
import numpy as np
import copy
import re

def readData(infile : str) -> list:
    """Create a list of monkeys from infile, each monkey is a dict with keys:
        'Business' : (int) total number of items trowed
        'Items' : (list of integers) current items
        'Operation' : (lambda function) returning the new item value
        'Test' : (lambda function) returning if test is passed with boolean
        True : (int) next monkey number
        False : (int) next monkey number
    """
    monkeys = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            sline = re.split(r" |: |, ", line)

            if sline[0] == "Monkey":
                # add new monkey
                monkeys.append({'Business' : 0})

            elif sline[0] == 'Starting':
                # "Starting items: 79, 98" -> [79, 98]
                monkeys[-1]['Items'] = [int(x) for x in sline[2:]]

            elif sline[0] == 'Operation':
                # "Operation: new = old * 19" -> lambda x : (x * 19) // 3
                monkeys[-1]['Operation']= line.split('= ')[1]
                # print(opstr)
                # operation = lambda old : (opstr // 3)
                # monkeys[-1]['Operation'] = operation

            elif sline[0] == 'Test':
                # "Test: divisible by 23" -> lambda x : (x % 23 == 0)
                # monkeys[-1]['Test'] = lambda x : (x % int(sline[-1]) == 0)
                monkeys[-1]['Test'] = int(sline[-1])


            elif sline[0] == "If":
                # Create corresponding boolean key with next monkey idx
                monkeys[-1][sline[1] == 'true'] = int(sline[-1])
    return monkeys


def part1(monkeys : list) -> int:
    for round in range(20):
        for i, monkey in enumerate(monkeys):
            for item in monkey['Items']:
                old = item
                item = eval(monkey['Operation']) // 3
                boolean = item%monkey['Test'] == 0
                new_monkey_index = monkey[boolean]
                monkeys[new_monkey_index]['Items'].append(item)
            # clean monkey items and update business points
            monkeys[i]['Business'] += len(monkeys[i]['Items'])
            monkeys[i]['Items'] = []
        
    business_points = [x['Business'] for x in monkeys]
    print(business_points)
    business_points.sort()
    return business_points[-2] * business_points[-1]


def part2(monkeys : list) -> int:
    large_modulus = np.prod([x['Test'] for x in monkeys])
    for round in range(10000):
        for i, monkey in enumerate(monkeys):
            for item in monkey['Items']:
                old = item
                item = eval(monkey['Operation']) % large_modulus
                boolean = item%monkey['Test'] == 0
                new_monkey_index = monkey[boolean]
                monkeys[new_monkey_index]['Items'].append(item)
            # clean monkey items and update business points
            monkeys[i]['Business'] += len(monkeys[i]['Items'])
            monkeys[i]['Items'] = []
        
    business_points = [x['Business'] for x in monkeys]
    business_points.sort()
    return business_points[-2] * business_points[-1]


if __name__=='__main__':
    data = readData('../Data/day11')
    print(data)

    print("part 1:", part1(copy.deepcopy(data)))
    print("part 2:", part2(data))