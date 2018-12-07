import numpy as np

with open('input/5', 'r') as f: # read data
    data = np.asarray([ord(char) for char in f.read()]) # '\n' removes PBC imposed by np.roll

shift = 1
shifted_data = np.roll(data, shift) # imposes Periodic Boundary Conditions


i = 0
diff = ord('a') - ord('A')
for _ in range(2000):
    remove = ((data-shifted_data) == diff) # boolean list of reactions
    remove = remove + np.roll(remove,-shift) # include both reactants
    keep = ~remove # invert booleans
    data = data[keep] # keep non-reacting particles
    shift *= -1 # reverse shift aA --> Aa
    shifted_data = np.roll(data, shift) # shift new data
    

print(len(data)-1) # remove '\n'
