"""
    Advent of Code 2022, Day 1     🎄
    Python v3.10.6
    Rico van Midde
"""

def readData(infile : str) -> list:
    data = [[]]
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip("\n")
            if line == "":
                data.append([])
            else:
                data[-1].append(int(line))
    return data


def part1(data):
    hi = 0
    for elf in data:
        hi = max(hi, sum(elf))
    return hi


def part2(data):
    totals = [sum(x) for x in data]
    return sum(sorted(totals)[-3:])


if __name__ == '__main__':
    data = readData('../Data/day01')

    print("part 1:", part1(data))
    print("part 2:", part2(data))
