from collections import defaultdict

with open('input/7', 'r') as f:
    data = [(line[5], line[36]) for line in f]

d = defaultdict(list) # make a dictionary where each parent has a list of its children
for parent, child in data:
    d[parent].append(child)

all_children = set([i for j in d.values() for i in j]) # make a set of all values that are children

order = [] # order of steps
ready = sorted([parent for parent in d.keys() if parent not in all_children]) # all parents that are not children are ready for the first step

while ready:
    parent = ready.pop(0) # get the next parent
    children = d[parent] # get its children
    del d[parent] # delete the parent:children pair from dict
    for child in children: 
        all_children = [i for j in d.values() for i in j] # find all current children in dict
        if child not in all_children: # if child is not linked to another parent it is ready
            ready.append(child)

    order.append(parent) # update order
    ready = sorted(ready) # sort alphabetically

print(''.join(order))
