def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n').split('-') for line in f]

    # lookup dict for connected caves
    d = {y:[] for x in data for y in x}
    for a, b in data:
        d[a].append(b)
        d[b].append(a)

    return d


def recursivePathFinder(curr, d, visited={'start'}, joker='used'):
    total = 0
    for cave in d[curr]:
        if cave == 'end':
            total += 1
            continue
        elif cave == 'start':
            continue

        if cave.islower() and (cave in visited):

            # edit for part 2
            if joker == 'unused':
                total += recursivePathFinder(cave, d, visited|{cave}, joker='used') # <- local joker is not changed, therefor both paths are walked
            
            continue

        total += recursivePathFinder(cave, d, visited|{cave}, joker)
    return total


if __name__=='__main__':
    data = readData('../Data/day12')
    print(recursivePathFinder('start', data, {'start'}))
    print(recursivePathFinder('start', data, {'start'}, joker='unused'))