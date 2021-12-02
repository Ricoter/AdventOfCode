def getData(infile):
    with open('../Data/day02', 'r') as f:
        data = [list(line.strip('\n').split()) for line in f]
    return data

navigator = {
    'forward': [1, 0],
    'down': [0, 1],
    'up': [0, -1]
}

def part1(data):
    x, y = 0, 0
    for direction, value in data:
        dx, dy = navigator[direction]
        x += dx * int(value)
        y += dy * int(value)
    
    return x * y

def part2(data):
    x, y, aim = 0, 0, 0
    for direction, value in data:
        dx, daim = navigator[direction]
        x += dx * int(value)
        aim += daim * int(value)
        y += dx * aim * int(value)
    
    return x * y

if __name__=='__main__':
    data = getData('../Data/day02')
    print(part1(data))
    print(part2(data))