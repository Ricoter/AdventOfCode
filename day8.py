import numpy as np
import operator

data = []

with open('input8', 'r') as f:
    for line in f:
        data.append(line.split())

scores = {}
for i in data:
    scores[i[0]] = 0

print(scores)

ops = {'inc': operator.add, 'dec': operator.sub,
        '==': operator.eq, '>=': operator.ge,
        '>': operator.gt, '<=': operator.le,
        '<': operator.lt, '!=': operator.ne,
        }

max_score = 0

for l in data:
    
    if ops[l[5]](scores[l[4]], int(l[6])):
        tmp = ops[l[1]](scores[l[0]], int(l[2]))
        scores[l[0]] = tmp
        max_score = max(max_score, tmp)

print(scores[max(scores.items(), key=operator.itemgetter(1))[0]])
print("max:", max_score)
    
