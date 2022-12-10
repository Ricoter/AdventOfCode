"""
    Advent of Code 2022, Day 6     🎄🎄🎄🎄🎄🎄
    Python v3.10.6
    Rico van Midde
"""
def readData(infile : str) -> str:
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    return data[0]


def solve(data : str, n : int) -> int:
    for i in range(len(data)-n-1):
        chunk = data[i:i+n]
        if len(set(chunk)) == n:
            return i+n


def part1(data):
    return solve(data, 4)


def part2(data):
    return solve(data, 14)


if __name__=='__main__':
    data = readData('../Data/day06')
    # print(data)

    print("part 1:", part1(data))
    print("part 2:", part2(data))