from collections import defaultdict

test = 0

if test:
    infile = 'input/7test'
    n_workers = 2
    n_values = 6
    dt = 0
else:
    infile = 'input/7'
    n_workers = 5
    n_values = 26
    dt = 60

with open(infile, 'r') as f:
    data = [(line[5], line[36]) for line in f]

d = defaultdict(list) # make a dictionary where each parent has a list of its children
for parent, child in data:
    d[parent].append(child)

all_children = set([i for j in d.values() for i in j]) # make a set of all values that are children

order = [] # order of steps
ready = sorted([parent for parent in d.keys() if parent not in all_children]) # all parents that are not children are ready for the first step

workers = [list() for _ in range(n_workers)]

import ipdb
#ipdb.set_trace()

counter =  -1
while ready or len(order) != n_values:

    # distribute jobs to workers
    for worker in workers:
        if worker != []: # if worker has a job
            worker[0][1] -= 1 # substract 1 time unit
            if worker[0][1] == 0: # if job is finished
                parent, _ = worker.pop(0) # free worker and take parent
                children = d[parent] # find parents children
        
                del d[parent] # free children 
                all_children = [i for j in d.values() for i in j] # update remaining children

                for child in children: # append children without parents to ready
                    if child not in all_children:
                        ready.append(child)

                order.append(parent) # update order

    for worker in workers:
        if worker == []: # if worker has no job
            if ready != []: # check if jobs are available
                ready = sorted(ready) # sort alphabetically
                parent = ready.pop(0) # next parent
                time = dt + ord(parent) - 64 # jobtime
                worker.append([parent, time]) # give job to worker
              
    print(workers)
    counter += 1


print('Part A:', ''.join(order))
print('Part B:', counter)
# 925 < answer < 937, 938 , !930, !932, !933
print(len(workers))

