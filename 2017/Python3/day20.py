with open('input20', 'r') as f:
    data = [sum(list(map(lambda x: abs(int(x)), line.split(', ')[-1].strip('a=<>\n').split(',')))) for line in f]
print(data.index(min(data)))
print(len(data))
