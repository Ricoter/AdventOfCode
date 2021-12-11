import numpy as np
import re

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
    return data

def removeValidChunks(line):
    while True:
        newline = re.sub("\[\]|\(\)|\{\}|<>", "", line)
        if newline==line:
            break
        line = newline
    return line


def part1(data):
    points = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
    for line in data:
        line = removeValidChunks(line)
        for c in line:
            if c in points.keys():
                score += points[c]
                break
    return score

def part2(data):
    points = {'(':1, '[':2, '{':3, '<':4}
    scores = []
    for i, line in enumerate(data):
        line = removeValidChunks(line)
        scores.append(0)
        for c in line[::-1]:
            if c not in points.keys():
                scores.pop()
                break
            scores[-1] *= 5
            scores[-1] += points[c]
    scores = sorted(scores)
    return scores[len(scores)//2]

if __name__=='__main__':
    data = readData('../Data/day10')
    print(part1(data))
    print(part2(data))