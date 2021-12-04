import numpy as np

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]

    numbers = np.array(data[0].split(',')).astype(int)
    cards = []
    for line in data[1:]:
        if line == '':
            cards.append([])
            continue
        cards[-1].append(line.split())

    cards = np.array(cards).astype(int)
    return numbers, cards

def check(card):
    for i in range(len(card)):
        if sum(card[i,:]) == -5 or sum(card[:,i]) == -5:
            return True
    return False

def part1(data):
    numbers, cards = data
    for n in numbers:
        for card in cards:
            card[card==n] = -1
            if check(card):
                card[card==-1] = 0
                return np.sum(card) * n
    return 0

def part2(data):
    numbers, cards = data
    counter = len(cards)
    for n in numbers:
        for card in cards:
            card[card==n] = -1
            if check(card):
                if counter == 1:
                    card[card==-1] = 0
                    return np.sum(card) * n
                counter -= 1
                card[:,:] = -2
    return 0

if __name__=='__main__':
    data = readData('../Data/day04')
    print(part1(data))
    print(part2(data))