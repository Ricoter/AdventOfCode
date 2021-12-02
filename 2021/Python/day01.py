def part1(data):
    return sum([data[i-1]<data[i] for i in range(1,len(data))])


def part2(data):
    n = 0
    for i in range(4,len(data)+1):
        # sliding window
        a = sum(data[i-4:i-1])
        b = sum(data[i-3:i])

        if a < b:
            n += 1
    return n

if __name__=='__main__':
    with open('../Data/day01', 'r') as f:
        data = [int(line.strip('\n')) for line in f]

    print(part1(data))
    print(part2(data))