import numpy as np

with open('input/5', 'r') as f: # read data
    fulldata = np.asarray([ord(char) for char in f.read()]) # '\n' removes PBC imposed by np.roll



diff = ord('a') - ord('A')
smallest = np.inf
for c in range(ord('a'), ord('z')+1):
    data = fulldata[~(fulldata == c)]
    data = data[~(data == (c-diff))]
    shift = 1
    print(data[:100])
    shifted_data = np.roll(data, shift) # imposes Periodic Boundary Conditions
    for _ in range(5000):
        remove = ((data-shifted_data) == diff) # boolean list of reactions
        remove = remove + np.roll(remove,-shift) # include both reactants
        keep = ~remove # invert booleans
        data = data[keep] # keep non-reacting particles
        shift *= -1 # reverse shift aA --> Aa
        shifted_data = np.roll(data, shift) # shift new data
    if (len(data) - 1) < smallest:
        smallest = len(data) - 1

print(smallest)
