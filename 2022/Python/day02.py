"""
    Advent of Code 2022, Day 2     🎄
    Python v3.10.6
    Rico van Midde
"""

def readData(infile : str) -> list:
    """ creates a 2d numpy array

    Args:
        infile (str): pointer to input file

    Returns:
        list: _description_
    """
    with open(infile, 'r') as f:
        data = [line.strip('\n').split(' ') for line in f]
    print(data)
    return data

def part1(data):
    # points earned for draw / win
    draw = 3
    win = 6

    # total points
    points = 0
    for opp, you in data:
        # local points
        _points = 0

        # Rock
        if you == 'X':
            _points += 1
            if opp == 'A':
                _points += draw 
            elif opp == 'C':
                _points += win
        
        # Paper
        elif you == 'Y':
            _points += 2
            if opp == 'B':
                _points += draw 
            elif opp == 'A':
                _points += win

        # Scissors
        elif you == 'Z':
            _points += 3
            if opp == 'C':
                _points += draw 
            elif opp == 'B':
                _points += win

        # update total points
        points += _points
        
    return points

def part2(data):
    # translate XYZ for old meaning
    for i, line in enumerate(data):
        a, b = line
        
        # lose
        if b == 'X':
            if a == 'A':
                data[i][1] = 'Z'
            elif a == 'C':
                data[i][1] = 'Y'
        # draw
        elif b == 'Y':
            if a == 'A':
                data[i][1] = 'X'
            elif a == 'C':
                data[i][1] = 'Z'
        # win
        elif b == 'Z':
            if a == 'A':
                data[i][1] = 'Y'
            elif a == 'C':
                data[i][1] = 'X'
    return part1(data)

if __name__=='__main__':
    data = readData('../Data/day02')
    print(part1(data))
    print(part2(data))