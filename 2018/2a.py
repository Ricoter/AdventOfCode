from collections import Counter

with open('input/2', 'r') as f: # read data
    a = [line for line in f]

twos, threes = 0, 0 # initialize variables

for ID in a:
    counter = Counter(ID).values() # count all occurrences

    if 2 in counter: # update counters
        twos += 1
    if 3 in counter:
        threes += 1

checksum = twos * threes # calculate checksum
print(checksum) # print result

